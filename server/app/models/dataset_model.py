# 定义数据存储和查询的逻辑。(数据模型和数据库操作。)
class DataStorage:
    data = []  # 类变量，用于在内存中暂时存储数据

    @classmethod
    def add_data(cls, json_data):
        cls.data.append(json_data)  # 添加数据到存储中

    @classmethod
    def query_by_key(cls, key):
        # 简单的线性搜索，返回包含指定key的所有数据
        return [item for item in cls.data if key in item]
