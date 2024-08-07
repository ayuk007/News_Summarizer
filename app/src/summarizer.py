from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

class Summarizer:
    def __init__(self, model = "mixtral-8x7b-32768", temperature = 0.7):
        self.summarizer_model = ChatGroq(model = model, temperature = temperature)
        self.prompt = Prompt.prompt
        self.chain = self.prompt | self.summarizer_model

    def summarize(self, article_title, article_text):
        return self.chain.invoke({"article_text": article_text, "article_title": article_title}).content


@dataclass
class Prompt:
    template = """You are a very good assistant that summarizes online articles.
        
        Here's the article you want to summarize.

        ==================
        Title: {article_title}

        {article_text}
        ==================

        Write a summary of the previous article.
        """
    prompt = PromptTemplate.from_template(template = template)