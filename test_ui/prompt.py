from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from ai_ocr.azure.openai_ops import get_llm

messages = [
    ("system",
     "You are assistant that creates a JSON schema from the input. Only reply with JSON Schema"
     ),
    ("human", "{input}"),
]


def create_schema(instruction: str):
    prompt = ChatPromptTemplate.from_messages(messages)
    model = get_llm()
    chain = prompt | model
    return chain.invoke({"input": instruction}).content
