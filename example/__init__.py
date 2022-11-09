from flask import Flask
from flask_html import Page, Head

def create_app():
    
    app = Flask(__name__)
    from .blueprint import pages
    app.register_blueprint(pages)
    return app
    
    