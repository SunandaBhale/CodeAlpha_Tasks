import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Books Dashboard", layout="centered")
st.title("📚 Books Data Dashboard")

df = pd.read_csv("books_data.csv")

st.subheader("🔍 Dataset Preview")
st.dataframe(df.head())

st.subheader("📊 Dataset Information")
st.write("Number of rows:", df.shape[0])
st.write("Number of columns:", df.shape[1])

if "Price" in df.columns:
    st.subheader("💰 Price Distribution")
    fig1, ax1 = plt.subplots()
    ax1.hist(df["Price"], bins=10)
    ax1.set_xlabel("Price")
    ax1.set_ylabel("Count")
    st.pyplot(fig1)

if "Rating" in df.columns:
    st.subheader("⭐ Rating Distribution")
    fig2, ax2 = plt.subplots()
    df["Rating"].value_counts().plot(kind="bar", ax=ax2)
    ax2.set_xlabel("Rating")
    ax2.set_ylabel("Number of Books")
    st.pyplot(fig2)

for col in df.columns:
    if "category" in col.lower():
        st.subheader("📂 Books by Category")
        fig3, ax3 = plt.subplots()
        df[col].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax3)
        st.pyplot(fig3)
        break

st.success("✅ Dashboard loaded successfully")