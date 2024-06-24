from typing import Literal

from langchain_core.pydantic_v1 import BaseModel, Field


class GradeAnswer(BaseModel):
    """Binary score to assess if the answer addresses the question."""

    binary_score: Literal["yes", "no"] = Field(
        description="Answer addresses the question, 'yes' or 'no'"
    )


class GradeHallucinations(BaseModel):
    """Binary score for hallucination present in generation answer."""

    binary_score: Literal["yes", "no"] = Field(
        ...,
        description="Don't consider calling external APIs for additional information. Answer is supported by the facts, 'yes' or 'no'.",
    )


class GradeDocuments(BaseModel):
    """Binary score for relevance check on retrieved documents."""

    binary_score: Literal["yes", "no"] = Field(
        description="Documents are relevant to the question, 'yes' or 'no'"
    )


class RouteQuery(BaseModel):
    """Route a user query to the most relevant datasource."""

    datasource: Literal["vectorstore", "websearch"] = Field(
        ...,
        description="Given a user question choose to route it to web search or a vectorstore.",
    )
