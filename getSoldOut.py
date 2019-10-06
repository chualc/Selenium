# https://www.fortytwo.sg/dining/dining-tables.html

from selenium import webdriver
import time

# Credit: https://stackoverflow.com/questions/48850974/selenium-scroll-to-end-of-page-indynamically-loading-webpage
def scroll_down(driver):
    """A method for scrolling the page."""

    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:

        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break

        last_height = new_height
        
        
driver = webdriver.Chrome()
driver.get("https://www.fortytwo.sg/dining/dining-tables.html")

scroll_down(driver)  # wait for the website to load the page

html_list = driver.find_element_by_id("catalog-listing")
items = html_list.find_elements_by_tag_name("li")

count = 0
total = 0
print("Items that are sold out - generating the list takes a while")
for item in items:
    total += 1
    if 'Sold Out' in item.text:
        # html content = item.get_attribute("innerHTML")  # display html content
        
        div = item.find_element_by_class_name('item-info')
        title = div.find_element_by_css_selector('a').get_attribute('title')      
        count += 1
        print(count, title)
        
driver.close()
print(count,"out of", total, "items are sold out")
