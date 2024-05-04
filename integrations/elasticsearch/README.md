[![test](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/elasticsearch.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/elasticsearch.yml)

[![PyPI - Version](https://img.shields.io/pypi/v/elasticsearch-deepstack.svg)](https://pypi.org/project/elasticsearch-deepstack)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/elasticsearch-deepstack.svg)](https://pypi.org/project/elasticsearch-deepstack)

# Elasticsearch Document Store

Document Store for Deepstack 2.x, supports ElasticSearch 8.

## Installation

```console
pip install elasticsearch-deepstack
```

## Testing

To run tests first start a Docker container running ElasticSearch. We provide a utility `docker-compose.yml` for that:

```console
docker-compose up
```

Then run tests:

```console
hatch run test
```

## License

`elasticsearch-deepstack` is distributed under the terms of the [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html) license.
