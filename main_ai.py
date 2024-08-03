import streamlit as st
from dotenv import load_dotenv
import os
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain_core.messages import HumanMessage, AIMessage

# load OPEN AI api key
load_dotenv()
key = os.getenv('KEY')

# init OPEN AI with langchain
llm = OpenAI(api_key = key) 

# chat history - logging our messages
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# template how communication should look
prompt = PromptTemplate(
    input_variables=["question"],
    template="Question: {question}\nAnswer: "
)

# answer the question in style of our prompt-template (from understand question to give answer)
# LLMChain is like workgroup 
chain = LLMChain(llm = llm, prompt = prompt)

# FRONTEND - title
st.title("OPEN AI chat model")

# input line
user_message = st.chat_input("Your question...")

# showing conversation
for message in st.session_state.chat_history:
    # checking the type of message
    if isinstance(message, HumanMessage):
        with st.chat_message("User"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.markdown(message.content)

if user_message is not None and user_message != "":
    st.session_state.chat_history.append(HumanMessage(user_message))

    with st.chat_message("User"):
        # formated output
        st.markdown(user_message)

    with st.chat_message("AI"):
        ai_answer = chain.run(question = user_message)
        st.markdown(ai_answer)

    st.session_state.chat_history.append(AIMessage(ai_answer))