import streamlit as st
import pandas as pd
import plotly.express as px


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Book Data Dashboard",
    page_icon="📚",
    layout="wide"
)


# ==========================================
# LOAD DATA
# ==========================================

@st.cache_data
def load_data():
    df = pd.read_csv("books_data.csv")

    # Clean Price column
    df["Price"] = (
        df["Price"]
        .astype(str)
        .str.replace("£", "", regex=False)
        .str.replace("Â", "", regex=False)
    )

    # Convert Price to numeric
    df["Price"] = pd.to_numeric(
        df["Price"],
        errors="coerce"
    )

    return df


df = load_data()


# ==========================================
# DASHBOARD TITLE
# ==========================================

st.title("📚 Book Data Analytics Dashboard")

st.markdown(
    "Interactive visualization dashboard created using "
    "**Python, Streamlit, and Plotly**."
)

st.divider()


# ==========================================
# SIDEBAR FILTERS
# ==========================================

st.sidebar.header("🔍 Dashboard Filters")

rating_order = ["One", "Two", "Three", "Four", "Five"]

selected_ratings = st.sidebar.multiselect(
    "Select Rating",
    options=rating_order,
    default=rating_order
)


# ==========================================
# FILTER DATA
# ==========================================

filtered_df = df[
    df["Rating"].isin(selected_ratings)
].copy()


# ==========================================
# KEY STATISTICS
# ==========================================

st.subheader("📊 Key Statistics")

col1, col2, col3, col4 = st.columns(4)

total_books = len(filtered_df)

if total_books > 0:
    average_price = filtered_df["Price"].mean()
    highest_price = filtered_df["Price"].max()
    lowest_price = filtered_df["Price"].min()
else:
    average_price = 0
    highest_price = 0
    lowest_price = 0


col1.metric(
    "Total Books",
    total_books
)

col2.metric(
    "Average Price",
    f"₹{average_price:.2f}"
)

col3.metric(
    "Highest Price",
    f"₹{highest_price:.2f}"
)

col4.metric(
    "Lowest Price",
    f"₹{lowest_price:.2f}"
)


st.divider()


# ==========================================
# CHECK IF DATA IS AVAILABLE
# ==========================================

if filtered_df.empty:

    st.warning("Please select at least one rating from the sidebar.")

else:

    # ==========================================
    # RATING DISTRIBUTION
    # ==========================================

    rating_counts = (
        filtered_df["Rating"]
        .value_counts()
        .reindex(rating_order, fill_value=0)
        .reset_index()
    )

    rating_counts.columns = [
        "Rating",
        "Number of Books"
    ]


    fig_rating = px.bar(
        rating_counts,
        x="Rating",
        y="Number of Books",
        title="Book Distribution by Rating",
        text="Number of Books"
    )

    fig_rating.update_layout(
        xaxis_title="Rating",
        yaxis_title="Number of Books"
    )

    st.plotly_chart(
        fig_rating,
        use_container_width=True,
        config={"displayModeBar": True}
    )


    # ==========================================
    # PRICE DISTRIBUTION
    # ==========================================

    fig_price = px.histogram(
        filtered_df,
        x="Price",
        nbins=20,
        title="Distribution of Book Prices"
    )

    fig_price.update_layout(
        xaxis_title="Price (₹)",
        yaxis_title="Number of Books"
    )

    st.plotly_chart(
        fig_price,
        use_container_width=True,
        config={"displayModeBar": True}
    )


    # ==========================================
    # AVERAGE PRICE BY RATING
    # ==========================================

    average_price_by_rating = (
        filtered_df
        .groupby("Rating")["Price"]
        .mean()
        .reindex(rating_order)
        .dropna()
        .reset_index()
    )

    average_price_by_rating.columns = [
        "Rating",
        "Average Price"
    ]


    fig_avg_price = px.bar(
        average_price_by_rating,
        x="Rating",
        y="Average Price",
        title="Average Book Price by Rating",
        text_auto=".2f"
    )

    fig_avg_price.update_layout(
        xaxis_title="Rating",
        yaxis_title="Average Price (₹)"
    )

    st.plotly_chart(
        fig_avg_price,
        use_container_width=True,
        config={"displayModeBar": True}
    )


    # ==========================================
    # TOP 10 MOST EXPENSIVE BOOKS
    # ==========================================

    top_books = (
        filtered_df
        .sort_values(
            by="Price",
            ascending=False
        )
        .head(10)
    )


    fig_top_books = px.bar(
        top_books,
        x="Price",
        y="Title",
        orientation="h",
        title="Top 10 Most Expensive Books",
        text="Price"
    )

    fig_top_books.update_traces(
        texttemplate="₹%{text:.2f}",
        textposition="outside"
    )

    fig_top_books.update_layout(
        xaxis_title="Price (₹)",
        yaxis_title="Book Title",
        yaxis={"categoryorder": "total ascending"}
    )

    st.plotly_chart(
        fig_top_books,
        use_container_width=True,
        config={"displayModeBar": True}
    )


    # ==========================================
    # DATA TABLE
    # ==========================================

    st.divider()

    st.subheader("📋 Book Dataset")

    display_df = filtered_df.copy()

    # Format price with ₹ symbol
    display_df["Price"] = display_df["Price"].apply(
        lambda x: f"₹{x:.2f}"
    )

    st.dataframe(
        display_df,
        use_container_width=True
    )


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "CodeAlpha Data Analytics Internship | "
    "Task 3: Data Visualization | "
    "Created by Ambika"
)