routing_system_template = """You are an expert at routing a user question to a vectorstore or websearch.
The vectorstore contains documents related to Retrieval-augmented generation (RAG).
Use the vectorstore for questions on these topics. For all else, use websearch."""

relevance_system_template = """You are a grader assessing relevance of a retrieved document to a user question.
If the document contains keyword(s) or semantic meaning related to the question, grade it as relevant.
Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."""

grader_system_template = """You are a grader assessing whether an LLM generation is supported by a set of retrieved facts.
Restrict yourself to give a binary score, either 'yes' or 'no'. If the answer is supported or partially supported by the set of facts, consider it a yes.
Don't consider calling external APIs for additional information as consistent with the facts."""

answer_grader_system_template = """You are a grader assessing whether an answer addresses / resolves a question.
Give a binary score 'yes' or 'no'. 'Yes' means that the answer resolves the question."""
