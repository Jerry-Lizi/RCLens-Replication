'''
Descripttion: your project
Author: Jerry_Liweeeee
Date: 2024-03-15 16:25:53
'''
from flask import Flask

def create_app():
    app = Flask(__name__)  # 创建Flask应用实例
    
    # 注册蓝图，用于管理路由
    from app.api.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    return app  # 返回创建的Flask应用实例
