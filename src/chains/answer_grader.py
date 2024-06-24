from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from utils.data_models import GradeAnswer
from utils.models import Cohere_llm
from utils.prompts import answer_grader_system_template

# Output parser
answer_grader_parser = PydanticOutputParser(pydantic_object=GradeAnswer)

answer_grader_system_message_prompt = SystemMessagePromptTemplate.from_template(
    answer_grader_system_template
)

# Human prompt
answer_grader_human_template = "User question: \n\n {question} \n\n LLM generation: {generation}\n\n{format_instructions}"
answer_grader_human_message_prompt = HumanMessagePromptTemplate.from_template(
    answer_grader_human_template
)

# Combine prompts into a chat prompt template
chat_prompt = ChatPromptTemplate.from_messages(
    [answer_grader_system_message_prompt, answer_grader_human_message_prompt]
)

# Format instructions for the LLM
answer_format_instructions = answer_grader_parser.get_format_instructions()

# Create a chain to generate and parse the response
answer_grader = chat_prompt | Cohere_llm | answer_grader_parser
