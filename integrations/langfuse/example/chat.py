import os

os.environ["DEEPSTACK_CONTENT_TRACING_ENABLED"] = "true"

from deepstack import Pipeline
from deepstack.components.builders import DynamicChatPromptBuilder
from deepstack.components.generators.chat import OpenAIChatGenerator
from deepstack.dataclasses import ChatMessage
from deepstack_integrations.components.connectors.langfuse import LangfuseConnector

if __name__ == "__main__":

    pipe = Pipeline()
    pipe.add_component("tracer", LangfuseConnector("Chat example"))
    pipe.add_component("prompt_builder", DynamicChatPromptBuilder())
    pipe.add_component("llm", OpenAIChatGenerator(model="gpt-3.5-turbo"))

    pipe.connect("prompt_builder.prompt", "llm.messages")

    messages = [
        ChatMessage.from_system("Always respond in German even if some input data is in other languages."),
        ChatMessage.from_user("Tell me about {{location}}"),
    ]

    response = pipe.run(
        data={"prompt_builder": {"template_variables": {"location": "Berlin"}, "prompt_source": messages}}
    )
    print(response["llm"]["replies"][0])
    print(response["tracer"]["trace_url"])
