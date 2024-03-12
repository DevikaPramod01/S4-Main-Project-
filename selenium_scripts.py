from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Specify the path to the ChromeDriver executable
chrome_driver_path = r'C:/Users/devik/Desktop/S4 main project/prjt/chromedriver-win64/chromedriver-win64/chromedriver.exe'

# Set the path to ChromeDriver using the Service class
service = Service(chrome_driver_path)

# Create a new instance of the Chrome driver, passing the service
driver = webdriver.Chrome(service=service)

# Navigate to a website
driver.get('https://www.example.com')

# Your Selenium code goes here

# Close the browser when done
driver.quit()
