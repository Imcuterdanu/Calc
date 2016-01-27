from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://jeremydomasian.github.io/supercalc_v1-4/SuperCalc-v2.html')

InputElem = browser.find_element_by_name('nine')
InputElem.click()

InputElem = browser.find_element_by_name('clear')
InputElem.click()