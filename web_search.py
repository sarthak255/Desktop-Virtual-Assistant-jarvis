# src/web_search.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Function to perform a web search
def web_search(query):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    search_box = driver.find_element_by_name("q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    results = driver.find_elements_by_css_selector("h3")
    for result in results:
        print(result.text)
    driver.quit()

# Test the web search function
if __name__ == "__main__":
    query = "OpenAI GPT-4"
    web_search(query)
