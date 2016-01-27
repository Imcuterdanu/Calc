from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://jeremydomasian.github.io/supercalc_v1-4/SuperCalc-v2.html')

inputElem = browser.find_element_by_name('nine')
inputElem.click()

timesElem = browser.find_element_by_name('times')
timesElem.click()

nextElem = browser.find_element_by_name('nine')
nextElem.click()

outputElem = browser.find_element_by_name('DoIt')
outputElem.click()