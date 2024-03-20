// VarianceVisualization.js 组件用于可视化展示数据集中每个特征的方差。

import React from "react";

function VarianceVisualization() {
  // 用伪数据来展示方差可视化的样子
  // 在实际应用中，这些数据应该从后端获取并动态渲染
  const varianceData = [
    { feature: "age", variance: 2.76 },
    { feature: "blood_pressure", variance: 1.13 },
    // ... 更多特征数据
  ];

  return (
    <div>
      <h2>Variance Visualization</h2>
      <div className="variance-container">
        {varianceData.map((data, index) => (
          <div
            key={index}
            className="variance-bar"
            style={{ height: `${data.variance * 10}px` }}
          >
            {data.feature}
          </div>
        ))}
      </div>
    </div>
  );
}

export default VarianceVisualization;
