# Project Name

StayTech_Retail_Sales_Highlights

# Team Members
1. Mann Chavda (Ku2407u327)
2. Akshat Bansal (Ku2407u251)
3. Meet Dave (Ku2407u331)
4. Heman Darji (Ku2407u779)
5. Meet Vastani (Ku2407u451)

 # Overview
 
This script is a Python-based retail data analysis tool that processes a CSV file containing sales and revenue data. It extracts meaningful insights like seasonal sales patterns, top-performing products, and revenue trends over time using data visualization.

## Table of content
1. Overview
2. Requirements
3. Features
4. How to Use
5. CSV File Requirements
6. Data Preprocessing
7. Visualizations
8. Seasonal Sales Patterns
9. Top 10 Products
10. Revenue Trends
11. Output Examples
12. Error Handling
13. Future Enhancements
14. Author



## Requirements
Python 3.x


### Required Python libraries:
- pandas
- matplotlib
- seaborn
- tkinter (for file selection dialog)
- json
- os 

## Features
1. Seasonal Sales Patterns:
 - Visualizes monthly sales data across multiple years using a heatmap.
2. Top Products Analysis:
- Identifies and visualizes the top 10 products by sales and revenue.
3. Revenue Trends:
- Plots revenue trends over time to observe seasonal changes and patterns.

## How to Use
- Run the script in a Python environment with the required libraries installed.
- When prompted, select the retail_sales_highlights.csv file using the file picker dialog.

### The script will:
- Load the CSV file or create an empty one if it doesn't exist.
- Validate and preprocess the data (e.g., ensure dates are in proper format).
- Perform data analysis and visualization.

## CSV File Requirements
- The script expects a CSV file with the following columns:
- date: Date of the transaction (in a recognizable date format).
- sales: Total sales for the transaction.
- revenue: Total revenue for the transaction.
- product_name: Name of the product.
- If the file is missing required columns, the script will terminate with an error.

## Data Preprocessing
-  Ensures the date column is in datetime format.
-  Extracts useful time-based features:
  - Month
  - Year
  - Day of the week
  - Limits the dataset to the first 1,000 rows if it exceeds this size.

## Visualizations

Seasonal Sales Patterns:
Heatmap of monthly sales patterns across years.
Top 10 Products:
Bar charts showing the top 10 products by:
Total sales
Total revenue
Revenue Trends:
Line plot showing revenue trends over time, grouped by year and month.

## Output Examples
1. Seasonal Sales Patterns: Heatmap showing sales variations by month and year.
2. Top Products:
  - Bar chart for top 10 products by sales.
  - Bar chart for top 10 products by revenue.
3. Revenue Trends: Line chart showing revenue fluctuations across months for each year.

## Error Handling
- If no file is selected, the script exits with an error message.
- If the selected file is missing, an empty CSV file with the required columns is created.
- If required columns are missing in the dataset, the script terminates with an error.

## Future Enhancements
- Add functionality to analyze additional trends, like sales per weekday or per region.
- Provide options for exporting visualizations.
- Allow user-defined thresholds for data size or filtering criteria.

## Author
- Developed by Team StayTech.
- Thank You.
