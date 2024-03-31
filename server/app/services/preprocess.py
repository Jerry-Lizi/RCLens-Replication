import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

def handle_missing_values(data, numerical_strategy='mean', categorical_strategy='most_frequent'):
    """
    处理数据集中的缺失值。
    
    参数:
    data -- pandas DataFrame对象，包含数据集
    numerical_strategy -- 数值型列的填充策略，默认为均值填充
    categorical_strategy -- 分类列的填充策略，默认为众数填充
    
    返回:
    处理缺失值后的DataFrame
    """
    # 分类特征和数值特征应该明确区分
    numerical_features = data.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = data.select_dtypes(include=['object', 'category']).columns
    
    # 数值型特征缺失值处理
    num_imputer = SimpleImputer(strategy=numerical_strategy)
    data[numerical_features] = num_imputer.fit_transform(data[numerical_features])
    
    # 分类特征缺失值处理
    cat_imputer = SimpleImputer(strategy=categorical_strategy)
    data[categorical_features] = cat_imputer.fit_transform(data[categorical_features])
    
    return data

def standardize_data(data):
    """
    对数据集进行标准化处理。
    
    参数:
    data -- pandas DataFrame对象，包含数据集
    
    返回:
    标准化后的DataFrame
    """
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    scaled_df = pd.DataFrame(scaled_data, index=data.index, columns=data.columns)
    
    return scaled_df
    
def preprocess_data(data):
    """
    对数据集进行预处理：缺失值处理和标准化处理。
    
    参数:
    data -- pandas DataFrame对象，包含数据集
    
    返回:
    预处理后的DataFrame
    """
    # 缺失值处理
    data = handle_missing_values(data)
    
    # 只对数值型特征进行标准化处理
    numerical_features = data.select_dtypes(include=['int64', 'float64']).columns
    data[numerical_features] = standardize_data(data[numerical_features])
    
    return data
