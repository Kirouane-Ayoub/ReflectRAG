from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from utils.data_models import GradeDocuments
from utils.models import Gemini_llm  # you can use Cohere_llm
from utils.prompts import relevance_system_template

# Output parser
relevance_parser = PydanticOutputParser(pydantic_object=GradeDocuments)


# System prompt

relevance_system_message_prompt = SystemMessagePromptTemplate.from_template(
    relevance_system_template
)

# Human prompt
relevance_human_template = "Retrieved document: \n\n {document} \n\n User question: {question}\n\n{format_instructions}"
relevance_human_message_prompt = HumanMessagePromptTemplate.from_template(
    relevance_human_template
)

# Combine prompts into a chat prompt template
chat_prompt = ChatPromptTemplate.from_messages(
    [relevance_system_message_prompt, relevance_human_message_prompt]
)

# Format instructions for the LLM
retrieval_format_instructions = relevance_parser.get_format_instructions()

# Create a chain to generate and parse the response
retrieval_grader_relevance = chat_prompt | Gemini_llm | relevance_parser
