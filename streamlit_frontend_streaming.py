# st.session_state => streamlit state
# st.chat_input => input box 
# st.chat_message  => Used to display a chat message in a conversational UI.
# st.text => Used to display plain text in your Streamlit app.
# st.write_stream => Used for streaming


import streamlit as st
# import chatbot from langgraph_backend file
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

# st.session_state -> dict -> 
CONFIG = {'configurable': {'thread_id': 'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

#{'role': 'user', 'content': 'Hi'}
#{'role': 'assistant', 'content': 'Hi=ello'}

user_input = st.chat_input('Type here')

if user_input:

    # first add the message to message_history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    # print user's messages
    with st.chat_message('user'):
        st.text(user_input)

    # print ai's response
    with st.chat_message('assistant'):
    # streaming way(chatbot.stream provide two things-> 1. message_chunk 2.metadata)
        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config= {'configurable': {'thread_id': 'thread-1'}},
                stream_mode= 'messages'
            )
        )

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})

    