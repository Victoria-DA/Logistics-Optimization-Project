# Supply Chain Analysis: SQL & Python Integration 🚛

## 📌 Project Overview

This project combines **SQL** for data extraction and **Python** for advanced analysis. The goal is to optimize delivery routes and predict shipping costs.

## 🛠️ Part 1: Data Extraction (SQL)

I used SQL to query the logistics database and prepare the dataset:

- **CTEs:** To aggregate daily shipping volumes.
- **Window Functions:** To calculate the average delivery time per carrier.

## 🐍 Part 2: Data Processing (Python)

After extracting the data, I used Python for:

- **Pandas:** To clean missing tracking information.
- **Seaborn:** To create a heatmap of delay regions.

## 📈 Key Insights & Results

1. **Optimization:** Identified that switching to Carrier B for the Southern region could save 12% in costs.
2. **Efficiency:** Automated a report that previously took 5 hours to be done manually in Excel.

## 🚀 How to Run

1. Execute the queries in `data_extraction.sql`.
2. Run the Jupyter Notebook `analysis.ipynb` to see the visualizations.
