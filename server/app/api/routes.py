from flask import Blueprint, request
from app.services.data_service import upload_data, query_data
# 新增import
from app.services.data_service import compute_variance

api_bp = Blueprint('api', __name__)  # 创建蓝图实例，管理一组相关的路由


@api_bp.route('/upload', methods=['POST'])  # 定义上传数据的路由，只允许POST方法
def upload():
    return upload_data(request)  # 调用服务层处理上传的数据

@api_bp.route('/query', methods=['GET'])  # 定义查询数据的路由，只允许GET方法
def query():
    key = request.args.get('key')  # 从请求的查询字符串中获取'key'参数
    return query_data(key)  # 调用服务层处理数据查询

# 方差计算路由
@api_bp.route('/variance', methods=['POST'])
def variance():
    return compute_variance(request)  # 调用服务层计算方差