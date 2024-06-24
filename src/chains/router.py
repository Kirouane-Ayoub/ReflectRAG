from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from utils.data_models import RouteQuery
from utils.models import Cohere_llm
from utils.prompts import routing_system_template

# Output parser
routing_parser = PydanticOutputParser(pydantic_object=RouteQuery)

routing_system_message_prompt = SystemMessagePromptTemplate.from_template(
    routing_system_template
)

routing_human_template = "{question}\n\n{format_instructions}"
routing_human_message_prompt = HumanMessagePromptTemplate.from_template(
    routing_human_template
)

# Combine prompts and add formatting instructions for structured output
chat_prompt = ChatPromptTemplate.from_messages(
    [routing_system_message_prompt, routing_human_message_prompt]
)

# Format instructions for the LLM
routing_format_instructions = routing_parser.get_format_instructions()

# Create a chain to generate and parse the response
routing_chain = chat_prompt | Cohere_llm | routing_parser
