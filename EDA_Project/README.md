# 📊 Exploratory Data Analysis (EDA) – Book Dataset

## 📌 Project Overview

This project performs Exploratory Data Analysis (EDA) on a dataset containing information about 1000 books collected through web scraping.

The analysis explores the structure and quality of the dataset, identifies patterns in book prices and ratings, and creates visualizations to understand the data clearly.

This project was completed as part of the **CodeAlpha Data Analytics Internship – Task 2: Exploratory Data Analysis (EDA)**.

---

## 🎯 Objectives

The main objectives of this project are:

* Understand the dataset structure.
* Check data types and column information.
* Identify missing values.
* Detect duplicate records.
* Clean and prepare the Price column for analysis.
* Calculate descriptive statistics.
* Explore patterns in book prices and ratings.
* Create meaningful visualizations.

---

## 🛠️ Technologies Used

* Python
* Pandas
* Matplotlib

---

## 📁 Dataset Information

The dataset contains information about **1000 books** with the following columns:

* **Title** – Name of the book
* **Price** – Price of the book
* **Availability** – Stock availability
* **Rating** – Book rating
* **Scraped_At** – Date and time when the data was collected

---

## 🔍 Data Analysis Performed

### 1. Dataset Overview

* Total Rows: **1000**
* Total Columns: **5**

### 2. Data Quality Check

* Missing Values: **0**
* Duplicate Rows: **0**

### 3. Data Cleaning

The Price column initially contained the pound symbol (£). The symbol was removed, and the column was converted from text format to numeric format for analysis.

### 4. Price Statistics

* Average Price: **£35.07**
* Minimum Price: **£10.00**
* Maximum Price: **£59.99**

### 5. Questions Explored

1. What is the average price of books?
2. Which book is the most expensive?
3. Which book is the cheapest?
4. How are books distributed across rating categories?
5. What is the availability status of the books?

---

## 📊 Key Insights

* The dataset contains **1000 book records**.
* There are **no missing values** in the dataset.
* There are **no duplicate rows**.
* The average book price is approximately **£35.07**.
* The highest book price is **£59.99**.
* The lowest book price is **£10.00**.
* The largest rating category is **One Star**, containing **226 books**.
* All **1000 books** in the scraped dataset were listed as **In stock**.

---

## 📈 Visualizations Created

The project generates the following visualizations:

1. **Rating Distribution**
2. **Price Distribution**
3. **Average Price by Rating**

All visualizations are saved in the `visualizations` folder.

---

## 📁 Project Structure

```text
EDA_Project/
│
├── books_data.csv
├── eda.py
├── README.md
│
└── visualizations/
    ├── rating_distribution.png
    ├── price_distribution.png
    └── average_price_by_rating.png
```

---

## ▶️ How to Run the Project

### 1. Install Required Libraries

```bash
pip install pandas matplotlib
```

### 2. Run the EDA Script

```bash
python eda.py
```

### 3. Output

The program will:

* Display dataset information in the terminal.
* Perform data cleaning and analysis.
* Answer key exploratory questions.
* Generate and save visualizations.

---

## 👩‍💻 Author

**Ambika**

Data Analytics Intern
CodeAlpha
