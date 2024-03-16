'''
Descripttion: your project
Author: Jerry_Liweeeee
Date: 2024-03-15 16:31:36
'''
# 定义数据存储和查询的逻辑。(数据模型和数据库操作。)
from app.utils.db import db

class Dataset:
    collection = db['datasets']  # 指定数据库中的集合（相当于SQL数据库中的表）

    @classmethod
    def insert(cls, data):
        # 插入数据到MongoDB
        return cls.collection.insert_one(data).inserted_id

    @classmethod
    def find_by_key(cls, key):
        # 从MongoDB中查询数据
        cursor = cls.collection.find()
        results = [{doc[key]: doc[key]} for doc in cursor if key in doc]
        return results
