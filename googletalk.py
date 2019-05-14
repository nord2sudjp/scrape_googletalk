from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(".\chromedriver")
#driver = webdriver.PhantomJS()
driver.get('https://books.google.com/talktobooks/query')

assert 'Books' in driver.title

input_element = driver.find_element_by_name('queryString')
input_element.send_keys('Python')
input_element.send_keys(Keys.RETURN)

sleep(2)
assert 'Passages' in driver.page_source
driver.save_screenshot('search_result.png')

for a in driver.find_elements_by_css_selector('#main-content > query-page > div > section > div > div > div.snippet-container > div > blockquote'):
  print(a.text)
  print('='*20)
 