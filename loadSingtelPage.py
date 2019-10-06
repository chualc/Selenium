from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.singtel.com/personal/products-services/mobile/phones")

# Keep clicking 'Show more phones' button to list all the phones
while True:
    try:
        driver.find_element_by_css_selector('.ux-button.button.show-more-phones').click()
    except:
        break

catalogue = driver.find_elements_by_class_name("ux-catalogue-block")
for elem in catalogue:
    title = elem.find_element_by_class_name("product-title")
    dollar = elem.find_element_by_class_name("main-dollar")
    print(title.text, dollar.text)
    
driver.close()