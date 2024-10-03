from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to your msedgedriver
EDGE_DRIVER_PATH = 'D:/NEW/msedgedriver.exe'

# List of phone numbers to check
phone_numbers = [
#add your number here
'9876543210',

]

# Initialize the Edge WebDriver
service = Service(executable_path=EDGE_DRIVER_PATH)
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options)

# Function to check if "Data Booster" option is available for a phone number
def check_data_booster(phone_number):
    url = 'https://www.jio.com/selfcare/recharge/mobility/'
    driver.get(url)
    
    try:
        # Set the window size
        driver.set_window_size(1058, 802)

        # Input the phone number
        phone_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "submitNumber"))
        )
        phone_input.send_keys(phone_number)

        # Click the Continue button
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div:nth-child(12) > .j-button"))
        )
        continue_button.click()

        # Wait for the page to load and check for "Data Booster"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".plans_container__32sCX"))
        )
        
        # Check if "Data Booster" option is present
        data_booster_element = driver.find_elements(By.XPATH, "//*[contains(text(), 'Data Booster')]")
        return len(data_booster_element) > 0

    except Exception as e:
        print(f"Error checking {phone_number}: {e}")
        return False

# Check each phone number and print the result
results = {}
for number in phone_numbers:
    result = check_data_booster(number)
    results[number] = "Recharge Done" if result else "Recharge Not Done"

# Print the results with numbers before each output
for index, (number, status) in enumerate(results.items(), start=1):
    print(f"{index}) {number}: {status}")

# Close the WebDriver
driver.quit()
