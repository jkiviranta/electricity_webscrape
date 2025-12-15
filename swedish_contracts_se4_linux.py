from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager


#################################################################
# Define functions and set date
#################################################################

# Function to scrape data from a specific alternative
def scrape_alternative_dynamic_variable():

    global driver

    try:
        # Collect information for the energy source
        energy_sources = []
        for i in range(1, 7):  # Try i from 1 to 6
            try:
                xpath = f'//*[@id="sectionTwo"]/div[2]/div/div[{i}]/p'
                text = driver.find_element(By.XPATH, xpath).text
                if text:
                    energy_sources.append(text.strip())
            except:
                break  # Stop if the element doesn't exist

        # Join all found energy sources with underscores
        energy_source_combined = "_".join(energy_sources)

        return {
            "contract_name": driver.find_element(By.XPATH, '//*[@id="svid12_3b08dbd5183b0def2ee18e"]/div[2]/div/div[1]/h1').text,
            "retailer_name": driver.find_element(By.XPATH, '//*[@id="svid12_3b08dbd5183b0def2ee18e"]/div[2]/div/div[1]/p').text,
            "fixed_price_element_ore_kwh": driver.find_element(By.XPATH, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[1]/td[2]').text,
            "unit_price_ore_kwh": 0,
            "wholesale_price_monthly_avg_ore_kwh": driver.find_element(By.XPATH, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[2]/td[2]').text,
            "markup_ore_kwh": driver.find_element(By.XPATH, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[3]/td[2]').text,
            "variable_costs_ore_kwh": driver.find_element(By.XPATH, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[4]/td[2]').text,
            "vat_ore_kwh": driver.find_element(By.XPATH, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[5]/td[2]').text,
            "total_ore_kwh": driver.find_element(By.XPATH, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[6]/td[2]').text,
            "energy_source": energy_source_combined
        }
    except Exception as e:
        print(f"Error scraping alternative: {e}")
        return None
    

# Function to scrape data from a specific alternative
def scrape_alternative_mixed():

    global driver

    try:
        # Collect information for the energy source
        energy_sources = []
        for i in range(1, 7):  # Try i from 1 to 6
            try:
                xpath = f'//*[@id="sectionTwo"]/div[2]/div/div[{i}]/p'
                text = driver.find_element(By.XPATH, xpath).text
                if text:
                    energy_sources.append(text.strip())
            except:
                break  # Stop if the element doesn't exist

        # Join all found energy sources with underscores
        energy_source_combined = "_".join(energy_sources)

        return {
            "contract_name": driver.find_element(By.XPATH, '//*[@id="svid12_3b08dbd5183b0def2ee18e"]/div[2]/div/div[1]/h1').text,
            "retailer_name": driver.find_element(By.XPATH, '//*[@id="svid12_3b08dbd5183b0def2ee18e"]/div[2]/div/div[1]/p').text,
            "fixed_price_element_ore_kwh": driver.find_element(By.XPATH, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[1]/td[2]').text,
            "unit_price_ore_kwh": driver.find_element(By.XPATH, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[2]/td[2]').text,
            "wholesale_price_monthly_avg_ore_kwh": driver.find_element(By.XPATH, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[3]/td[2]').text,
            "markup_ore_kwh": driver.find_element(By.XPATH, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[4]/td[2]').text,
            "variable_costs_ore_kwh": driver.find_element(By.XPATH, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[5]/td[2]').text,
            "vat_ore_kwh": driver.find_element(By.XPATH, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[6]/td[2]').text,
            "total_ore_kwh": driver.find_element(By.XPATH, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[7]/td[2]').text,
            "energy_source": energy_source_combined
        }
    except Exception as e:
        print(f"Error scraping alternative: {e}")
        return None
    

# Function to scrape data from a specific alternative
def scrape_alternative_fixed():

    global driver

    try:
        # Collect information for the energy source
        energy_sources = []
        for i in range(1, 7):  # Try i from 1 to 6
            try:
                xpath = f'//*[@id="sectionTwo"]/div[2]/div/div[{i}]/p'
                text = driver.find_element(By.XPATH, xpath).text
                if text:
                    energy_sources.append(text.strip())
            except:
                break  # Stop if the element doesn't exist

        # Join all found energy sources with underscores
        energy_source_combined = "_".join(energy_sources)
        
        return {
            "contract_name": driver.find_element(By.XPATH, '//*[@id="svid12_3b08dbd5183b0def2ee18e"]/div[2]/div/div[1]/h1').text,
            "retailer_name": driver.find_element(By.XPATH, '//*[@id="svid12_3b08dbd5183b0def2ee18e"]/div[2]/div/div[1]/p').text,
            "fixed_price_element_ore_kwh": driver.find_element(By.XPATH, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[1]/td[2]').text,
            "unit_price_ore_kwh": driver.find_element(By.XPATH, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[2]/td[2]').text,
            "wholesale_price_monthly_avg_ore_kwh": 0,
            "markup_ore_kwh": 0,
            "variable_costs_ore_kwh": 0,
            "vat_ore_kwh": driver.find_element(By.XPATH, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[3]/td[2]').text,
            "total_ore_kwh": driver.find_element(By.XPATH, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[4]/td[2]').text,
            "energy_source": energy_source_combined
        }
    except Exception as e:
        print(f"Error scraping alternative: {e}")
        return None

    
# Get the current date and store it as a string (to add it as a column in the DataFrame)
global current_date
current_date = datetime.now().strftime('%Y-%m-%d')

# Function to get to the page with the contract options
def open_page():
    
    global driver

    # Set up the Chrome WebDriver using WebDriver Manager for automatic driver management
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    options = webdriver.ChromeOptions()
    
    # Set options
    #options.add_argument("--headless")
    #options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    
    # Initialize the driver with specified options
    driver = webdriver.Chrome(service=service, options=options)    

    # Open the target URL
    driver.get("https://elpriskollen.se/")
    time.sleep(0.3)

    # Don't approve cookies
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/section/footer/form[2]/button'))
    ).click()

    # Fill postal code (malmö 211 09, elområde 4)
    postal_code_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="pcode"]'))
    )
    postal_code_input.send_keys("211 09")

    # Click "nästa"
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="next-page"]'))
    ).click()

    # Wait for the annual consumption field to be visible
    annual_electricity_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="annual_consumption"]'))
    )

    # Clear the default value in the Annual Consumption field
    annual_electricity_input.clear()

    # Now send the new Annual Consumption value
    annual_electricity_input.send_keys("2000")

    # Press "nästa" to proceed forward
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="next-page"]'))
    ).click()

        # Select kvartspris
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[1]/a[1]'))
    ).click()

    # Click ready to see offers
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[3]/a[2]'))
    ).click()


# Function to loop through all alternatives on the current page and scrape data for each one (starting from index 3)
def scrape_all_alternatives(start_n_alternative=1, scrape_function=scrape_alternative_dynamic_variable):

    global scraped_data
    global driver

    try:
        # Try to get the number of alternatives
        n_alternatives_text = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="svid12_330e0006183eeab50d8c0b"]/div[2]/div/div[2]/div[2]/div[1]/div/p/strong'))
        ).text.strip()

        # If empty, skip scraping
        if not n_alternatives_text.isdigit():
            print("⚠️ No alternatives found today, skipping scraping.")
            return

        n_alternatives = int(n_alternatives_text)

    except TimeoutException:
        print("⚠️ Alternatives element not found, skipping scraping.")
        return
    except Exception as e:
        print(f"❌ Unexpected error while checking alternatives: {e}")
        return

    # Number of alternatives before clicking "Show All"
    n_before_show_all = 9
    
    for i in range(start_n_alternative, n_alternatives + 1):
        print(f"Scraping alternative {i} of {n_alternatives}")
        
        if i >= n_before_show_all + 1:
            try:
                show_all_button = WebDriverWait(driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="svid12_330e0006183eeab50d8c0b"]/div[2]/div/div[2]/div[2]/div[2]/div[10]/div/button'))
                )
                driver.execute_script("arguments[0].scrollIntoView(true);", show_all_button)
                time.sleep(0.3)
                show_all_button.click()
                time.sleep(0.3)  # Wait for the additional alternatives to load
            except Exception as e:
                print("❌ Could not click 'Show All' button:", e)
                continue

        # Open the i-th alternative
       # Try the first XPath
        try:
            xpath_primary = f'//*[@id="svid12_330e0006183eeab50d8c0b"]/div[2]/div/div[2]/div[2]/div[2]/div[{i}]/div/div[5]/div[3]/a'
            element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, xpath_primary))
            )
        except TimeoutException:
            print(f"⚠️ Primary XPath failed for alternative {i}, trying fallback")
            # Try the fallback XPath
            xpath_fallback = f'//*[@id="svid12_330e0006183eeab50d8c0b"]/div[2]/div/div[2]/div[2]/div[2]/div[{i}]/div/div[5]/div[2]/a'
            try:
                element = WebDriverWait(driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH, xpath_fallback))
                )
            except TimeoutException:
                print(f"❌ Both XPaths failed for alternative {i}, skipping")
                continue       

        # Scroll and click the found element
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.3)  # Let any animations finish
        element.click()

        # Wait for the page to load
        time.sleep(0.3)

        # Scrape data from the alternative
        scraped_data_i = scrape_function()

        # If data was scraped successfully, append it to the list
        if scraped_data_i:
            scraped_data.append(scraped_data_i)

        # Go back to the main offers page
        driver.back()


