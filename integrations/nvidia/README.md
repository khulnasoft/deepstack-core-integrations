# nvidia-deepstack

[![PyPI - Version](https://img.shields.io/pypi/v/nvidia-deepstack.svg)](https://pypi.org/project/nvidia-deepstack)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/nvidia-deepstack.svg)](https://pypi.org/project/nvidia-deepstack)

---

**Table of Contents**

- [nvidia-deepstack](#nvidia-deepstack)
  - [Installation](#installation)
  - [Contributing](#contributing)
  - [License](#license)

## Installation

```console
pip install nvidia-deepstack
```

## Contributing

`hatch` is the best way to interact with this project, to install it:

```sh
pip install hatch
```

With `hatch` installed, to run all the tests:

```
hatch run test
```

> Note: integration tests will be skipped unless the env var NVIDIA_API_KEY is set. The api key needs to be valid
> in order to pass the tests.

To only run unit tests:

```
hatch run test -m"not integration"
```

To run the linters `ruff` and `mypy`:

```
hatch run lint:all
```

## License

`nvidia-deepstack` is distributed under the terms of the [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html) license.
