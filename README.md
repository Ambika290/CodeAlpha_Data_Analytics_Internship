# 📊 CodeAlpha Data Analytics Internship

## 📌 Internship Overview

This repository contains the projects completed as part of the **CodeAlpha Data Analytics Internship**.

The projects focus on developing practical skills in:

- Web Scraping
- Data Collection
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Visualization
- Interactive Dashboard Development

A total of **three tasks** were completed using Python and data analytics libraries.

---

# 📁 Repository Structure

```text
CodeAlpha_Data_Analytics_Internship/
│
├── README.md
│
├── Task_1_Web_Scraping/
│   ├── scraper.py
│   ├── books_data.csv
│   └── README.md
│
├── Task_2_EDA/
│   ├── books_data.csv
│   ├── eda.py
│   ├── README.md
│   │
│   └── visualizations/
│       ├── rating_distribution.png
│       ├── price_distribution.png
│       └── average_price_by_rating.png
│
└── Task_3_Data_Visualization/
    ├── books_data.csv
    ├── dashboard.py
    ├── requirements.txt
    └── README.md
```

---

# 🚀 Task 1: Web Scraping

## 📌 Objective

The objective of this task was to collect data from a public website and create a structured dataset for further analysis.

## 🔧 Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas

## 📊 Project Description

A Python web scraper was developed to extract book information from the **Books to Scrape** website.

The scraper automatically navigates through multiple pages and collects structured information about books.

## 📋 Data Collected

The following information was collected:

- Book Title
- Price
- Availability
- Rating
- Scraped Date and Time

## 📈 Result

- Successfully scraped **1000 books**
- Collected data from **50 pages**
- Created a structured dataset
- Saved the final dataset as `books_data.csv`

---

# 🔍 Task 2: Exploratory Data Analysis (EDA)

## 📌 Objective

The objective of this task was to explore the dataset, understand its structure, identify patterns, and generate useful insights.

## 🔧 Technologies Used

- Python
- Pandas
- Matplotlib

## 📊 Analysis Performed

The following analysis was performed:

- Dataset shape analysis
- Column inspection
- Data type analysis
- Missing value analysis
- Duplicate row analysis
- Data cleaning
- Price statistics
- Rating distribution analysis
- Availability analysis

## ❓ Questions Explored

1. What is the average book price?
2. Which book is the most expensive?
3. Which book is the cheapest?
4. How are books distributed by rating?
5. What is the availability status of the books?

## 💡 Key Insights

- Total Books: **1000**
- Total Columns: **5**
- Missing Values: **0**
- Duplicate Rows: **0**
- Average Price: **35.07**
- Highest Price: **59.99**
- Lowest Price: **10.00**
- Books are distributed across five rating categories.
- All scraped books were listed as available in stock.

## 📈 Visualizations Created

The following visualizations were generated:

1. **Rating Distribution**
2. **Price Distribution**
3. **Average Price by Rating**

All visualizations are stored in the `visualizations` folder.

---

# 📊 Task 3: Data Visualization

## 📌 Objective

The objective of this task was to transform the dataset into meaningful and interactive visualizations.

## 🔧 Technologies Used

- Python
- Pandas
- Streamlit
- Plotly

## 🖥️ Dashboard Features

The interactive dashboard includes:

### 📊 Key Statistics

- Total Books
- Average Price
- Highest Price
- Lowest Price

### 📈 Visualizations

1. **Book Distribution by Rating**
2. **Distribution of Book Prices**
3. **Average Book Price by Rating**
4. **Top 10 Most Expensive Books**

### 🔍 Interactive Features

- Rating Filter
- Interactive Charts
- Dynamic Statistics
- Filtered Dataset Table

---

# 🌐 Live Dashboard

The interactive Book Data Analytics Dashboard is deployed online using Streamlit Community Cloud.

👉 **[Click here to view the Live Dashboard](https://codealphadataanalyticsinternship-9xoj2rrcidm7of6pwx4h7x.streamlit.app/)**

---

## ▶️ How to Run the Dashboard Locally

### Step 1: Install Required Libraries

```bash
python -m pip install streamlit pandas plotly
```

### Step 2: Navigate to the Dashboard Folder

```bash
cd Task_3_Data_Visualization
```

### Step 3: Run the Dashboard

```bash
python -m streamlit run dashboard.py
```

The dashboard will open in your web browser.

---

# 🛠️ Technologies Used

The following technologies were used across all projects:

- Python
- Pandas
- Requests
- BeautifulSoup
- Matplotlib
- Streamlit
- Plotly

---

# 📚 Skills Demonstrated

Through these projects, the following data analytics skills were practiced:

- Web Scraping
- Data Collection
- HTML Parsing
- Data Cleaning
- Data Preparation
- Exploratory Data Analysis
- Descriptive Statistics
- Data Visualization
- Interactive Dashboard Development
- Python Programming
- Working with CSV Files

---

# 📌 Dataset

The dataset used in these projects contains information about **1000 books** collected through web scraping.

### Dataset Columns

- **Title** – Name of the book
- **Price** – Price of the book
- **Availability** – Stock availability
- **Rating** – Book rating
- **Scraped_At** – Date and time when the data was collected

---

# 👩‍💻 Author

**Ambika**

B.Tech Student – Data Analytics

**CodeAlpha Data Analytics Internship**

---

# ✅ Project Status

🎉 **Completed Successfully**

This repository contains the three completed tasks:

- ✅ Task 1: Web Scraping
- ✅ Task 2: Exploratory Data Analysis
- ✅ Task 3: Data Visualization
- ✅ Interactive Dashboard Deployed Online
