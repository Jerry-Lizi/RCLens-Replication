// DatasetUpload.js 定义一个组件，用于上传数据集到服务器。

import React, { useState } from "react";
import { uploadDataset } from "../services/ApiService"; // 引入API服务中的上传方法

function DatasetUpload() {
  const [file, setFile] = useState(null); // 文件状态

  const handleFileChange = (e) => {
    setFile(e.target.files[0]); // 当用户选择文件时更新状态
  };

  const handleUpload = async () => {
    if (file) {
      const response = await uploadDataset(file); // 调用上传服务方法
      alert(response.message); // 提示上传结果
    }
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} /> // 文件输入框
      <button onClick={handleUpload}>Upload</button> // 上传按钮
    </div>
  );
}

export default DatasetUpload;
