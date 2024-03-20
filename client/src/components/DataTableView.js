/*
 * @Descripttion: your project
 * @Author: Jerry_Liweeeee
 * @Date: 2024-03-20 10:27:50
 */
// DataTableView.js 组件用于展示数据集的表格视图，并允许用户通过查询来筛选数据。

import React, { useState } from "react";
import { fetchQueryResults } from "../services/ApiService"; // 引入服务层的查询方法

function DataTableView() {
  const [query, setQuery] = useState(""); // 查询字符串的状态
  const [data, setData] = useState([]); // 表格数据的状态

  const handleQueryChange = (e) => {
    setQuery(e.target.value); // 当用户输入查询条件时更新状态
  };

  const handleSearch = async () => {
    try {
      const results = await fetchQueryResults(query); // 发送查询请求并获取结果
      setData(results); // 使用查询结果更新表格数据
    } catch (error) {
      console.error("Error fetching query results:", error); // 处理查询错误
    }
  };

  // 根据数据动态生成表格头部
  const renderTableHeader = () => {
    return data.length > 0 ? (
      <tr>
        {Object.keys(data[0]).map((key, index) => (
          <th key={index}>{key}</th> // 显示每一个特征作为表头
        ))}
      </tr>
    ) : null;
  };

  // 根据数据动态生成表格行
  const renderTableRows = () => {
    return data.map((row, index) => (
      <tr key={index}>
        {Object.values(row).map((val, idx) => (
          <td key={idx}>{val}</td> // 显示每一行的特征值
        ))}
      </tr>
    ));
  };

  // 渲染查询框和表格
  return (
    <div>
      <input
        type="text"
        value={query}
        onChange={handleQueryChange}
        placeholder="Enter your query here"
      />
      <button onClick={handleSearch}>Search</button>
      <table>
        <thead>{renderTableHeader()} // 渲染表头</thead>
        <tbody>{renderTableRows()} // 渲染表格数据行</tbody>
      </table>
    </div>
  );
}

export default DataTableView;
