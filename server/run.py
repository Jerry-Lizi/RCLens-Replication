'''
Descripttion: your project
Author: Jerry_Liweeeee
Date: 2024-03-14 10:01:28
'''
from flask import Flask
from app.routes.article_routes import article_bp
from app.routes.user_routes import user_bp
from app.routes.comment_routes import comment_bp

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(article_bp, url_prefix='/api/articles')
app.register_blueprint(user_bp, url_prefix='/api/users')
app.register_blueprint(comment_bp, url_prefix='/api/comments')

if __name__ == '__main__':
    app.run(debug=True)
