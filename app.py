import streamlit as st

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Research Assistant")
st.write(
    "Ask a research-related question and get an AI-generated response."
)

st.subheader("Ask your question")

query = st.text_area(
    "Enter your research question:",
    placeholder="Example: What are the applications of Agentic AI in education?"
)

if st.button("Generate Answer"):
    if query.strip():
        st.info("Your question was received.")
        st.write("Question:", query)
    else:
        st.warning("Please enter a question.")