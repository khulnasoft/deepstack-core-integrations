# SPDX-FileCopyrightText: 2023-present khulnasoft GmbH <info@khulnasoft.com>
#
# SPDX-License-Identifier: Apache-2.0
from unittest.mock import Mock, patch

from deepstack.dataclasses import Document
from deepstack.utils import Secret

from deepstack_integrations.components.retrievers.pinecone import PineconeEmbeddingRetriever
from deepstack_integrations.document_stores.pinecone import PineconeDocumentStore


def test_init_default():
    mock_store = Mock(spec=PineconeDocumentStore)
    retriever = PineconeEmbeddingRetriever(document_store=mock_store)
    assert retriever.document_store == mock_store
    assert retriever.filters == {}
    assert retriever.top_k == 10


@patch("deepstack_integrations.document_stores.pinecone.document_store.pinecone")
def test_to_dict(mock_pinecone, monkeypatch):
    monkeypatch.setenv("PINECONE_API_KEY", "env-api-key")
    mock_pinecone.Index.return_value.describe_index_stats.return_value = {"dimension": 512}
    document_store = PineconeDocumentStore(
        environment="gcp-starter",
        index="default",
        namespace="test-namespace",
        batch_size=50,
        dimension=512,
    )
    retriever = PineconeEmbeddingRetriever(document_store=document_store)
    res = retriever.to_dict()
    assert res == {
        "type": "deepstack_integrations.components.retrievers.pinecone.embedding_retriever.PineconeEmbeddingRetriever",
        "init_parameters": {
            "document_store": {
                "init_parameters": {
                    "api_key": {
                        "env_vars": [
                            "PINECONE_API_KEY",
                        ],
                        "strict": True,
                        "type": "env_var",
                    },
                    "environment": "gcp-starter",
                    "index": "default",
                    "namespace": "test-namespace",
                    "batch_size": 50,
                    "dimension": 512,
                },
                "type": "deepstack_integrations.document_stores.pinecone.document_store.PineconeDocumentStore",
            },
            "filters": {},
            "top_k": 10,
        },
    }


@patch("deepstack_integrations.document_stores.pinecone.document_store.pinecone")
def test_from_dict(mock_pinecone, monkeypatch):
    data = {
        "type": "deepstack_integrations.components.retrievers.pinecone.embedding_retriever.PineconeEmbeddingRetriever",
        "init_parameters": {
            "document_store": {
                "init_parameters": {
                    "api_key": {
                        "env_vars": [
                            "PINECONE_API_KEY",
                        ],
                        "strict": True,
                        "type": "env_var",
                    },
                    "environment": "gcp-starter",
                    "index": "default",
                    "namespace": "test-namespace",
                    "batch_size": 50,
                    "dimension": 512,
                },
                "type": "deepstack_integrations.document_stores.pinecone.document_store.PineconeDocumentStore",
            },
            "filters": {},
            "top_k": 10,
        },
    }

    mock_pinecone.Index.return_value.describe_index_stats.return_value = {"dimension": 512}
    monkeypatch.setenv("PINECONE_API_KEY", "test-key")
    retriever = PineconeEmbeddingRetriever.from_dict(data)

    document_store = retriever.document_store
    assert document_store.environment == "gcp-starter"
    assert document_store.api_key == Secret.from_env_var("PINECONE_API_KEY", strict=True)
    assert document_store.index == "default"
    assert document_store.namespace == "test-namespace"
    assert document_store.batch_size == 50
    assert document_store.dimension == 512

    assert retriever.filters == {}
    assert retriever.top_k == 10


def test_run():
    mock_store = Mock(spec=PineconeDocumentStore)
    mock_store._embedding_retrieval.return_value = [Document(content="Test doc", embedding=[0.1, 0.2])]
    retriever = PineconeEmbeddingRetriever(document_store=mock_store)
    res = retriever.run(query_embedding=[0.5, 0.7])
    mock_store._embedding_retrieval.assert_called_once_with(
        query_embedding=[0.5, 0.7],
        filters={},
        top_k=10,
    )
    assert len(res) == 1
    assert len(res["documents"]) == 1
    assert res["documents"][0].content == "Test doc"
    assert res["documents"][0].embedding == [0.1, 0.2]