# Function for pressing the button to select all contract types
def select_all_contract_types():
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="svid12_330e0006183eeab50d8c0b"]/div[2]/div/div[2]/div[1]/div[2]/a/span[1]'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(0.3)  # Let any animations finish
    element.click()


#################################################################
# Execute scraping
#################################################################

# Initialize the list to store scraped data
scraped_data = []
scraped_data_quarterly = []
scraped_data_hourly = []
scraped_data_variable = []
scraped_data_mixed = []
scraped_data_fixed_6months = []
scraped_data_fixed_1year = []
scraped_data_fixed_2years = []
scraped_data_fixed_3years = []
scraped_data_fixed_4years = []
scraped_data_fixed_5years = []

# Open the page and set parameters
open_page()

# Loop through all the contract types.
# Quarterly price contracts
scrape_all_alternatives(start_n_alternative=1, scrape_function=scrape_alternative_dynamic_variable)
# Save the data temporarily and clear the main list
scraped_data_quarterly = scraped_data.copy()
scraped_data.clear()

# Hourly price contracts
# Click twice select all contract types to reset any previous selection
select_all_contract_types()
select_all_contract_types()

# Choose hourly price contracts
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="AvtalMedTimpris"]/div/a/span[1]'))
)
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(0.3)  # Let any animations finish
element.click()
time.sleep(0.3)

