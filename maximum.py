from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://jeremydomasian.github.io/supercalc_v1-4/SuperCalc-v2.html')

InputElem = browser.find_element_by_name('nine')
count = 0
while(count < 20):
	InputElem.click()
	count = count + 1