
# 📊 End-to-End Automated Data Analysis Pipeline

## 🔹 Overview

This project is an automated data analysis system that processes CSV datasets, performs data cleaning, generates insights, visualizes trends, and enables SQL-based analysis.

It is designed to work on **different datasets dynamically** without hardcoding column names, making it flexible and adaptable.

---

## 🔹 Features

* ✅ Automatic data cleaning (missing values, duplicates)
* ✅ Dynamic column type detection (numeric, categorical, date)
* ✅ Statistical analysis (mean, median, min, max, correlation)
* ✅ Data visualization (histograms, bar charts, trend lines)
* ✅ Safe file handling for real-world messy datasets
* ✅ SQL-based querying for business insights

---

## 🔹 Tech Stack

* **Python** (Pandas, Matplotlib)
* **MySQL** (for data querying)
* **Git & GitHub** (version control)

---

## 🔹 Project Structure

```
project/
│
├── src/
│   ├── main.py
│   ├── cleaning.py
│   ├── analysis.py
│   └── utils.py
│
├── data/
│   └── sample_superstore.csv
│
├── sql/
│   └── queries.sql
│
├── outputs/        # ignored in git
├── README.md
└── .gitignore
```

---

## 🔹 Workflow

```
CSV Dataset
   ↓
Data Cleaning (Python)
   ↓
Analysis + Visualization
   ↓
Stored as Cleaned Data
   ↓
SQL Queries for Insights
```

---

## 🔹 How to Run

### 1. Install dependencies

```bash
pip install pandas matplotlib
```

### 2. Run the project

```bash
python src/main.py data/sample_superstore.csv
```

---

## 🔹 Sample SQL Queries

```sql
-- Total Sales
SELECT SUM(Sales) FROM test;

-- Sales by Category
SELECT Category, SUM(Sales)
FROM test
GROUP BY Category;

-- Monthly Trend
SELECT MONTH(`Order Date`), SUM(Sales)
FROM test
GROUP BY MONTH(`Order Date`);
```

---

## 🔹 Key Learnings

* Built a **flexible and adaptive data pipeline**
* Handled real-world dataset issues (missing values, inconsistent formats)
* Integrated Python with SQL for end-to-end analysis
* Applied modular programming and clean code practices

---

## 🔹 Future Improvements

* Add dashboard (Power BI / Streamlit)
* Add automated report generation (PDF)
* Connect directly to database from Python

---

## 🔹 Author

**Ayush Chib**

