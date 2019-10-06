# https://buildmedia.readthedocs.org/media/pdf/selenium-python/latest/selenium-python.pdf

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://shopee.sg/Apple-iphone-6s-Plus-64GB-%EF%BC%88DEMO-SET-SG-1-month-warranty-)-i.27987240.2187574237")

elem = driver.find_element_by_css_selector('div._3n5NQx')
print(elem.text)