# Scrape the alternatives
scrape_all_alternatives(start_n_alternative=1, scrape_function=scrape_alternative_dynamic_variable)
# Save the data temporarily and clear the main list
scraped_data_hourly = scraped_data.copy()
scraped_data.clear()

# Variable contracts
# Reset any previous selection
select_all_contract_types()  
select_all_contract_types()

# Choose variable contracts
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="RorligaAvtal"]/div/a/span[1]'))
)
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(0.3)  # Let any animations finish
element.click()
time.sleep(0.3)

# Scrape the alternatives
scrape_all_alternatives(start_n_alternative=1, scrape_function=scrape_alternative_dynamic_variable)
# Save the data temporarily and clear the main list
scraped_data_variable = scraped_data.copy()
scraped_data.clear()

# Mixed contracts
# Reset any previous selection
select_all_contract_types()  
select_all_contract_types()

# Choose mixed contracts
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="Mixavtal"]/div/a/span[1]'))
)
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(0.3)  # Let any animations finish
element.click()
time.sleep(0.3)

# Scrape the alternatives
scrape_all_alternatives(start_n_alternative=1, scrape_function=scrape_alternative_mixed)
# Save the data temporarily and clear the main list
scraped_data_mixed = scraped_data.copy()
scraped_data.clear()

# Fixed contracts - 6 months
# Reset any previous selection
select_all_contract_types()  
select_all_contract_types()

# Choose fixed contracts - 6 months
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="FastaAvtal"]/div[1]/a/span[1]'))
)
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(0.3)  # Let any animations finish
element.click()
time.sleep(0.3)

# Scrape the alternatives
scrape_all_alternatives(start_n_alternative=1, scrape_function=scrape_alternative_fixed)
# Save the data temporarily and clear the main list
scraped_data_fixed_6months = scraped_data.copy()
scraped_data.clear()

# Fixed contracts - 1 year
# Reset any previous selection
select_all_contract_types()  
select_all_contract_types()

# Choose fixed contracts - 1 year
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="FastaAvtal"]/div[2]/a/span[1]'))
)
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(0.3)  # Let any animations finish
element.click()
time.sleep(0.3)

