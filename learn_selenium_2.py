from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

options = Options()
# Run in headless mode if needed
# options.add_argument('--headless')

service = Service(executable_path='/path/to/new/geckodriver')
driver = webdriver.Firefox(service=service, options=options)

try:
    driver.get("https://www.python.org")
    print(f"Page title: {driver.title}")
finally:
    driver.quit()
