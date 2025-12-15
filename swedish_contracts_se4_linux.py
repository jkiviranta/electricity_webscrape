from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
import time
import pandas as pd
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager


#################################################################
# Define functions and set date
#################################################################

# Define a safe click that waits until the element is visible and scrolls to it
def safe_click(driver, xpath, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", element
        )
        try:
            element.click()
        except (ElementClickInterceptedException, StaleElementReferenceException):
            driver.execute_script("arguments[0].click();", element)
    except TimeoutException:
        raise TimeoutException(f"Timed out waiting for clickable element: {xpath}")


# Function to safely get text from an element
def safe_get_text(driver, xpath, timeout=5):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element.text.strip()
    except TimeoutException:
        return ""


# Function to scrape data from a specific alternative
def scrape_alternative_dynamic_variable():

    global driver

    try:
        # Collect information for the energy source
        energy_sources = []
        for i in range(1, 7):  # Try i from 1 to 6
            xpath = f'//*[@id="sectionTwo"]/div[2]/div/div[{i}]/p'
            text = safe_get_text(driver, xpath)
            if text:
                energy_sources.append(text)
            else:
                break  # Stop if the element doesn't exist or is empty

        # Join all found energy sources with underscores
        energy_source_combined = "_".join(energy_sources)

        return {
            "contract_name": safe_get_text(driver, '//*[@id="svid12_3b08dbd5183b0def2ee18e"]/div[2]/div/div[1]/h1'),
            "retailer_name": safe_get_text(driver, '//*[@id="svid12_3b08dbd5183b0def2ee18e"]/div[2]/div/div[1]/p'),
            "fixed_price_element_ore_kwh": safe_get_text(driver, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[1]/td[2]'),
            "unit_price_ore_kwh": 0,
            "wholesale_price_monthly_avg_ore_kwh": safe_get_text(driver, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[2]/td[2]'),
            "markup_ore_kwh": safe_get_text(driver, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[3]/td[2]'),
            "variable_costs_ore_kwh": safe_get_text(driver, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[4]/td[2]'),
            "vat_ore_kwh": safe_get_text(driver, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[5]/td[2]'),
            "total_ore_kwh": safe_get_text(driver, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[6]/td[2]'),
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
            xpath = f'//*[@id="sectionTwo"]/div[2]/div/div[{i}]/p'
            text = safe_get_text(driver, xpath)
            if text:
                energy_sources.append(text)
            else:
                break  # Stop if the element doesn't exist or is empty

        # Join all found energy sources with underscores
        energy_source_combined = "_".join(energy_sources)

        return {
            "contract_name": safe_get_text(driver, '//*[@id="svid12_3b08dbd5183b0def2ee18e"]/div[2]/div/div[1]/h1'),
            "retailer_name": safe_get_text(driver, '//*[@id="svid12_3b08dbd5183b0def2ee18e"]/div[2]/div/div[1]/p'),
            "fixed_price_element_ore_kwh": safe_get_text(driver, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[1]/td[2]'),
            "unit_price_ore_kwh": safe_get_text(driver, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[2]/td[2]'),
            "wholesale_price_monthly_avg_ore_kwh": safe_get_text(driver, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[3]/td[2]'),
            "markup_ore_kwh": safe_get_text(driver, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[4]/td[2]'),
            "variable_costs_ore_kwh": safe_get_text(driver, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[5]/td[2]'),
            "vat_ore_kwh": safe_get_text(driver, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[6]/td[2]'),
            "total_ore_kwh": safe_get_text(driver, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[7]/td[2]'),
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
            xpath = f'//*[@id="sectionTwo"]/div[2]/div/div[{i}]/p'
            text = safe_get_text(driver, xpath)
            if text:
                energy_sources.append(text)
            else:
                break  # Stop if the element doesn't exist or is empty

        # Join all found energy sources with underscores
        energy_source_combined = "_".join(energy_sources)

        return {
            "contract_name": safe_get_text(driver, '//*[@id="svid12_3b08dbd5183b0def2ee18e"]/div[2]/div/div[1]/h1'),
            "retailer_name": safe_get_text(driver, '//*[@id="svid12_3b08dbd5183b0def2ee18e"]/div[2]/div/div[1]/p'),
            "fixed_price_element_ore_kwh": safe_get_text(driver, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[1]/td[2]'),
            "unit_price_ore_kwh": safe_get_text(driver, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[2]/td[2]'),
            "wholesale_price_monthly_avg_ore_kwh": 0,
            "markup_ore_kwh": 0,
            "variable_costs_ore_kwh": 0,
            "vat_ore_kwh": safe_get_text(driver, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[3]/td[2]'),
            "total_ore_kwh": safe_get_text(driver, '//*[@id="sectionThree"]/div[1]/table/tbody/tr[4]/td[2]'),
            "energy_source": energy_source_combined
        }

    except Exception as e:
        print(f"Error scraping alternative: {e}")
        return None

    
# Get the current date and store it as a string (to add it as a column in the DataFrame)
global current_date
current_date = datetime.now().strftime('%Y-%m-%d')

def open_page():

    global driver

    # Set up the Chrome WebDriver using WebDriver Manager for automatic driver management
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    options = webdriver.ChromeOptions()

    # Set options
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Initialize the driver with specified options
    driver = webdriver.Chrome(service=service, options=options)

    # Open the target URL
    driver.get("https://elpriskollen.se/")
    time.sleep(0.3)

    # Reject cookies
    safe_click(driver, '/html/body/div[2]/div/section/footer/form[2]/button')

    # Fill postal code
    postal_code_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="pcode"]'))
    )
    postal_code_input.send_keys("211 09")

    # Click "nästa"
    safe_click(driver, '//*[@id="next-page"]')

    # Wait for the annual consumption field
    annual_electricity_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="annual_consumption"]'))
    )

    # Scroll into view
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", annual_electricity_input)
    time.sleep(0.2)

    # Clear and enter new value
    annual_electricity_input.clear()
    annual_electricity_input.send_keys("2000")

    # Click "nästa"
    safe_click(driver, '//*[@id="next-page"]')
    time.sleep(0.2)

    # Select kvartspris
    safe_click(driver, '//*[@id="app"]/div/div[1]/div[2]/div[1]/a[1]')

    # Click ready to see offers
    safe_click(driver, '//*[@id="app"]/div/div[3]/a[2]')


# Function to scrape all alternatives
def scrape_all_alternatives(driver, scrape_fn, start_n=1):
    scraped = []
    show_all_clicked = False

    try:
        n_text = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 '//*[@id="svid12_330e0006183eeab50d8c0b"]/div[2]/div/div[2]/div[2]/div[1]/div/p/strong')
            )
        ).text.strip()

        if not n_text.isdigit():
            return scraped

        n_alternatives = int(n_text)

    except TimeoutException:
        return scraped

    for i in range(start_n, n_alternatives + 1):
        if i > 9 and not show_all_clicked:
            try:
                safe_click(
                    driver,
                    '//*[@id="svid12_330e0006183eeab50d8c0b"]/div[2]/div/div[2]/div[2]/div[2]/div[10]/div/button'
                )
                show_all_clicked = True
            except Exception:
                pass

        primary = (
            f'//*[@id="svid12_330e0006183eeab50d8c0b"]/div[2]/div/div[2]/div[2]/div[2]/div[{i}]/div/div[5]/div[3]/a'
        )
        fallback = (
            f'//*[@id="svid12_330e0006183eeab50d8c0b"]/div[2]/div/div[2]/div[2]/div[2]/div[{i}]/div/div[5]/div[2]/a'
        )

        try:
            safe_click(driver, primary)
        except Exception:
            try:
                safe_click(driver, fallback)
            except Exception:
                continue

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        scraped.append(scrape_fn(driver))
        driver.back()

    return scraped


# Function for pressing the button to select all contract types
def select_all_contract_types():
    safe_click(
        driver,
        '//*[@id="svid12_330e0006183eeab50d8c0b"]/div[2]/div/div[2]/div[1]/div[2]/a/span[1]'
    )


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
safe_click(driver, '//*[@id="AvtalMedTimpris"]/div/a/span[1]')
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
safe_click(driver, '//*[@id="RorligaAvtal"]/div/a/span[1]')
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
safe_click(driver, '//*[@id="Mixavtal"]/div/a/span[1]')
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
safe_click(driver, '//*[@id="FastaAvtal"]/div[1]/a/span[1]')
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
safe_click(driver, '//*[@id="FastaAvtal"]/div[2]/a/span[1]')
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
safe_click(driver, '//*[@id="FastaAvtal"]/div[3]/a/span[1]')
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
safe_click(driver, '//*[@id="FastaAvtal"]/div[4]/a/span[1]')
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
safe_click(driver, '//*[@id="FastaAvtal"]/div[5]/a/span[1]')
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
safe_click(driver, '//*[@id="FastaAvtal"]/div[6]/a/span[1]')
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
