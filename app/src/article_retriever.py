import requests
from newspaper import Article

class ArticleRetriever:
    def __init__(self, timeout = 10):
        self.session = requests.Session()
        self.timeout = timeout
        self.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
        }

    def retrieve_article(self, article_url):
        article_response = self.session.get(article_url, headers = self.headers, timeout = self.timeout)
        if article_response.status_code == 200:
            article = Article(article_url)
            article.download()
            article.parse()
            return article.text, article.title
        
        else:
            print(f"Failed to fetch the article at {article_url}")
            return None, None            
