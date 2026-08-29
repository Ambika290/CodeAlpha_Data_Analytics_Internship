# 📚 Book Data Web Scraping

## 📌 Project Overview

This project is a web scraping project developed using Python. It extracts book information from the **Books to Scrape** website and stores the collected data in a CSV file for further analysis.

The project was completed as part of the **CodeAlpha Data Analytics Internship – Task 1: Web Scraping**.

---

## 🎯 Objective

The main objective of this project is to:

* Extract book data from a public website.
* Navigate through multiple web pages automatically.
* Collect structured information from HTML pages.
* Create a dataset for further data analysis.

---

## 🛠️ Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas

---

## 📊 Data Collected

The following information was collected for each book:

* **Title**
* **Price**
* **Availability**
* **Rating**
* **Scraped Date and Time**

---

## ⚙️ Project Workflow

1. Sent HTTP requests to the website using the `requests` library.
2. Parsed the HTML content using `BeautifulSoup`.
3. Extracted book details from each webpage.
4. Automatically navigated through all available pages.
5. Collected data for **1000 books across 50 pages**.
6. Stored the extracted data in a Pandas DataFrame.
7. Exported the final dataset as `books_data.csv`.

---

## 📁 Project Structure

```text
Web_Scraping_Project/
│
├── scraper.py
├── books_data.csv
└── README.md
```

---

## ▶️ How to Run the Project

### 1. Install Required Libraries

```bash
pip install requests beautifulsoup4 pandas
```

### 2. Run the Python Script

```bash
python scraper.py
```

### 3. Output

After successful execution, the program creates:

```text
books_data.csv
```

The dataset contains information about **1000 books**.

---

## 📈 Result

The web scraper successfully collected book information from multiple pages and created a structured CSV dataset containing **1000 book records**.

---

## 👩‍💻 Author

**Ambika**

Data Analytics Intern
CodeAlpha
