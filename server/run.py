'''
Descripttion: 启动Flask应用。
Author: Jerry_Liweeeee
Date: 2024-03-14 10:01:28
'''
from app import create_app

app = create_app()  # 创建Flask应用

if __name__ == '__main__':
    app.run(debug=True)  # 运行Flask应用，开启调试模式

