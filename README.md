CodeAlpha Data Analytics Internship

This repository contains the tasks completed during the CodeAlpha Data Analytics Internship.
The project focuses on web scraping and data visualization using Python to extract, analyze, and visualize real-world data.

Repository Structure

CodeAlpha/
|
|-- Web_Scraping/
|   |-- books_scraping.py
|   |-- books_data.csv
|
|-- Data_Visualization/
|   |-- dashboard.py
|   |-- books_data.csv
|
|-- README.md

Task 1: Web Scraping (Books Data)

Objective
To collect book data from a books website and store it in a structured format for further analysis.

Tools & Libraries Used
Python
Requests
BeautifulSoup
Pandas

Data Collected
Book Title
Price
Rating
Availability

Output
Data stored in books_data.csv

Description
The web scraping script extracts book details by parsing HTML content from the website.
The collected data is cleaned and saved into a CSV file for visualization and analysis.

Task 2: Data Visualization (Dashboard)

Objective
To visualize the scraped book data and present insights using charts and a dashboard.

Tools & Libraries Used
Python
Pandas
Matplotlib
Streamlit

Visualizations Created
Dataset preview
Price distribution
Rating distribution
Availability analysis

Dashboard Execution
Run the following command inside the Data_Visualization folder:

streamlit run dashboard.py

The dashboard will open in the browser at http://localhost:8501

Key Learnings
Web scraping using BeautifulSoup
Data cleaning and preprocessing
Data visualization using Matplotlib
Building interactive dashboards with Streamlit
End-to-end data analytics workflow

Conclusion
This project demonstrates practical experience in collecting real-world data, analyzing it, and presenting meaningful insights through visualizations and dashboards.

Author
Sunanda Bhale 
Data Analytics Intern – CodeAlpha
