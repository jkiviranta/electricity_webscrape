from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime, timedelta

# Set up the Chrome WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open the target URL (replace this with the URL you want to scrape)
driver.get("https://data.nordpoolgroup.com/auction/day-ahead/prices?deliveryDate=latest&currency=EUR&aggregation=Hourly&deliveryAreas=EE,LT,LV,AT,BE,FR,GER,NL,PL,DK1,DK2,FI,NO1,NO2,NO3,NO4,NO5,SE1,SE2,SE3,SE4")

# Disallow cookies
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-mdc-dialog-0"]/div/div/gdpr-dialog/div/div[2]/div/button[1]'))
).click()

# Wait for the table to be visible
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="grid-wrapper"]/div[1]/dx-data-grid/div[1]'))
)

# Locate the table element
table = driver.find_element(By.XPATH, '//*[@id="grid-wrapper"]/div[1]/dx-data-grid/div[1]')

# Extract all the rows within the table
rows = table.find_elements(By.XPATH, ".//tr")

# Create an empty list to store table data
table_data = []

# Iterate through the rows
for row in rows:
    # Extract all cells in the row (both 'td' and 'th' for header rows)
    cells = row.find_elements(By.XPATH, ".//td | .//th")
    # Get the text from each cell and strip quotes or unwanted characters
    cell_data = [cell.text.replace('"', '') for cell in cells]  # Remove quotes if present
    # Append the row data to the table_data list
    table_data.append(cell_data)

# Convert the scraped table data into a pandas DataFrame
df = pd.DataFrame(table_data)

# Keep only data rows
df_cleaned = df.iloc[2:26]  # Select rows 3-27 (indexes 2-26)

# Drop the first column
df_cleaned = df_cleaned.drop(df.columns[0], axis=1)

# Clean the data: split any values that might be combined in one column
#df_cleaned = df_cleaned.apply(lambda x: x.str.split(",", expand=True))

# Rename the columns as specified
df_cleaned.columns = ["EE", "LT", "LV", "AT", "BE", "FR", "GER", "NL", "PL", "DK1", "DK2", "FI", "NO1", "NO2", "NO3", "NO4", "NO5", "SE1", "SE2", "SE3", "SE4"]

# Add a column indicating the date of prices (tomorrow)
today = datetime.now()
tomorrow = today + timedelta(days=1)
df_cleaned["Date"] = tomorrow.date()

# Add a column with the hour ranges
hour_ranges = ["00-01", "01-02", "02-03", "03-04", "04-05", "05-06", "06-07", "07-08", "08-09", "09-10", "10-11", "11-12", "12-13", "13-14", "14-15", "15-16", "16-17", "17-18", "18-19", "19-20", "20-21", "21-22", "22-23", "23-00"]

# Assuming your scraped data corresponds to these hours, add them as a new column
df_cleaned["Hour"] = hour_ranges[:len(df_cleaned)]  # Adjust length if needed

# Reorder the columns to put "Date" and "Hour" in the first positions if desired
df_cleaned = df_cleaned[["Date", "Hour"] + df_cleaned.columns[:-2].tolist()]

# Close the browser
driver.quit()

# Save a safety version to folder "Contract_data" that is in the same path as "scraped_price_data.csv" and add the current date under the variable "today" to the file name (e.g. scraped_price_data20240228.csv)
output_folder = "Price_data"
file_name_w_date = f"scraped_price_data_{today.strftime('%Y%m%d')}.csv"
output_file_path = f"{output_folder}/{file_name_w_date}"
df_cleaned.to_csv(output_file_path, index=False)