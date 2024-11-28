import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

# Step 1: Open a file picker dialog to select the CSV file
Tk().withdraw()  # Hide the root window
file_path = askopenfilename(title="Select the retail_data.csv file", filetypes=[("CSV files", "*.csv")])

# Check if a file was selected
if not file_path:
    print("Error: No file selected. Please select a valid 'retail_data.csv' file.")
    exit()

# Step 2: Check if the file exists
if not os.path.exists(file_path):
    print(f"The file '{file_path}' does not exist. Creating a new empty CSV file...")
    
    # Define column names
    columns = ['date', 'sales', 'revenue', 'product_name']
    
    # Create an empty DataFrame with the required columns
    data = pd.DataFrame(columns=columns)
    
    # Save the empty DataFrame to the CSV file
    data.to_csv(file_path, index=False)
    print(f"New empty CSV file '{file_path}' created.")
else:
    # Step 3: Try to load the existing dataset
    try:
        data = pd.read_csv(file_path)
        print("File loaded successfully!")
        
        # Limit to 1,000 entries if the dataset is larger
        if len(data) > 1000:
            print("Dataset contains more than 1,000 entries. Limiting to the first 1,000 entries.")
            data = data.head(1000)
        
        print(data.head())  # Print the first few rows to inspect the data
        
        # Rename columns to match expected names
        data.columns = data.columns.str.lower().str.replace(' ', '_')  # Convert to lowercase and replace spaces with underscores
    except Exception as e:
        print(f"Error loading the file: {e}")
        exit()

# Step 4: Ensure the required columns exist in the dataset
required_columns = {'date', 'sales', 'revenue', 'product_name'}
missing_columns = required_columns - set(data.columns)
if missing_columns:
    print(f"Error: Dataset is missing one or more required columns: {missing_columns}")
    exit()

# Step 5: Ensure 'date' column is in datetime format
data['date'] = pd.to_datetime(data['date'], errors='coerce')  # Convert to datetime, invalid dates become NaT
if data['date'].isnull().sum() > 0:
    print(f"Warning: Some dates could not be parsed. These rows are set to NaT.")

# Step 6: Extract useful time features (Month, Year, Day of Week)
data['month'] = data['date'].dt.month
data['year'] = data['date'].dt.year
data['day_of_week'] = data['date'].dt.day_name()

# --- 1. Seasonal Sales Patterns ---
# Group by month and year, summing sales and revenue
monthly_sales = data.groupby(['year', 'month']).agg({'sales': 'sum', 'revenue': 'sum'}).reset_index()

# Create a pivot table for plotting seasonal sales
monthly_sales_pivot = monthly_sales.pivot(index="month", columns="year", values="sales")

# Plot heatmap for seasonal sales patterns
plt.figure(figsize=(10, 6))
sns.heatmap(monthly_sales_pivot, annot=True, fmt='.0f', cmap="coolwarm")
plt.title("Seasonal Sales Patterns (Monthly Sales)")
plt.xlabel("Year")
plt.ylabel("Month")
plt.show()

# --- 2. Top Products ---
# Group by product_name and sum sales and revenue
top_products = data.groupby('product_name').agg({'sales': 'sum', 'revenue': 'sum'}).reset_index()

# Sort products by sales and revenue, limit to 1,000 if necessary
top_products = top_products.head(1000)

# Sort products by sales and revenue
top_products_sales = top_products.sort_values(by='sales', ascending=False).head(10)
top_products_revenue = top_products.sort_values(by='revenue', ascending=False).head(10)

# Plot top 10 products by sales
plt.figure(figsize=(12, 6))
sns.barplot(x='sales', y='product_name', data=top_products_sales)
plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product Name")
plt.show()

# Plot top 10 products by revenue
plt.figure(figsize=(12, 6))
sns.barplot(x='revenue', y='product_name', data=top_products_revenue)
plt.title("Top 10 Products by Revenue")
plt.xlabel("Total Revenue")
plt.ylabel("Product Name")
plt.show()

# --- 3. Revenue Trends ---
# Group by year and month to get revenue trends over time
monthly_revenue = data.groupby(['year', 'month']).agg({'revenue': 'sum'}).reset_index()

# Plot revenue trends over time
plt.figure(figsize=(12, 6))
sns.lineplot(x='month', y='revenue', hue='year', data=monthly_revenue, marker='o')
plt.title("Revenue Trends Over Time")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.show()
