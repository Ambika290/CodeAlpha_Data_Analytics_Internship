import pandas as pd
import matplotlib.pyplot as plt
import os


# ==========================================
# 1. LOAD THE DATASET
# ==========================================

df = pd.read_csv("books_data.csv")

print("\n" + "=" * 50)
print("BOOKS DATASET - EXPLORATORY DATA ANALYSIS")
print("=" * 50)


# ==========================================
# 2. DATASET OVERVIEW
# ==========================================

print("\n1. DATASET SHAPE")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n2. FIRST 5 ROWS")
print(df.head())

print("\n3. COLUMN NAMES")
print(df.columns.tolist())

print("\n4. DATA TYPES")
print(df.dtypes)


# ==========================================
# 3. MISSING VALUES
# ==========================================

print("\n5. MISSING VALUES")
print(df.isnull().sum())


# ==========================================
# 4. DUPLICATE VALUES
# ==========================================

print("\n6. DUPLICATE ROWS")
print("Total duplicate rows:", df.duplicated().sum())


# ==========================================
# 5. DATA CLEANING
# ==========================================

# Remove £ symbol from Price
df["Price"] = df["Price"].astype(str)

df["Price"] = (
    df["Price"]
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
)

# Convert Price to numeric
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

print("\n7. DATA TYPES AFTER CLEANING")
print(df.dtypes)


# ==========================================
# 6. DESCRIPTIVE STATISTICS
# ==========================================

print("\n8. PRICE STATISTICS")
print(df["Price"].describe())


# ==========================================
# 7. EDA QUESTIONS AND ANALYSIS
# ==========================================

# QUESTION 1: What is the average book price?
average_price = df["Price"].mean()

print("\nQUESTION 1: What is the average book price?")
print(f"Average Price: £{average_price:.2f}")


# QUESTION 2: What is the most expensive book?
most_expensive = df.loc[df["Price"].idxmax()]

print("\nQUESTION 2: What is the most expensive book?")
print("Title:", most_expensive["Title"])
print("Price: £", most_expensive["Price"])


# QUESTION 3: What is the cheapest book?
cheapest = df.loc[df["Price"].idxmin()]

print("\nQUESTION 3: What is the cheapest book?")
print("Title:", cheapest["Title"])
print("Price: £", cheapest["Price"])


# QUESTION 4: How are books distributed by rating?
rating_order = ["One", "Two", "Three", "Four", "Five"]

rating_counts = (
    df["Rating"]
    .value_counts()
    .reindex(rating_order)
)

print("\nQUESTION 4: How many books are in each rating category?")
print(rating_counts)


# QUESTION 5: How many books are available?
availability_counts = df["Availability"].value_counts()

print("\nQUESTION 5: Book availability")
print(availability_counts)


# ==========================================
# 8. CREATE VISUALIZATIONS FOLDER
# ==========================================

os.makedirs("visualizations", exist_ok=True)


# ==========================================
# 9. VISUALIZATION 1 - RATING DISTRIBUTION
# ==========================================

plt.figure(figsize=(8, 5))

rating_counts.plot(kind="bar")

plt.title("Distribution of Books by Rating")
plt.xlabel("Rating")
plt.ylabel("Number of Books")

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    "visualizations/rating_distribution.png"
)

plt.show()


# ==========================================
# 10. VISUALIZATION 2 - PRICE DISTRIBUTION
# ==========================================

plt.figure(figsize=(8, 5))

plt.hist(
    df["Price"].dropna(),
    bins=20,
    edgecolor="black"
)

plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")

plt.tight_layout()

plt.savefig(
    "visualizations/price_distribution.png"
)

plt.show()


# ==========================================
# 11. VISUALIZATION 3 - AVERAGE PRICE BY RATING
# ==========================================

average_price_by_rating = (
    df.groupby("Rating")["Price"]
    .mean()
    .reindex(rating_order)
)

plt.figure(figsize=(8, 5))

average_price_by_rating.plot(
    kind="bar"
)

plt.title("Average Book Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Average Price (£)")

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    "visualizations/average_price_by_rating.png"
)

plt.show()


# ==========================================
# 12. FINAL SUMMARY
# ==========================================

print("\n" + "=" * 50)
print("EDA COMPLETED SUCCESSFULLY!")
print("=" * 50)

print(f"\nTotal Books Analyzed: {len(df)}")
print(f"Average Book Price: £{average_price:.2f}")
print(f"Highest Book Price: £{df['Price'].max():.2f}")
print(f"Lowest Book Price: £{df['Price'].min():.2f}")

print("\nVisualizations saved in the 'visualizations' folder.")