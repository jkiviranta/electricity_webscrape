from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager

#################################################################
# Prepare a list to store the scraped data
#################################################################
scraped_data = []


#################################################################
# Define functions to scrape data from the website
#################################################################

# Function for opening the webpage and inputting the common elements of search
def open_page():
    
    # Define driver as global variable
    global driver

    # Set up the Chrome WebDriver using WebDriver Manager
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    options = webdriver.ChromeOptions()

    # If you need to run headless on Linux, add these options
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(service=service, options=options)

    # Open the target URL
    driver.get("https://www.sahkonhinta.fi/")

    # Wait for the page to load
    time.sleep(5)

    # Wait for the Postal Code field to be visible
    postal_code_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="PostalCodeInput"]'))
    )

    # Clear the default value in the Postal Code field
    postal_code_input.clear()  # This clears the text in the input field

    # Now send the new Postal Code
    postal_code_input.send_keys("00100")

    # Wait for the Postal Code field to be visible
    annual_electricity_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="AnnualElectricityInput"]'))
    )

    # Clear the default value in the Postal Code field
    annual_electricity_input.clear()  # This clears the text in the input field

    # Now send the new Postal Code
    annual_electricity_input.send_keys("10000")


# Function to loop through all alternatives on the current page and scrape data for each one (starting from index 3)
def scrape_all_alternatives(start_n_alternative=3):

    # Define the global variables
    global scraped_data
    global driver

    n_alternative = start_n_alternative  # Starting alternative number
    while True:
        try:
            # Open the nth alternative
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'//*[@id="app"]/article/main/div/div[2]/div/div[2]/div/div/div[{n_alternative}]/div/div[6]/div/div[1]'))
            ).click()

            # Wait for the page to load
            time.sleep(3)

            # Scrape the data for the current alternative
            data = scrape_alternative()
            if data:
                scraped_data.append(data)

            # Go back to the main page (before opening the alternative)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'//*[@id="app"]/article/main/div/div/div[1]/div[1]/div/span[2]'))
            ).click()

            # Wait for the main page to reload
            time.sleep(3)

            # Increment to the next alternative
            n_alternative += 1

        except Exception as e:
            print(f"No more alternatives to scrape. Stopping at alternative {n_alternative - 1}.")
            break


# Function to scrape data from a specific alternative
def scrape_alternative():

    # Define the global varibles
    global driver

    # Scrape data from the specific XPaths for each alternative
    try:
        name_data_0 = driver.find_element(By.XPATH, '//*[@id="app"]/article/main/div/div/div[4]/div/div[2]/div/div[1]/span[1]').text
        data_0 = driver.find_element(By.XPATH, '//*[@id="app"]/article/main/div/div/div[4]/div/div[2]/div/div[1]/span[2]').text
        name_data_1 = driver.find_element(By.XPATH, '//*[@id="app"]/article/main/div/div/div[3]/div/div[2]/div/div[1]/span[1]').text
        data_1 = driver.find_element(By.XPATH, '//*[@id="app"]/article/main/div/div/div[3]/div/div[2]/div/div[1]/span[2]/section/span[1]').text
        name_data_2 = driver.find_element(By.XPATH, '//*[@id="app"]/article/main/div/div/div[3]/div/div[2]/div/div[2]/span[1]').text
        data_2 = driver.find_element(By.XPATH, '//*[@id="app"]/article/main/div/div/div[3]/div/div[2]/div/div[2]/span[2]/section/span[1]').text
        data_3 = driver.find_element(By.XPATH, '//*[@id="app"]/article/main/div/div/div[4]/div/div[2]/div/div[2]/span[2]').text
        data_4 = driver.find_element(By.XPATH, '//*[@id="app"]/article/main/div/div/div[4]/div/div[2]/div/div[4]/span[2]/span').text
        data_5 = driver.find_element(By.XPATH, '//*[@id="app"]/article/main/div/div/div[7]/div/div[2]/div/div/div[1]/div/ul/li[1]').text
        return [name_data_0, data_0, name_data_1, data_1, name_data_2, data_2, data_3, data_4, data_5]
    except Exception as e:
        print(f"Error scraping alternative: {e}")
        return None


#################################################################
# Set date
#################################################################

# Get the current date and store it as a string (to add it as a column in the DataFrame)
global current_date
current_date = datetime.now().strftime('%Y-%m-%d')


#################################################################
# Loop through all contract types using the functions built above
#################################################################

for contract_type in [2,3]:

    for pricing_model in [2,3,4,5]:
        # Open the page and input zip-code and annual electricity consumption
        open_page()

        WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="ContractTypeInput"]'))
        ).click()

        # Correct XPath to select the contract option dynamically using f-string
        WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, f'//*[@id="ContractTypeInput"]/option[{contract_type}]'))
        ).click()

        WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="PricingModelInput"]'))
        ).click()

        # Correct XPath to select the pricing model dynamically using f-string
        WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, f'//*[@id="PricingModelInput"]/option[{pricing_model}]'))
        ).click()

        # Select vertaile (Search button)
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/article/main/div[1]/div/div[1]/div/div/div[1]/div/div/div[6]/div/div[1]'))
        ).click()

        # Wait for the page to load
        time.sleep(10)

        # Open all alternatives (Click on "Näytä kaikki tarjoukset" button)
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/article/main/div/div[2]/div/div[2]/div/div/div[9]/div/div'))
            ).click()

            # Wait for the alternatives to load
            time.sleep(3)

            # Iterate through all alternatives
            scrape_all_alternatives()
        except Exception as e:
            # If there's an issue (e.g., no alternatives), print the error and skip to the next combination
            print(f"No alternatives found for contract type {contract_type} and pricing model {pricing_model}. Skipping to next.")
            
            # Close the driver after scraping
            driver.quit()
            continue    

#################################################################
# Close the driver and save the scraped data to a CSV file
#################################################################

# Convert the scraped data to a pandas DataFrame
columns = ['Name_data_0', 'Data_0','Name_data_1', 'Data_1', 'Name_data_2', 'Data_2', 'Data_3', 'Data_4', 'Data_5']
df = pd.DataFrame(scraped_data, columns=columns)
df["Date"] = current_date

# Save to folder "Contract_data" that is in the same path as "scraped_data.csv" and add the current date under the variable "current_date" to the file name (e.g. scraped_data20240228.csv)
output_folder = "Contract_data"
file_name_w_date = f"scraped_contract_data_{current_date}.csv"
output_file_path = f"{output_folder}/{file_name_w_date}"
df_cleaned.to_csv(output_file_path, index=False)
