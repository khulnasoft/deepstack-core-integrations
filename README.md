# Deepstack 2.x Core Integrations

This repository contains integrations to extend the capabilities of [Deepstack](https://github.com/khulnasoft/deepstack) version 2.0 and
onwards. The code in this repo is maintained by [khulnasoft](https://www.khulnasoft.com), see each integration's `README` file for details around installation, usage and support.

## Quick start

You will need `hatch` to work on or create new integrations, open [this link](https://hatch.pypa.io/latest/install/#installation)
and follow the install instructions for your operating system and platform.

All the integrations are self contained, so the first step before working on one is to `cd` into the proper folder.
For example, to run the tests suite for the Chroma document store, from the root of the repo:

```sh
$ cd integrations/chroma
$ hatch run test
```

Hatch will take care of setting up an isolated Python environment and run the tests.

Please check out our [Contribution Guidelines](CONTRIBUTING.md) for all the details.

## Inventory

| Package                                                                                                        | Type                | PyPi Package                                                                                                                                             | Status                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [amazon-bedrock-deepstack](integrations/amazon-bedrock/)                                                        | Generator           | [![PyPI - Version](https://img.shields.io/pypi/v/amazon-bedrock-deepstack.svg)](https://pypi.org/project/amazon-bedrock-deepstack)                         | [![Test / amazon_bedrock](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/amazon_bedrock.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/amazon_bedrock.yml)                   |
| [amazon-sagemaker-deepstack](integrations/amazon_sagemaker/)                                                    | Generator           | [![PyPI - Version](https://img.shields.io/pypi/v/amazon-sagemaker-deepstack.svg)](https://pypi.org/project/amazon-sagemaker-deepstack)                     | [![Test / amazon_sagemaker](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/amazon_sagemaker.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/amazon_sagemaker.yml)             |
| [anthropic-deepstack](integrations/anthropic/)                                                                  | Generator           | [![PyPI - Version](https://img.shields.io/pypi/v/anthropic-deepstack.svg)](https://pypi.org/project/anthropic-deepstack)                                   | [![Test / anthropic](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/anthropic.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/anthropic.yml)                                  |
| [astra-deepstack](integrations/astra/)                                                                          | Document Store      | [![PyPI - Version](https://img.shields.io/pypi/v/astra-deepstack.svg)](https://pypi.org/project/astra-deepstack)                                           | [![Test / astra](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/astra.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/astra.yml)                                              |
| [chroma-deepstack](integrations/chroma/)                                                                        | Document Store      | [![PyPI - Version](https://img.shields.io/pypi/v/chroma-deepstack.svg)](https://pypi.org/project/chroma-deepstack)                                         | [![Test / chroma](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/chroma.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/chroma.yml)                                           |
| [cohere-deepstack](integrations/cohere/)                                                                        | Embedder, Generator, Ranker | [![PyPI - Version](https://img.shields.io/pypi/v/cohere-deepstack.svg)](https://pypi.org/project/cohere-deepstack)                                         | [![Test / cohere](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/cohere.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/cohere.yml)                                           |
| [deepeval-deepstack](integrations/deepeval/)                                                                    | Evaluator           | [![PyPI - Version](https://img.shields.io/pypi/v/deepeval-deepstack.svg)](https://pypi.org/project/deepeval-deepstack)                                     | [![Test / deepeval](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/deepeval.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/deepeval.yml)                                     |
| [elasticsearch-deepstack](integrations/elasticsearch/)                                                          | Document Store      | [![PyPI - Version](https://img.shields.io/pypi/v/elasticsearch-deepstack.svg)](https://pypi.org/project/elasticsearch-deepstack)                           | [![Test / elasticsearch](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/elasticsearch.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/elasticsearch.yml)                      |
| [fastembed-deepstack](integrations/fastembed/)                                                                  | Embedder            | [![PyPI - Version](https://img.shields.io/pypi/v/fastembed-deepstack.svg)](https://pypi.org/project/fastembed-deepstack/)                                  | [![Test / fastembed](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/fastembed.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/fastembed.yml)                                  |
| [google-ai-deepstack](integrations/google_ai/)                                                                  | Generator           | [![PyPI - Version](https://img.shields.io/pypi/v/google-ai-deepstack.svg)](https://pypi.org/project/google-ai-deepstack)                                   | [![Test / google-ai](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/google_ai.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/google_ai.yml)                                  |
| [google-vertex-deepstack](integrations/google_vertex/)                                                          | Generator           | [![PyPI - Version](https://img.shields.io/pypi/v/google-vertex-deepstack.svg)](https://pypi.org/project/google-vertex-deepstack)                           | [![Test / google-vertex](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/google_vertex.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/google_vertex.yml)                      |
| [gradient-deepstack](integrations/gradient/)                                                                    | Embedder, Generator | [![PyPI - Version](https://img.shields.io/pypi/v/gradient-deepstack.svg)](https://pypi.org/project/gradient-deepstack)                                     | [![Test / gradient](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/gradient.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/gradient.yml)                                     |
| [instructor-embedders-deepstack](integrations/instructor_embedders/)                                            | Embedder            | [![PyPI - Version](https://img.shields.io/pypi/v/instructor-embedders-deepstack.svg)](https://pypi.org/project/instructor-embedders-deepstack)             | [![Test / instructor-embedders](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/instructor_embedders.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/instructor_embedders.yml) |
| [jina-deepstack](integrations/jina/)                                                                            | Embedder, Ranker    | [![PyPI - Version](https://img.shields.io/pypi/v/jina-deepstack.svg)](https://pypi.org/project/jina-deepstack)                                             | [![Test / jina](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/jina.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/jina.yml)                                                 |
| [langfuse-deepstack](integrations/langfuse/)                                                                    | Tracer              | [![PyPI - Version](https://img.shields.io/pypi/v/langfuse-deepstack.svg?color=orange)](https://pypi.org/project/langfuse-deepstack)                        | [![Test / langfuse](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/langfuse.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/langfuse.yml)                                     |
| [llama-cpp-deepstack](integrations/llama_cpp/)                                                                  | Generator           | [![PyPI - Version](https://img.shields.io/pypi/v/llama-cpp-deepstack.svg?color=orange)](https://pypi.org/project/llama-cpp-deepstack)                      | [![Test / llama-cpp](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/llama_cpp.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/llama_cpp.yml)                                  |
| [mistral-deepstack](integrations/mistral/)                                                                      | Embedder, Generator | [![PyPI - Version](https://img.shields.io/pypi/v/mistral-deepstack.svg)](https://pypi.org/project/mistral-deepstack)                                       | [![Test / mistral](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/mistral.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/mistral.yml)                                        |
| [mongodb-atlas-deepstack](integrations/mongodb_atlas/)                                                          | Document Store      | [![PyPI - Version](https://img.shields.io/pypi/v/mongodb-atlas-deepstack.svg?color=orange)](https://pypi.org/project/mongodb-atlas-deepstack)              | [![Test / mongodb-atlas](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/mongodb_atlas.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/mongodb_atlas.yml)                      |
| [nvidia-deepstack](integrations/nvidia/)                                                                        | Generator           | [![PyPI - Version](https://img.shields.io/pypi/v/nvidia-deepstack.svg?color=orange)](https://pypi.org/project/nvidia-deepstack)                            | [![Test / nvidia](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/nvidia.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/nvidia.yml)                                           |
| [ollama-deepstack](integrations/ollama/)                                                                        | Generator           | [![PyPI - Version](https://img.shields.io/pypi/v/ollama-deepstack.svg?color=orange)](https://pypi.org/project/ollama-deepstack)                            | [![Test / ollama](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/ollama.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/ollama.yml)                                           |
| [opensearch-deepstack](integrations/opensearch/)                                                                | Document Store      | [![PyPI - Version](https://img.shields.io/pypi/v/opensearch-deepstack.svg)](https://pypi.org/project/opensearch-deepstack)                                 | [![Test / opensearch](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/opensearch.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/opensearch.yml)                               |
| [optimum-deepstack](integrations/optimum/)                                                                      | Embedder            | [![PyPI - Version](https://img.shields.io/pypi/v/optimum-deepstack.svg)](https://pypi.org/project/optimum-deepstack)                                       | [![Test / optimum](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/optimum.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/optimum.yml)                                        |
| [pinecone-deepstack](integrations/pinecone/)                                                                    | Document Store      | [![PyPI - Version](https://img.shields.io/pypi/v/pinecone-deepstack.svg?color=orange)](https://pypi.org/project/pinecone-deepstack)                        | [![Test / pinecone](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/pinecone.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/pinecone.yml)                                     |
| [pgvector-deepstack](integrations/pgvector/)                                                                    | Document Store      | [![PyPI - Version](https://img.shields.io/pypi/v/pgvector-deepstack.svg?color=orange)](https://pypi.org/project/pgvector-deepstack)                        | [![Test / pgvector](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/pgvector.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/pgvector.yml)                                     |
| [qdrant-deepstack](integrations/qdrant/)                                                                        | Document Store      | [![PyPI - Version](https://img.shields.io/pypi/v/qdrant-deepstack.svg?color=orange)](https://pypi.org/project/qdrant-deepstack)                            | [![Test / qdrant](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/qdrant.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/qdrant.yml)                                           |
| [ragas-deepstack](integrations/ragas/)                                                                          | Evaluator           | [![PyPI - Version](https://img.shields.io/pypi/v/ragas-deepstack.svg)](https://pypi.org/project/ragas-deepstack)                                           | [![Test / ragas](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/ragas.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/ragas.yml)                                              |
| [unstructured-fileconverter-deepstack](integrations/unstructured/)                                              | File converter      | [![PyPI - Version](https://img.shields.io/pypi/v/unstructured-fileconverter-deepstack.svg)](https://pypi.org/project/unstructured-fileconverter-deepstack) | [![Test / unstructured](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/unstructured.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/unstructured.yml)                         |
| [uptrain-deepstack](https://github.com/khulnasoft/deepstack-core-integrations/tree/staging/integrations/uptrain) | Evaluator           | [![PyPI - Version](https://img.shields.io/pypi/v/uptrain-deepstack.svg)](https://pypi.org/project/uptrain-deepstack)                                       | Staged                                                                                                                                                                                                                                               |
| [weaviate-deepstack](integrations/weaviate/)                                                                    | Document Store      | [![PyPI - Version](https://img.shields.io/pypi/v/weaviate-deepstack.svg)](https://pypi.org/project/weaviate-deepstack)                                     | [![Test / weaviate](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/weaviate.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/weaviate.yml)                                     |
