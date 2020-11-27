import requests as re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import winsound
PATH = "C:\Program Files (x86)\chromedriver.exe"
# load up the webdriver
browser = webdriver.Chrome(PATH)
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second

# shipping info
email = ""
fn = ""
ln = ""
address = ""
city = ""
zip = ""
phone = ""

# billing info
# cnum = ""
# nameOnCard = ""
# exp = ""
# sc = ""

# continously scrape the page looking for restock.
gmk_olivia_url = "https://novelkeys.xyz/collections/extras-group-buy/products/gmk-olivia-extras"

inStock = False
while not inStock:
    data = re.get(gmk_olivia_url)
    soup = BeautifulSoup(data.text, "html.parser")
    dropdown = soup.find("select", class_='product-form__variants')
    ctr = 0
    for option in dropdown:
        option = str(option)
        if ctr == 1:
            if "Sold out" in option: # light base still sold out
                # stay false, repeating loop
                print("Still not in stock yet")
            else:
                inStock = True
            break
        ctr += 1
    time.sleep(1.5)

winsound.Beep(frequency, duration)
browser.get(gmk_olivia_url)

# once restock has been confirmed, proceed with selenium automation process.
# cart item
print("Loaded")
dropdown = Select(browser.find_element_by_class_name("single-option-selector"))
dropdown.select_by_visible_text("Light Base")
browser.find_element_by_id("AddToCart-product-template").click()
time.sleep(0.5)
# checkout page
browser.get("https://novelkeys.xyz/cart")
browser.find_element_by_name("checkout").click()
# make the sleep here dynamic, need to wait for the page to load before inputting information
isPresent = False
while not isPresent:
    try:
        isPresent = browser.find_element_by_id("checkout_email")
    except AttributeError as ae:
        isPresent = False
    isPresent = True


# contact info
browser.find_element_by_id("checkout_email").send_keys(email)
# firstname
browser.find_element_by_id("checkout_shipping_address_first_name").send_keys(fn)
# lastname
browser.find_element_by_id("checkout_shipping_address_last_name").send_keys(ln)
# address
browser.find_element_by_id("checkout_shipping_address_address1").send_keys(address)
# city
browser.find_element_by_id("checkout_shipping_address_city").send_keys(city)
# country
countryDropdown = Select(browser.find_element_by_id("checkout_shipping_address_country"))
countryDropdown.select_by_value("United States")
# state
stateDropdown = Select(browser.find_element_by_id("checkout_shipping_address_province"))
stateDropdown.select_by_value("CA")
# zip
browser.find_element_by_id("checkout_shipping_address_zip").send_keys(zip)
# phone
browser.find_element_by_id("checkout_shipping_address_phone").send_keys(phone)
browser.find_element_by_id("continue_button").click()

# shipping info
time.sleep(1.5) # make dynamic
browser.find_element_by_id("continue_button").click()

# billing info
time.sleep(0.5)
# card number
browser.find_element_by_xpath("iframe[@title='Field container for: Card number']").send_keys(cnum)
# name on card
browser.find_element_by_xpath("iframe[@title='Field container for: Name on card']").send_keys(nameOnCard)
# expiration
browser.find_element_by_xpath("iframe[@title='Field container for: Expiration date (MM / YY)']").send_keys(exp)
# SC
browser.find_element_by_xpath("iframe[@title='Field container for: Security code']").send_keys(sc)
