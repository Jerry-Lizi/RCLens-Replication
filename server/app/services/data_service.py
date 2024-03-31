'''
Descripttion: your project
Author: Jerry_Liweeeee
Date: 2024-03-15 16:30:19
'''
'''
Descripttion: your project
Author: Jerry_Liweeeee
Date: 2024-03-15 16:30:19
'''
# 将处理数据上传和查询、计算方差的业务逻辑。
from flask import jsonify
import json
import numpy as np
from app.models.dataset_model import Dataset
from sklearn.neighbors import LocalOutlierFactor
from app.services.preprocess import preprocess_data #引用数据预处理的函数


def upload_data(request):
    file = request.files.get('file')  # 从请求中获取上传的文件
    if not file:
        return jsonify({'error': 'No file provided'}), 400  # 如果文件不存在，返回错误
    
    try:
        json_data = json.loads(file.read())  # 读取文件内容并转换成JSON
        Dataset.insert(json_data)  # 插入数据到MongoDB
        return jsonify({'message': 'Data uploaded successfully'}), 201  # 返回成功消息
    except Exception as e:
        return jsonify({'error': 'Invalid JSON format', 'message': str(e)}), 400  # 如果JSON格式错误，返回错误

def query_data(key):
    if not key:
        return jsonify({'error': 'No key provided'}), 400  # 如果key参数不存在，返回错误
    
    results = Dataset.find_by_key(key)  # 从MongoDB查询数据
    if results:
        return jsonify({'results': results}), 200  # 如果查询到数据，返回数据
    else:
        return jsonify({'message': 'No data found for the given key'}), 404  # 如果没有查询到数据，返回消息


# 计算方差的服务函数
def compute_variance(request):
    data = request.json  # 从请求体中获取JSON数据
    if not data:
        return jsonify({'error': 'No data provided'}), 400  # 如果数据不存在，返回错误

    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        return jsonify({'error': 'Invalid data format'}), 400  # 检查数据格式是否为列表中的字典

    try:
        # 转换数据并计算方差
        features = {key: [] for key in data[0]}  # 初始化特征列表
        for item in data:
            for key in features:
                features[key].append(item.get(key, None))  # 收集每个键的值
        
        variances = {key: np.var(features[key]) for key in features}  # 计算方差
        return jsonify({'variance': variances}), 200  # 返回方差
    except Exception as e:
        return jsonify({'error': 'Error processing data', 'message': str(e)}), 500  # 处理错误

def preprocess_and_evaluate(data):
    """
    对数据进行预处理并计算LOF分数。
    
    参数:
    data -- 以字典形式提供的原始数据
    
    返回:
    包含LOF分数的字典
    """
    # 将字典转换为DataFrame
    df = pd.DataFrame(data)
    # 执行预处理
    preprocessed_df = preprocess_data(df)
    # 计算LOF分数
    lof = LocalOutlierFactor()
    lof_scores = -lof.fit_predict(preprocessed_df)
    # 将LOF分数添加到原始DataFrame中
    df['LOF_Score'] = lof_scores
    # 转换为字典以便返回JSON
    result = df.to_dict(orient='records')
    return result