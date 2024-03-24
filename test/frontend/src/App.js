/*
 * @Descripttion: your project
 * @Author: Jerry_Liweeeee
 * @Date: 2024-03-24 15:04:29
 */
import React, { useState } from "react";
import "./App.css";
import axios from "axios";

function App() {
  const [variance, setVariance] = useState(null);
  const [error, setError] = useState("");

  const handleFileUpload = (e) => {
    setError(""); // 重置错误信息
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append("file", file);

    axios
      .post("http://localhost:5000/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      })
      .then((response) => {
        if (response.data.variance !== undefined) {
          // 显示方差结果
          setVariance(response.data.variance);
        } else if (response.data.error) {
          // 显示错误信息
          setError(response.data.error);
        }
      })
      .catch((error) => {
        // 显示错误信息
        setError(error.response.data.error || "发生错误，请重试。");
      });
  };

  return (
    <div className="App">
      <header className="App-header">
        <input type="file" onChange={handleFileUpload} />
        {error && <p className="error">错误：{error}</p>}
        {variance !== null && <p>方差: {variance}</p>}
      </header>
    </div>
  );
}

export default App;
