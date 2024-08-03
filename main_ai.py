import streamlit as st
from dotenv import load_dotenv
import os
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

# load OPEN AI api key
load_dotenv()
key = os.getenv('KEY')

# init OPEN AI with langchain
llm = OpenAI(api_key = key) 

st.title("OPEN AI chat model")

prompt = PromptTemplate(
    input_variables=["question"],
    template="Question: {question}\nAnswer: "
)

chain = LLMChain(llm = llm, prompt = prompt)

user_chat = st.chat_input("Your question...")