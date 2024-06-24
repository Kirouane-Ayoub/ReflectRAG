from graph.workflow import (
    GraphState,
    decide_to_generate,
    generate,
    grade_documents,
    grade_generation_v_documents_and_question,
    retrieve,
    route_question,
    web_search,
)
from langgraph.graph import END, StateGraph

workflow = StateGraph(GraphState)

# Define the nodes
workflow.add_node("websearch", web_search)  # web search # key: action to do
workflow.add_node("retrieve", retrieve)  # retrieve
workflow.add_node("grade_documents", grade_documents)  # grade documents
workflow.add_node("generate", generate)  # generatae

workflow.add_edge("websearch", "generate")  # start -> end of node
workflow.add_edge("retrieve", "grade_documents")

# Build graph
workflow.set_conditional_entry_point(
    route_question,
    {
        "websearch": "websearch",
        "vectorstore": "retrieve",
    },
)

workflow.add_conditional_edges(
    "grade_documents",  # start: node
    decide_to_generate,  # defined function
    {
        "websearch": "websearch",  # returns of the function
        "generate": "generate",  # returns of the function
    },
)
workflow.add_conditional_edges(
    "generate",  # start: node
    grade_generation_v_documents_and_question,  # defined function
    {
        "not supported": "generate",  # returns of the function
        "useful": END,  # returns of the function
        "not useful": "websearch",  # returns of the function
    },
)

# Compile
app = workflow.compile()
