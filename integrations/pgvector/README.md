# pgvector-deepstack

[![PyPI - Version](https://img.shields.io/pypi/v/pgvector-deepstack.svg)](https://pypi.org/project/pgvector-deepstack)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pgvector-deepstack.svg)](https://pypi.org/project/pgvector-deepstack)

---

**Table of Contents**

- [pgvector-deepstack](#pgvector-deepstack)
  - [Installation](#installation)
  - [Testing](#testing)
  - [License](#license)

## Installation

```console
pip install pgvector-deepstack
```

## Testing

Ensure that you have a PostgreSQL running with the `pgvector` extension. For a quick setup using Docker, run:
```
docker run -d -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres ankane/pgvector
```

then run the tests:

```console
hatch run test
```

To run the coverage report:

```console
hatch run cov
```

## License

`pgvector-deepstack` is distributed under the terms of the [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html) license.
