from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate

from ai_ocr.azure.openai_ops import get_llm


def get_structured_data(pages: str, prompt: str, json_schema: str, images=[]) -> any:
    messages = [
        ("system",
         prompt
         ),
        ("human", "{input}"),
        ("human", "{schema}"),
    ]

    schema_prompt = """
    The output should be formatted as a JSON instance that conforms to the JSON schema below.

    As an example, for the schema {"properties": {"foo": {"title": "Foo", "description": "a list of strings", "type": "array", "items": {"type": "string"}}}, "required": ["foo"]}
    the object {"foo": ["bar", "baz"]} is a well-formatted instance of the schema. The object {"properties": {"foo": ["bar", "baz"]}} is not well-formatted.

    Here is the output schema:
    ```""" + json_schema + "```"
    prompt = ChatPromptTemplate.from_messages(messages)
    if len(images) > 0:
        prompt.append(HumanMessage("Use these images to verify the ocr information."))
    for img in images:
        print("adding image")
        prompt.append(
            HumanMessage(content=[{"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img}"}}]))
    model = get_llm()
    chain = prompt | model
    return chain.invoke({"input": pages, "schema": schema_prompt})
