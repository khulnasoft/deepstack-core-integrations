# amazon-sagemaker-deepstack

[![PyPI - Version](https://img.shields.io/pypi/v/amazon-sagemaker-deepstack.svg)](https://pypi.org/project/amazon-sagemaker-deepstack)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/amazon-sagemaker-deepstack.svg)](https://pypi.org/project/amazon-sagemaker-deepstack)

-----

**Table of Contents**

- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## Installation

```console
pip install amazon-sagemaker-deepstack
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

> Note: You need to export your AWS credentials for Sagemaker integration tests to run (`AWS_ACCESS_KEY_ID` and 
`AWS_SECRET_SECRET_KEY`). If those are missing, the integration tests will be skipped.

To only run unit tests:
```
hatch run test -m "not integration"
```

To only run integration tests:
```
hatch run test -m "integration"
```

To run the linters `ruff` and `mypy`:
```
hatch run lint:all
```

## License

`amazon-sagemaker-deepstack` is distributed under the terms of the [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html) license.
