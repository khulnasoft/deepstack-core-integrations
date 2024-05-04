# fastembed-deepstack

[![PyPI - Version](https://img.shields.io/pypi/v/fastembed-deepstack.svg)](https://pypi.org/project/fastembed-deepstack)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fastembed-deepstack.svg)](https://pypi.org/project/fastembed-deepstack)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install fastembed-deepstack
```

## Usage

You can use `FastembedTextEmbedder` and `FastembedDocumentEmbedder` by importing as:

```python
from deepstack_integrations.components.embedders.fastembed import FastembedTextEmbedder

text = "fastembed is supported by and maintained by Qdrant."
text_embedder = FastembedTextEmbedder(
    model="BAAI/bge-small-en-v1.5"
)
text_embedder.warm_up()
embedding = text_embedder.run(text)["embedding"]
```

```python
from deepstack_integrations.components.embedders.fastembed import FastembedDocumentEmbedder
from deepstack.dataclasses import Document

embedder = FastembedDocumentEmbedder(
    model="BAAI/bge-small-en-v1.5",
)
embedder.warm_up()
doc = Document(content="fastembed is supported by and maintained by Qdrant.", meta={"long_answer": "no",})
result = embedder.run(documents=[doc])
```

You can use `FastembedSparseTextEmbedder` and `FastembedSparseDocumentEmbedder` by importing as:

```python
from deepstack_integrations.components.embedders.fastembed import FastembedSparseTextEmbedder

text = "fastembed is supported by and maintained by Qdrant."
text_embedder = FastembedSparseTextEmbedder(
    model="prithvida/Splade_PP_en_v1"
)
text_embedder.warm_up()
embedding = text_embedder.run(text)["embedding"]
```

```python
from deepstack_integrations.components.embedders.fastembed import FastembedSparseDocumentEmbedder
from deepstack.dataclasses import Document

embedder = FastembedSparseDocumentEmbedder(
    model="prithvida/Splade_PP_en_v1",
)
embedder.warm_up()
doc = Document(content="fastembed is supported by and maintained by Qdrant.", meta={"long_answer": "no",})
result = embedder.run(documents=[doc])
```

## License

`fastembed-deepstack` is distributed under the terms of the [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html) license.
