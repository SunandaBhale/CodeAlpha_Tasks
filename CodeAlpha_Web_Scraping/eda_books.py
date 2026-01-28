import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("books_data.csv")

df["Price"] = (
    df["Price"]
    .str.replace("£", "", regex=False)
    .astype(float)
)

df["Availability"] = (
    df["Availability"]
    .str.extract(r"(\d+)")
    .astype(int)
)

print(df.head())
print(df.info())
print(df.describe())

plt.figure()
sns.histplot(df["Price"], bins=20)
plt.title("Price Distribution")
plt.show()

plt.figure()
sns.countplot(x="Rating", data=df)
plt.title("Book Rating Count")
plt.show()

plt.figure()
sns.boxplot(x="Rating", y="Price", data=df)
plt.title("Price vs Rating")
plt.show()