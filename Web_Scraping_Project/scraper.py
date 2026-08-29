import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from urllib.parse import urljoin


# Base website URL
base_url = "https://books.toscrape.com/"

# Start URL
url = base_url

# Store all book data
books_data = []

# Page counter
page_number = 1


while url:

    print(f"Scraping page {page_number}...")

    # Send request
    response = requests.get(url)

    # Check request
    if response.status_code != 200:
        print(f"Failed to retrieve page {page_number}")
        break

    # Parse HTML
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all books
    books = soup.find_all("article", class_="product_pod")

    # Extract data from each book
    for book in books:

        # Title
        title = book.h3.a["title"]

        # Price
        price = book.find("p", class_="price_color").get_text(strip=True)

        # Availability
        availability = book.find(
            "p",
            class_="instock availability"
        ).get_text(strip=True)

        # Rating
        rating = book.find(
            "p",
            class_="star-rating"
        )["class"][1]

        # Store book information
        books_data.append({
            "Title": title,
            "Price": price,
            "Availability": availability,
            "Rating": rating,
            "Scraped_At": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        })

    # Find next page
    next_button = soup.select_one("li.next a")

    if next_button:

        next_url = next_button["href"]

        # Automatically create the correct next page URL
        url = urljoin(url, next_url)

        page_number += 1

    else:
        url = None


# Create DataFrame
df = pd.DataFrame(books_data)

# Save as CSV
df.to_csv(
    "books_data.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nScraping completed successfully!")
print(f"Total books scraped: {len(df)}")

print("\nFirst 5 rows:")
print(df.head())

print("\nCSV file saved as books_data.csv")
