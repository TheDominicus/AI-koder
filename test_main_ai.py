import pytest
from unittest.mock import patch, MagicMock
from langchain_core.messages import HumanMessage, AIMessage
from streamlit import session_state

def test_init_ai():
    from main_ai import init_ai
    from langchain.chains import LLMChain
    chain = init_ai()
    assert isinstance(chain, LLMChain), "Failed to setup chain"


# Mock chain.run to return a fixed response
@patch("main_ai.LLMChain.run", return_value="This is a test response")
def test_history(mock_run):
    from main_ai import history, init_ai

    session_state.chat_history = []
    chain = init_ai()
    user_message = "Test message"
    ai_response = history(user_message, chain)

    assert ai_response == "This is a test response"
    assert len(session_state.chat_history) == 2
    assert isinstance(session_state.chat_history[0], HumanMessage)
    assert session_state.chat_history[0].content == "Test message"
    assert isinstance(session_state.chat_history[1], AIMessage)
    assert session_state.chat_history[1].content == "This is a test response"

def test_display_chat():
    from main_ai import display_chat
    from streamlit.delta_generator import DeltaGenerator

    session_state.chat_history = [
        HumanMessage("User message"),
        AIMessage("AI message")
    ]

    with patch("streamlit.markdown") as mock_markdown, patch("streamlit.chat_message") as mock_chat_message:
        mock_chat_message.return_value.__enter__.return_value = DeltaGenerator(None)

        display_chat()

        assert mock_chat_message.call_count == 2
        assert mock_markdown.call_count == 2
        mock_markdown.assert_any_call("User message")
        mock_markdown.assert_any_call("AI message")