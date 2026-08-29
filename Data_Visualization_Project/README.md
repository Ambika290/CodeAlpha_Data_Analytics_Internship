# 📚 Book Data Analytics Dashboard

## 📌 Project Overview

This project presents an interactive Book Data Analytics Dashboard created using Python, Streamlit, and Plotly.

The dashboard analyzes book data collected through web scraping and presents important insights using interactive charts, filters, key statistics, and a data table.

This project was completed as part of the CodeAlpha Data Analytics Internship – Task 3: Data Visualization.

---

## 🎯 Objectives

The main objectives of this project are:

- Create an interactive data visualization dashboard.
- Analyze book prices and ratings.
- Display important statistics clearly.
- Provide interactive filters for users.
- Visualize patterns and trends in the dataset.

---

## 🛠️ Technologies Used

- Python
- Pandas
- Streamlit
- Plotly

---

## 📊 Dataset Information

The dashboard uses a dataset containing information about 1000 books.

### Dataset Columns

- **Title** – Name of the book
- **Price** – Price of the book
- **Availability** – Stock availability
- **Rating** – Book rating
- **Scraped_At** – Date and time when the data was collected

---

## 📈 Dashboard Features

### 🔍 Rating Filter

Users can filter the dashboard based on book ratings:

- One
- Two
- Three
- Four
- Five

### 📊 Key Statistics

The dashboard displays:

- Total Books
- Average Price
- Highest Price
- Lowest Price

### 📉 Visualizations

The dashboard includes the following visualizations:

1. **Book Distribution by Rating**
2. **Distribution of Book Prices**
3. **Average Book Price by Rating**
4. **Top 10 Most Expensive Books**

### 📋 Interactive Dataset

Users can view the filtered book dataset directly on the dashboard.

---

## 💡 Key Insights

- The dataset contains **1000 books**.
- The displayed average price is approximately **₹35.07**.
- The displayed highest price is **₹59.99**.
- The displayed lowest price is **₹10.00**.
- Book ratings are distributed across five rating categories.
- Users can interactively filter the dashboard based on ratings.

> **Note:** The original scraped website used British Pound (£) prices. The dashboard displays the ₹ symbol for presentation purposes. The numeric values were not converted using an exchange rate.

---

## 📁 Project Structure

```text
Data_Visualization_Project/
│
├── books_data.csv
├── dashboard.py
└── README.md