from selenium import webdriver

url = 'http://www.jd.com/'
browser=webdriver.Chrome()
browser.get(url)
# content=browser.page_source
# print(content)
button=browser.find.element_by_name('wd')