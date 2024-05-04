# anthropic-deepstack

[![PyPI - Version](https://img.shields.io/pypi/v/anthropic-deepstack.svg)](https://pypi.org/project/anthropic-deepstack)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/anthropic-deepstack.svg)](https://pypi.org/project/anthropic-deepstack)

-----

**Table of Contents**

- [Installation](#installation)
- [Contributing](#contributing)
- [Examples](#examples)
- [License](#license)

## Installation

```console
pip install anthropic-deepstack
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
> Note: there are no integration tests for this project.

To run the linters `ruff` and `mypy`:
```
hatch run lint:all
```

## Examples
You can find an example of how to do a simple RAG with Claude using online documentation in the `example/` folder of this repo.

## License

`anthropic-deepstack` is distributed under the terms of the [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html) license.
