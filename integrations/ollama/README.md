# ollama-deepstack

[![PyPI - Version](https://img.shields.io/pypi/v/ollama-deepstack.svg)](https://pypi.org/project/ollama-deepstack)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ollama-deepstack.svg)](https://pypi.org/project/ollama-deepstack)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install ollama-deepstack
```

## License

`ollama-deepstack` is distributed under the terms of the [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html) license.

## Testing

To run tests first start a Docker container running Ollama and pull a model for integration testing
It's recommended to use the smallest model possible for testing purposes - see https://ollama.ai/library for a list that Ollama supportd

```console
docker run -d -p 11434:11434 --name ollama ollama/ollama:latest
docker exec ollama ollama pull <your model here>
```

Then run tests:

```console
hatch run test
```

The default model used here is ``orca-mini``