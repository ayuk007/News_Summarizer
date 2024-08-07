import streamlit as st
from src.article_retriever import ArticleRetriever
from src.summarizer import Summarizer

article_retriever = ArticleRetriever()
summarizer = Summarizer()

def summarize(article_url, model, temperature):
    summarizer.summarizer_model.model_name = model
    summarizer.summarizer_model.temperature = temperature
    article_text, article_title = article_retriever.retrieve_article(article_url)
    if isinstance(article_title, str):
        summary = summarizer.summarize(article_title, article_text)
        return summary
    else:
        return "Unable to fetch summary"

st.title("News Summarizer")
with st.sidebar:
    st.header("Input Parameter")
    model_name = st.text_input("Model Name", "mixtral-8x7b-32768")
    temperature = st.slider("Temperature", 0.1, 1.0, step = 0.1,value = 0.7)

article_url = st.text_input("Article URL", "http://www.example.com")

if st.button("Process"):
    summary = summarize(article_url, model_name, temperature)
    st.write(summary)