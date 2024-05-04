# mongodb-atlas-deepstack

[![PyPI - Version](https://img.shields.io/pypi/v/mongodb-atlas-deepstack.svg)](https://pypi.org/project/mongodb-atlas-deepstack)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mongodb-atlas-deepstack.svg)](https://pypi.org/project/mongodb-atlas-deepstack)

-----

**Table of Contents**

- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## Installation

```console
pip install mongodb-atlas-deepstack
```

## Contributing

`hatch` is the best way to interact with this project, to install it:
```sh
pip install hatch
```

To run the linters `ruff` and `mypy`:
```
hatch run lint:all
```

To run all the tests:
```
hatch run test
```

Note: you need your own MongoDB Atlas account to run the tests: you can make one here: 
https://www.mongodb.com/cloud/atlas/register. Once you have it, export the connection string
to the env var `MONGO_CONNECTION_STRING`. If you forget to do so, all the tests will be skipped.

## License

`mongodb-atlas-deepstack` is distributed under the terms of the [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html) license.
