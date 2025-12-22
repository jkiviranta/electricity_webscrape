from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException,
    StaleElementReferenceException
)
import time
import pandas as pd
from datetime import datetime


#################################################################
# Safe click helper
#################################################################

def safe_click(driver, by, xpath, timeout=5, description="element"):
    """
    Safely attempts to click an element.
    Returns True if clicked successfully, False otherwise.
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, xpath))
        )

        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        time.sleep(0.5)

        try:
            element.click()
            return True

        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", element)
            return True

    except (TimeoutException, StaleElementReferenceException) as e:
        print(f"⚠️ safe_click failed for {description}: {e}")
        return False

    except Exception as e:
        print(f"❌ Unexpected click error for {description}: {e}")
        return False


#################################################################
# Scraping functions
#################################################################

def scrape_alternative_dynamic_variable():
    global driver
    try:
        energy_sources = []
        for i in range(1, 7):
            try:
                xpath = f'//*[@id="sectionTwo"]/div[2]/div/div[{i}]/p'
                text = driver.find_element(By.XPATH, xpath).text
                if text:
                    energy_sources.append(text.strip())
            except:
                break

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


def scrape_alternative_mixed():
    global driver
    try:
        energy_sources = []
        for i in range(1, 7):
            try:
                xpath = f'//*[@id="sectionTwo"]/div[2]/div/div[{i}]/p'
                text = driver.find_element(By.XPATH, xpath).text
                if text:
                    energy_sources.append(text.strip())
            except:
                break

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


def scrape_alternative_fixed():
    global driver
    try:
        energy_sources = []
        for i in range(1, 7):
            try:
                xpath = f'//*[@id="sectionTwo"]/div[2]/div/div[{i}]/p'
                text = driver.find_element(By.XPATH, xpath).text
                if text:
                    energy_sources.append(text.strip())
            except:
                break

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

  
#################################################################
# Globals and setup
#################################################################

current_date = datetime.now().strftime('%Y-%m-%d')
scraped_data = []


#################################################################
# Navigation
#################################################################

def open_page():
    
    global driver

    # Set up Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Open the target URL
    driver.get("https://elpriskollen.se/")
    time.sleep(2)

    # Reject cookies
    safe_click(
        driver,
        By.XPATH,
        '/html/body/div/div/div[2]/div[2]/div[2]/div[2]/dialog/div[2]/form[2]/button',
        description="reject cookies"
    )

    # Postal code
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="pcode"]'))
    ).send_keys("852 29")

    safe_click(driver, By.XPATH, '//*[@id="next-page"]', description="next (postal code)")

    # Annual consumption
    annual = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="annual_consumption"]'))
    )
    annual.clear()
    annual.send_keys("2000")

    safe_click(driver, By.XPATH, '//*[@id="next-page"]', description="next (consumption)")
    safe_click(driver, By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[1]/a[1]', description="kvartspris")
    safe_click(driver, By.XPATH, '//*[@id="app"]/div/div[3]/a[2]', description="see offers")


#################################################################
# Scrape alternatives
#################################################################
 
def scrape_all_alternatives(start_n_alternative=1, scrape_function=scrape_alternative_dynamic_variable):
    global scraped_data
    global driver

    try:
        n_alternatives_text = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,
                '//*[@id="svid12_330e0006183eeab50d8c0b"]/div[2]/div/div[2]/div[2]/div[1]/div/p/strong'))
        ).text.strip()

        if not n_alternatives_text.isdigit():
            print("⚠️ No alternatives found")
            return

        n_alternatives = int(n_alternatives_text)

    except Exception as e:
        print(f"❌ Could not determine alternatives: {e}")
        return

    n_before_show_all = 9

    for i in range(start_n_alternative, n_alternatives + 1):
        print(f"Scraping alternative {i}/{n_alternatives}")

        if i >= n_before_show_all + 1:
            safe_click(
                driver,
                By.XPATH,
                '//*[@id="svid12_330e0006183eeab50d8c0b"]/div[2]/div/div[2]/div[2]/div[2]/div[10]/div/button',
                description="show all"
            )

        xpath_primary = f'//*[@id="svid12_330e0006183eeab50d8c0b"]/div[2]/div/div[2]/div[2]/div[2]/div[{i}]/div/div[5]/div[3]/a'
        xpath_fallback = f'//*[@id="svid12_330e0006183eeab50d8c0b"]/div[2]/div/div[2]/div[2]/div[2]/div[{i}]/div/div[5]/div[2]/a'

        if not safe_click(driver, By.XPATH, xpath_primary, description=f"alternative {i} primary"):
            if not safe_click(driver, By.XPATH, xpath_fallback, description=f"alternative {i} fallback"):
                print(f"⏭️ Skipping alternative {i}")
                continue

        time.sleep(1)

        data = scrape_function()
        if data:
            scraped_data.append(data)

        driver.back()
        time.sleep(1)


#################################################################
# Select all contract types
#################################################################

def select_all_contract_types():
    safe_click(
        driver,
        By.XPATH,
        '//*[@id="svid12_330e0006183eeab50d8c0b"]/div[2]/div/div[2]/div[1]/div[2]/a/span[1]',
        description="select all contract types"
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
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="AvtalMedTimpris"]/div/a/span[1]'))
)
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(1)  # Let any animations finish
element.click()
time.sleep(1)

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
time.sleep(1)  # Let any animations finish
element.click()
time.sleep(1)

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
time.sleep(1)  # Let any animations finish
element.click()
time.sleep(1)

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
time.sleep(1)  # Let any animations finish
element.click()
time.sleep(1)

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
time.sleep(1)  # Let any animations finish
element.click()
time.sleep(1)

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
time.sleep(1)  # Let any animations finish
element.click()
time.sleep(1)

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
time.sleep(1)  # Let any animations finish
element.click()
time.sleep(1)

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
time.sleep(1)  # Let any animations finish
element.click()
time.sleep(1)

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
time.sleep(1)  # Let any animations finish
element.click()
time.sleep(1)

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
df['bidding_zone'] = 'SE2'


# Save to folder "swedish_contracts"
output_folder = "swedish_contracts"
file_name_w_date = f"scraped_data_se2_{current_date}.csv"
output_file_path = f"{output_folder}/{file_name_w_date}"
df.to_csv(output_file_path, index=False)
