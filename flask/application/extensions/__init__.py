from flask import Flask
from .core import init_databases,db
from .requirment2.sentiment_analysis import sentiment_analysis
from .requirment2.search import init_search_recommend_module, search_recommend
def init_plugs(app: Flask) -> None:
    init_databases(app)
    init_search_recommend_module()