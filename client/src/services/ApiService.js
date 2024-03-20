/*
 * @Descripttion: your project
 * @Author: Jerry_Liweeeee
 * @Date: 2024-03-20 10:28:50
 */
// ApiService.js 定义了与后端API交互的服务，包括数据上传和查询。

const API_BASE_URL = "http://localhost:5000/api"; // 后端API的基础URL，根据你的后端服务实际部署地址来修改

// 上传数据集到后端
export const uploadDataset = async (file) => {
  const formData = new FormData();
  formData.append("file", file); // 创建一个FormData对象，并添加文件

  try {
    const response = await fetch(`${API_BASE_URL}/upload`, {
      // 发送POST请求到后端的上传接口
      method: "POST",
      body: formData,
    });
    if (!response.ok) {
      throw new Error("Network response was not ok.");
    }
    return await response.json(); // 解析JSON响应
  } catch (error) {
    console.error("Error during data upload:", error);
    throw error;
  }
};

// 根据查询条件获取数据
export const fetchQueryResults = async (query) => {
  try {
    const response = await fetch(
      `${API_BASE_URL}/query?key=${encodeURIComponent(query)}`,
      {
        // 发送GET请求到后端的查询接口
        method: "GET",
      }
    );
    if (!response.ok) {
      throw new Error("Network response was not ok.");
    }
    return await response.json(); // 解析JSON响应
  } catch (error) {
    console.error("Error fetching query results:", error);
    throw error;
  }
};
