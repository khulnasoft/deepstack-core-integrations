# To run this example, you will need to set a `ANTHROPIC_API_KEY` environment variable.

from deepstack import Pipeline
from deepstack.components.builders import DynamicChatPromptBuilder
from deepstack.components.converters import HTMLToDocument
from deepstack.components.fetchers import LinkContentFetcher
from deepstack.components.generators.utils import print_streaming_chunk
from deepstack.dataclasses import ChatMessage
from deepstack.utils import Secret

from deepstack_integrations.components.generators.anthropic import AnthropicChatGenerator

messages = [
    ChatMessage.from_system("You are a prompt expert who answers questions based on the given documents."),
    ChatMessage.from_user("Here are the documents: {{documents}} \\n Answer: {{query}}"),
]

rag_pipeline = Pipeline()
rag_pipeline.add_component("fetcher", LinkContentFetcher())
rag_pipeline.add_component("converter", HTMLToDocument())
rag_pipeline.add_component("prompt_builder", DynamicChatPromptBuilder(runtime_variables=["documents"]))
rag_pipeline.add_component(
    "llm",
    AnthropicChatGenerator(
        api_key=Secret.from_env_var("ANTHROPIC_API_KEY"),
        model="claude-3-sonnet-20240229",
        streaming_callback=print_streaming_chunk,
    ),
)


rag_pipeline.connect("fetcher", "converter")
rag_pipeline.connect("converter", "prompt_builder")
rag_pipeline.connect("prompt_builder", "llm")

question = "What are the best practices in prompt engineering?"
rag_pipeline.run(
    data={
        "fetcher": {"urls": ["https://docs.anthropic.com/claude/docs/prompt-engineering"]},
        "prompt_builder": {"template_variables": {"query": question}, "prompt_source": messages},
    }
)
