from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://jeremydomasian.github.io/supercalc_v1-4/SuperCalc-v2.html')

inputElem = browser.find_element_by_name('Input')
inputElem.click()
number = ('123+22')
inputElem = send_keys(number)
