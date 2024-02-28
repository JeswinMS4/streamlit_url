# The wget, BeautifulSoup and selenium modules
import wget
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def webcontent(url):  
    # Configure Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=true')

    # Initialize Chrome webdriver
    driver = webdriver.Chrome(options=options)
    
    # Load the web page
    driver.get("https://www.whois.com/")
    
    # Find the input element by id and send the URL
    #elem = driver.find_element_by_id("whois_search_input") 
    #elem.send_keys(url)
    #elem.send_keys(Keys.RETURN) 
    
    # Construct the page URL
    page = "https://www.whois.com/whois/" + url
    driver.get(page)
    
    # Get the page source
    src = driver.page_source
    
    # Initialize the parser and parse the source "src"
    parser = BeautifulSoup(src, "lxml")
    
    # Define attributes for finding the desired element
    list_of_attributes = {"class": "df-raw", "id": "registrarData"}
    
    # Find the desired element
    tag = parser.findAll('pre', attrs=list_of_attributes)
    tag = str(tag).split('\n')
    
    # Close the webdriver
    driver.close()
    
    return tag

#tag = webcontent('google.com')
# for i in range(0, 5):
#     print(tag[5])
