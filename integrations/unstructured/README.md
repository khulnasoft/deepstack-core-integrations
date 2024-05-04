# unstructured-fileconverter-deepstack

[![PyPI - Version](https://img.shields.io/pypi/v/unstructured-fileconverter-deepstack.svg)](https://pypi.org/project/unstructured-fileconverter-deepstack)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/unstructured-fileconverter-deepstack.svg)](https://pypi.org/project/unstructured-fileconverter-deepstack)

-----

**Table of Contents**

- [unstructured-fileconverter-deepstack](#unstructured-fileconverter-deepstack)
  - [Installation](#installation)
  - [License](#license)
  - [Testing](#testing)

## Installation

```console
pip install unstructured-fileconverter-deepstack
```

## License

`unstructured-fileconverter-deepstack` is distributed under the terms of the [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html) license.

## Testing

To run tests, first start a Docker container running the Unstructured API:

```console
docker run -p 8000:8000 -d --rm --name unstructured-api quay.io/unstructured-io/unstructured-api:latest --port 8000 --host 0.0.0.0
```

Then run tests:

```console
hatch run test
```