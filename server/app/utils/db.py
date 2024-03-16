from pymongo import MongoClient
from config.config import Config

# 建立MongoDB数据库连接
client = MongoClient(Config.MONGO_URI)
db = client.get_default_database()
