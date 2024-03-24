'''
Descripttion: your project
Author: Jerry_Liweeeee
Date: 2024-03-24 14:18:41
'''
from flask import Flask, request, jsonify
import json
import numpy as np

app = Flask(__name__)

# 开启跨域支持
from flask_cors import CORS
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    接收前端上传的JSON文件，提取所有元素中的'values'，
    计算这些'values'的整体方差并返回结果。
    """
    try:
        file = request.files['file']
        data = json.load(file)  # 加载JSON数据

        # 检查数据是否是一个数组
        if not isinstance(data, list):
            return jsonify({'error': 'JSON文件的顶层结构应为数组'}), 400
        
        # 提取所有元素中的'values'
        values_list = [item['values'] for item in data if 'values' in item and isinstance(item['values'], (int, float))]
        
        # 检查是否有有效的values可计算方差
        if not values_list:
            return jsonify({'error': '没有有效的values数据以计算方差'}), 400
        
        # 计算方差
        values_array = np.array(values_list)
        variance = np.var(values_array)
        
        return jsonify({'variance': variance})

    except json.JSONDecodeError:
        # 捕获并处理 JSON 格式错误
        return jsonify({'error': '无法解析JSON文件，请检查文件格式'}), 400
    except Exception as e:
        # 捕获并处理其他错误
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
