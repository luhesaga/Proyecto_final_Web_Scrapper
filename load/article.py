from sqlalchemy import Column, String, Integer

from base import Base

class Article(Base):
    __tablename__ = 'articles'

    id = Column(String, primary_key = True)
    body = Column(String)
    host = Column(String)
    title = Column(String)
    news_paper_uid = Column(String)
    n_tokens_body = Column(Integer)
    n_tokens_title = Column(Integer)
    url = Column(String, unique = True)

    def __init__(self,
                 uid,
                 body,
                 host,
                 news_paper_uid,
                 n_tokens_body,
                 n_tokens_title,
                 title,
                 url):
        self.id = uid
        self.body = body
        self.host = host
        self.news_paper_uid = news_paper_uid
        self.n_tokens_body = n_tokens_body
        self.n_tokens_title = n_tokens_title
        self.title = title
        self.url = url