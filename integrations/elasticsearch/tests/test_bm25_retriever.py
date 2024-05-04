# SPDX-FileCopyrightText: 2023-present khulnasoft GmbH <info@khulnasoft.com>
#
# SPDX-License-Identifier: Apache-2.0
from unittest.mock import Mock, patch

from deepstack.dataclasses import Document
from deepstack_integrations.components.retrievers.elasticsearch import ElasticsearchBM25Retriever
from deepstack_integrations.document_stores.elasticsearch import ElasticsearchDocumentStore


def test_init_default():
    mock_store = Mock(spec=ElasticsearchDocumentStore)
    retriever = ElasticsearchBM25Retriever(document_store=mock_store)
    assert retriever._document_store == mock_store
    assert retriever._filters == {}
    assert retriever._top_k == 10
    assert not retriever._scale_score


@patch("deepstack_integrations.document_stores.elasticsearch.document_store.Elasticsearch")
def test_to_dict(_mock_elasticsearch_client):
    document_store = ElasticsearchDocumentStore(hosts="some fake host")
    retriever = ElasticsearchBM25Retriever(document_store=document_store)
    res = retriever.to_dict()
    assert res == {
        "type": "deepstack_integrations.components.retrievers.elasticsearch.bm25_retriever.ElasticsearchBM25Retriever",
        "init_parameters": {
            "document_store": {
                "init_parameters": {
                    "hosts": "some fake host",
                    "index": "default",
                    "embedding_similarity_function": "cosine",
                },
                "type": "deepstack_integrations.document_stores.elasticsearch.document_store.ElasticsearchDocumentStore",
            },
            "filters": {},
            "fuzziness": "AUTO",
            "top_k": 10,
            "scale_score": False,
        },
    }


@patch("deepstack_integrations.document_stores.elasticsearch.document_store.Elasticsearch")
def test_from_dict(_mock_elasticsearch_client):
    data = {
        "type": "deepstack_integrations.components.retrievers.elasticsearch.bm25_retriever.ElasticsearchBM25Retriever",
        "init_parameters": {
            "document_store": {
                "init_parameters": {"hosts": "some fake host", "index": "default"},
                "type": "deepstack_integrations.document_stores.elasticsearch.document_store.ElasticsearchDocumentStore",
            },
            "filters": {},
            "fuzziness": "AUTO",
            "top_k": 10,
            "scale_score": True,
        },
    }
    retriever = ElasticsearchBM25Retriever.from_dict(data)
    assert retriever._document_store
    assert retriever._filters == {}
    assert retriever._fuzziness == "AUTO"
    assert retriever._top_k == 10
    assert retriever._scale_score


def test_run():
    mock_store = Mock(spec=ElasticsearchDocumentStore)
    mock_store._bm25_retrieval.return_value = [Document(content="Test doc")]
    retriever = ElasticsearchBM25Retriever(document_store=mock_store)
    res = retriever.run(query="some query")
    mock_store._bm25_retrieval.assert_called_once_with(
        query="some query",
        filters={},
        fuzziness="AUTO",
        top_k=10,
        scale_score=False,
    )
    assert len(res) == 1
    assert len(res["documents"]) == 1
    assert res["documents"][0].content == "Test doc"