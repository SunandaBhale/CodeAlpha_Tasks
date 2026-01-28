import requests
from bs4 import BeautifulSoup
import pandas as pd

print("Starting web scraping...")

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

all_books = []

for page in range(1, 6):
    url = base_url.format(page)
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to load page {page}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text

        rating = book.find("p", class_="star-rating")["class"][1]

        availability = book.find("p", class_="instock availability").text.strip()

        all_books.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability
        })

df = pd.DataFrame(all_books)

df.to_csv("books_data.csv", index=False)

print(" Web scraping completed successfully!")
print(" Data saved in books_data.csv")
print(" Total books scraped:", len(df))