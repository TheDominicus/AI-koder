import streamlit as st
from dotenv import load_dotenv
import os
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain_core.messages import HumanMessage, AIMessage

def init_ai():
    # load OPEN AI api key
    load_dotenv()
    key = os.getenv('KEY')

<<<<<<< Updated upstream
    # init OPEN AI with langchain
    llm = OpenAI(api_key=key)

    # template how communication should look
    prompt = PromptTemplate(
        input_variables=["question"],
        template="Question: {question}\nAnswer: "
    )
    # answer the question in style of our prompt-template (from understand question to give answer)
    # LLMChain is like workgroup
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain

def history(user_message, chain):
    if user_message:
        # user's input to history
        st.session_state.chat_history.append(HumanMessage(user_message))

        # ai's respond and put to history
        ai_answer = chain.run(question = user_message)
        st.session_state.chat_history.append(AIMessage(ai_answer))
        return ai_answer
    return None

def display_chat():
    # showing conversation
    for message in st.session_state.chat_history:
        # checking the type of message
        if isinstance(message, HumanMessage):
            with st.chat_message("User"):
                st.markdown(message.content)
        elif isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.markdown(message.content)
=======
<<<<<<< Updated upstream
# init OPEN AI with langchain
llm = OpenAI(api_key = key) 
=======
    # init OPEN AI with langchain
    llm = OpenAI(api_key=key)
>>>>>>> Stashed changes

    # template how communication should look
    prompt = PromptTemplate(
        input_variables=["question"],
        template="Question: {question}\nAnswer: "
    )

<<<<<<< Updated upstream
chain = init_ai()
=======
    # answer the question in style of our prompt-template (from understand question to give answer)
    # LLMChain is like workgroup
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain

# function, that appends user message and AI answer to history list
def history(user_message, chain):
    if user_message:
        # user's input to history
        st.session_state.chat_history.append(HumanMessage(user_message))

        # ai's respond and put to history
        ai_answer = chain.run(question = user_message)
        st.session_state.chat_history.append(AIMessage(ai_answer))
        return ai_answer
    return None

def display_chat():
    # showing conversation
    for message in st.session_state.chat_history:
        # checking the type of message
        if isinstance(message, HumanMessage):
            with st.chat_message("User"):
                st.markdown(message.content)
        elif isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.markdown(message.content)
>>>>>>> Stashed changes

def main():
    # chat history - logging our messages
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

<<<<<<< Updated upstream
# template how communication should look
prompt = PromptTemplate(
    input_variables=["question"],
    template="Question: {question}\nAnswer: "
)
>>>>>>> Stashed changes

st.title("OPEN AI chat model")
=======
    chain = init_ai()

    st.title("OPEN AI chat model")
>>>>>>> Stashed changes

<<<<<<< Updated upstream
display_chat()
=======
    # input line
    user_message = st.chat_input("Your question...")

<<<<<<< Updated upstream
# showing conversation
for message in st.session_state.chat_history:
    # checking the type of message
    if isinstance(message, HumanMessage):
        with st.chat_message("User"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.markdown(message.content)
>>>>>>> Stashed changes

# check if the input line is not empty
if user_message is not None and user_message != "":
    with st.chat_message("User"):
        # formated output
        st.markdown(user_message)

    with st.chat_message("AI"):
<<<<<<< Updated upstream
        ai_answer = history(user_message, chain)
        st.markdown(ai_answer)
=======
        ai_answer = chain.run(question = user_message)
        st.markdown(ai_answer)

    st.session_state.chat_history.append(AIMessage(ai_answer))
=======
    display_chat()

    # check if the input line is not empty
    if user_message is not None and user_message != "":
        with st.chat_message("User"):
            # formated output
            st.markdown(user_message)

    with st.chat_message("AI"):
        ai_answer = history(user_message, chain)
        st.markdown(ai_answer)

main()
>>>>>>> Stashed changes
>>>>>>> Stashed changes
