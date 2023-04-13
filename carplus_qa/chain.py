import pickle, pinecone, os
from pathlib import Path

from langchain.chains.base import Chain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings

DIR_PATH = Path(__file__).parent

embeddings = OpenAIEmbeddings()

pinecone.init(
    api_key=os.environ["PINECONE_API_KEY"],
    environment=os.environ["PINECONE_ENVIRONMENT"],
)

index_name = 'carplus-text-embedding-ada-002'

docsearch = Pinecone.from_existing_index(index_name=index_name,embedding=embeddings,namespace='company_documents')

def get_chain() -> Chain:
    """Load your chain here."""
    template = """You are a chatbot assistant answering Q&A questions about 格上租車, a ride-sharing company in Taiwan.
    You are given the following extracted parts of a long document and a question. Provide a conversational answer.
    If you don't know the answer, simply reply with:'我不知道怎麼回答這個問題'. Don't try to make up an answer.
    If the question is not about 格上租車, politely inform them that you are tuned to only answer questions about 格上租車 and services that it provides.
    Question: {question}
    =========
    {context}
    =========
    Answer in Markdown:"""
    QA_PROMPT = PromptTemplate(template=template, input_variables=["question", "context"])


    chain_type_kwargs = {"prompt": QA_PROMPT}
    qa = RetrievalQA.from_chain_type(llm=ChatOpenAI(model_name='gpt-3.5-turbo',temperature=0,max_tokens=2000), chain_type="stuff", retriever=docsearch.as_retriever(), chain_type_kwargs=chain_type_kwargs)
    return qa
