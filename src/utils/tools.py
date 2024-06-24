from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.tools import DuckDuckGoSearchRun
from utils.models import Cohere_embeddings


def text_to_vec(embeddings, chunk_size=1200, chunk_overlap=200):
    loader = PyPDFDirectoryLoader("src/data_input")
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    chunks = text_splitter.split_documents(docs)
    db = Chroma.from_documents(chunks, embeddings)
    return db.as_retriever()


retriever = text_to_vec(Cohere_embeddings)
duckduckgo_search = DuckDuckGoSearchRun()
