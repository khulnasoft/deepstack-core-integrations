import os
from unittest.mock import patch

import pytest
from deepstack_integrations.document_stores.pgvector import PgvectorDocumentStore


@pytest.fixture
def document_store(request):
    os.environ["PG_CONN_STR"] = "postgresql://postgres:postgres@localhost:5432/postgres"
    table_name = f"deepstack_{request.node.name}"
    embedding_dimension = 768
    vector_function = "cosine_similarity"
    recreate_table = True
    search_strategy = "exact_nearest_neighbor"

    store = PgvectorDocumentStore(
        table_name=table_name,
        embedding_dimension=embedding_dimension,
        vector_function=vector_function,
        recreate_table=recreate_table,
        search_strategy=search_strategy,
    )

    yield store

    store.delete_table()


@pytest.fixture
def patches_for_unit_tests():
    with patch("deepstack_integrations.document_stores.pgvector.document_store.connect") as mock_connect, patch(
        "deepstack_integrations.document_stores.pgvector.document_store.register_vector"
    ) as mock_register, patch(
        "deepstack_integrations.document_stores.pgvector.document_store.PgvectorDocumentStore.delete_table"
    ) as mock_delete, patch(
        "deepstack_integrations.document_stores.pgvector.document_store.PgvectorDocumentStore._create_table_if_not_exists"
    ) as mock_create, patch(
        "deepstack_integrations.document_stores.pgvector.document_store.PgvectorDocumentStore._handle_hnsw"
    ) as mock_hnsw:

        yield mock_connect, mock_register, mock_delete, mock_create, mock_hnsw


@pytest.fixture
def mock_store(patches_for_unit_tests, monkeypatch):  # noqa: ARG001  patches are not explicitly called but necessary
    monkeypatch.setenv("PG_CONN_STR", "some-connection-string")
    table_name = "deepstack"
    embedding_dimension = 768
    vector_function = "cosine_similarity"
    recreate_table = True
    search_strategy = "exact_nearest_neighbor"

    store = PgvectorDocumentStore(
        table_name=table_name,
        embedding_dimension=embedding_dimension,
        vector_function=vector_function,
        recreate_table=recreate_table,
        search_strategy=search_strategy,
    )

    yield store
