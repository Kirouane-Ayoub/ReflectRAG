import utils.settings as settings
from dotenv import load_dotenv
from langchain_cohere import CohereEmbeddings
from langchain_community.llms import Cohere
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

Cohere_llm = Cohere(model=settings.COHERE_LLM_MODEL)
Cohere_embeddings = CohereEmbeddings(model=settings.COHERE_EMBEDDING_MODEL)

Gemini_llm = ChatGoogleGenerativeAI(model=settings.GEMINI_LLM_MODEL)
