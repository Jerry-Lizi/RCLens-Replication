// App.js 是React应用的根组件，它负责组织和展示其他子组件。

import React from "react";
import DatasetUpload from "./DatasetUpload"; // 引入数据上传组件
import VarianceVisualization from "./VarianceVisualization"; // 引入方差可视化组件
import DataTableView from "./DataTableView"; // 引入数据表格视图组件
import "./assets/styles.css"; // 引入样式文件

function App() {
  return (
    <div className="App">
      <h1>Data Analysis App</h1>
      <DatasetUpload /> // 数据上传组件，允许用户上传数据集文件
      <DataTableView /> // 数据表格视图组件，展示数据并提供查询功能
      <VarianceVisualization /> // 方差可视化组件，展示数据特征的方差
    </div>
  );
}

export default App;
