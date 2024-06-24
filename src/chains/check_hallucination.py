from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from utils.data_models import GradeHallucinations
from utils.models import Gemini_llm  # you can use Cohere_llm
from utils.prompts import grader_system_template

# Output parser
grader_parser = PydanticOutputParser(pydantic_object=GradeHallucinations)


grader_system_message_prompt = SystemMessagePromptTemplate.from_template(
    grader_system_template
)

# Human prompt
grader_human_template = "Set of facts: \n\n {documents} \n\n LLM generation: {generation}\n\n{format_instructions}"
grader_human_message_prompt = HumanMessagePromptTemplate.from_template(
    grader_human_template
)

# Combine prompts into a chat prompt template
grader_chat_prompt = ChatPromptTemplate.from_messages(
    [grader_system_message_prompt, grader_human_message_prompt]
)

# Format instructions for the LLM
grader_format_instructions = grader_parser.get_format_instructions()

# Create a chain to generate and parse the response
hallucination_grader = grader_chat_prompt | Gemini_llm | grader_parser
