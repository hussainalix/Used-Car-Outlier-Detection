🚗 Used Car Price Outlier Detection & Cleaning:
This project focuses on the Data Cleaning and Statistical Analysis of a real-world used cars dataset (4,000+ records). The goal was to identify and remove extreme price values (outliers) that could negatively impact Machine Learning models.
🧐 The Problem:
Raw data is often "noisy." In this dataset, car prices ranged from very low to several million dollars. These extreme values (outliers) make it difficult for models to learn the "normal" price trends.
🛠️ The Solution: IQR MethodI implemented the Interquartile Range (IQR) method to handle these outliers mathematically:Lower Quartile ($Q1$): 25th percentile of the data.Upper Quartile ($Q3$): 75th percentile of the data.IQR Formula: $IQR = Q3 - Q1$Boundaries: - Lower: $Q1 - 1.5 \times IQR$Upper: $Q3 + 1.5 \times IQR$
Key Technical Skills:
Data Wrangling: Converting string price data (e.g., $10,300) to numeric format using str.replace() and astype(float).
Visualization: Using Seaborn and Matplotlib to visualize data distribution.
Data Filtering: Successfully identified and removed 244 outliers.
📊 Visual Proof:
<img width="1184" height="490" alt="Images" src="https://github.com/user-attachments/assets/bc8f9860-062e-4739-ad90-6de128f58263" />
