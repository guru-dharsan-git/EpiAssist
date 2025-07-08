from model import answer_query
import streamlit as st

# Configure page
st.set_page_config(
    page_title="PH Surveillance RAG",
    page_icon="🦠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar with custom styling
with st.sidebar:
    st.markdown("---")
    st.markdown("Built using:")
    st.markdown("- FAISS vector database")
    st.markdown("- LangChain RAG framework")
    st.markdown("- Built using GuruLearn")

# Main content area
st.title("Public Health Surveillance RAG System")
st.markdown("""
**Ask questions about:**
- Disease outbreak detection protocols
- Laboratory confirmation methods
- Epidemiological investigation procedures
- Technical Guidelines (TG) Booklets analysis
""")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input and response handling
if prompt := st.chat_input("Enter your public health question:"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Analyzing guidelines..."):
            answer = answer_query(prompt)
        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
