'''
Descripttion: your project
Author: Jerry_Liweeeee
Date: 2024-03-14 10:02:05
'''
from flask import Blueprint
from app.controllers.articles import get_all_articles, create_article

article_bp = Blueprint('articles', __name__)

article_bp.route('/', methods=['GET'])(get_all_articles)
article_bp.route('/', methods=['POST'])(create_article)
# 其他路由...