# Scrape the alternatives
scrape_all_alternatives(start_n_alternative=1, scrape_function=scrape_alternative_fixed)
# Save the data temporarily and clear the main list
scraped_data_fixed_1year = scraped_data.copy()
scraped_data.clear()

# Fixed contracts - 2 years
# Reset any previous selection
select_all_contract_types()  
select_all_contract_types()

# Choose fixed contracts - 2 years
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="FastaAvtal"]/div[3]/a/span[1]'))
)
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(0.3)  # Let any animations finish
element.click()
time.sleep(0.3)

# Scrape the alternatives
scrape_all_alternatives(start_n_alternative=1, scrape_function=scrape_alternative_fixed)
# Save the data temporarily and clear the main list
scraped_data_fixed_2years = scraped_data.copy()
scraped_data.clear()

# Fixed contracts - 3 years
# Reset any previous selection
select_all_contract_types()  
select_all_contract_types()

# Choose fixed contracts - 3 years
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="FastaAvtal"]/div[4]/a/span[1]'))
)
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(0.3)  # Let any animations finish
element.click()
time.sleep(0.3)

# Scrape the alternatives
scrape_all_alternatives(start_n_alternative=1, scrape_function=scrape_alternative_fixed)
# Save the data temporarily and clear the main list
scraped_data_fixed_3years = scraped_data.copy()
scraped_data.clear()

# Fixed contracts - 4 years
# Reset any previous selection
select_all_contract_types()  
select_all_contract_types()

# Choose fixed contracts - 4 years
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="FastaAvtal"]/div[5]/a/span[1]'))
)
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(0.3)  # Let any animations finish
element.click()
time.sleep(0.3)

# Scrape the alternatives
scrape_all_alternatives(start_n_alternative=1, scrape_function=scrape_alternative_fixed)
# Save the data temporarily and clear the main list
scraped_data_fixed_4years = scraped_data.copy()
scraped_data.clear()

# Fixed contracts - 5 years
# Reset any previous selection
select_all_contract_types()  
select_all_contract_types()

# Choose fixed contracts - 5 years
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="FastaAvtal"]/div[6]/a/span[1]'))
)
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(0.3)  # Let any animations finish
element.click()
time.sleep(0.3)

# Scrape the alternatives
scrape_all_alternatives(start_n_alternative=1, scrape_function=scrape_alternative_fixed)
# Save the data temporarily and clear the main list
scraped_data_fixed_5years = scraped_data.copy()
scraped_data.clear()

# Add the contract type as a new key in each dictionary and combine all data into the main list
for data in scraped_data_quarterly:
    data['contract_type'] = 'quarterly_price'

for data in scraped_data_hourly:
    data['contract_type'] = 'hourly_price'

for data in scraped_data_variable:
    data['contract_type'] = 'variable_price'

for data in scraped_data_mixed:
    data['contract_type'] = 'mixed_price'

for data in scraped_data_fixed_6months:
    data['contract_type'] = 'fixed_price_6_months'
    
for data in scraped_data_fixed_1year:
    data['contract_type'] = 'fixed_price_1_year'

for data in scraped_data_fixed_2years:
    data['contract_type'] = 'fixed_price_2_years'

for data in scraped_data_fixed_3years:
    data['contract_type'] = 'fixed_price_3_years'

for data in scraped_data_fixed_4years:
    data['contract_type'] = 'fixed_price_4_years'

for data in scraped_data_fixed_5years:
    data['contract_type'] = 'fixed_price_5_years'

scraped_data = (scraped_data_quarterly + scraped_data_hourly + scraped_data_variable +
                scraped_data_mixed + scraped_data_fixed_6months + scraped_data_fixed_1year +
                scraped_data_fixed_2years + scraped_data_fixed_3years + scraped_data_fixed_4years +
                scraped_data_fixed_5years)

# Modify the dataframe or save the data as needed here
df = pd.DataFrame(scraped_data)
df['date'] = current_date
df['bidding_zone'] = 'SE4'


# Save to folder "Contract_data" that is in the same path as "scraped_data_se.csv"
output_folder = "swedish_contracts"
file_name_w_date = f"scraped_data_se4_{current_date}.csv"
output_file_path = f"{output_folder}/{file_name_w_date}"
df.to_csv(output_file_path, index=False)
