[![test](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/opensearch.yml/badge.svg)](https://github.com/khulnasoft/deepstack-core-integrations/actions/workflows/opensearch.yml)

[![PyPI - Version](https://img.shields.io/pypi/v/opensearch-deepstack.svg)](https://pypi.org/project/opensearch-deepstack)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/opensearch-deepstack.svg)](https://pypi.org/project/opensearch-deepstack)

# OpenSearch Document Store

Document Store for Deepstack 2.x, supports OpenSearch.

## Installation

```console
pip install opensearch-deepstack
```

## Testing

To run tests first start a Docker container running OpenSearch. We provide a utility `docker-compose.yml` for that:

```console
docker-compose up
```

Then run tests:

```console
hatch run test
```

## License

`opensearch-deepstack` is distributed under the terms of the [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html) license.
