from flask import Flask
from .core import init_databases,db
from .requirment2.sentiment_analysis import sentiment_analysis

def init_plugs(app: Flask) -> None:
    init_databases(app)
