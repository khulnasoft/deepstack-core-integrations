# In order to run this example, you will need to have an instance of Ollama running with the
# orca-mini model downloaded. We suggest you use the following commands to serve an orca-mini
# model from Ollama
#
# docker run -d -p 11434:11434 --name ollama ollama/ollama:latest
# docker exec ollama ollama pull orca-mini

from deepstack import Document, Pipeline
from deepstack.components.builders.prompt_builder import PromptBuilder
from deepstack.components.retrievers import InMemoryBM25Retriever
from deepstack.document_stores.in_memory import InMemoryDocumentStore
from deepstack_integrations.components.generators.ollama import OllamaGenerator

document_store = InMemoryDocumentStore()
document_store.write_documents(
    [
        Document(content="Super Mario was an important politician"),
        Document(content="Mario owns several castles and uses them to conduct important political business"),
        Document(
            content="Super Mario was a successful military leader who fought off several invasion attempts by "
            "his arch rival - Bowser"
        ),
    ]
)

query = "Who is Super Mario?"

template = """
Given only the following information, answer the question.
Ignore your own knowledge.

Context:
{% for document in documents %}
    {{ document.content }}
{% endfor %}

Question: {{ query }}?
"""
pipe = Pipeline()

pipe.add_component("retriever", InMemoryBM25Retriever(document_store=document_store))
pipe.add_component("prompt_builder", PromptBuilder(template=template))
pipe.add_component("llm", OllamaGenerator(model="orca-mini"))
pipe.connect("retriever", "prompt_builder.documents")
pipe.connect("prompt_builder", "llm")

response = pipe.run({"prompt_builder": {"query": query}, "retriever": {"query": query}})

print(response["llm"]["replies"])
# An expected response - the output is not deterministic:
# ['Based on the information provided, Super Mario is a successful military leader who fought
# off several invasion attempts by his arch rival - Bowser. He is also an important politician and owns several
# castles where he conducts political business. ' 'Therefore, it can be inferred that Super Mario is a combination of
# both a military leader and an important politician.']
