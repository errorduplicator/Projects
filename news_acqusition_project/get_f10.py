from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
import time
import re
import pandas as pd

list_ = open('list.txt','r')
events = []
links = []
data = {'event' : events,
        'link' : links}
driver = webdriver.Chrome()
lines = list_.readlines()
for line in range(5362):    
    code = lines[line]
    driver.get(''.join(['https://basic.10jqka.com.cn/', code, '/news.html']))

    driver.implicitly_wait(10)
    m_box_subnews = driver.find_element(By.ID, "pub")
    page_link_box = m_box_subnews.find_element(By.ID, "splpager_page")
    page_links = page_link_box.find_elements(By.CLASS_NAME, "page-link")
    next_page = page_links[-1]
    for page in range(1, 20):
        driver.implicitly_wait(3)
        m_box_subnews = driver.find_element(By.ID, "pub")
        page_link_box = m_box_subnews.find_element(By.ID, "splpager_page")
        page_links = page_link_box.find_elements(By.CLASS_NAME, "page-link")
        next_page = page_links[-1]
        elements = m_box_subnews.find_elements(By.CLASS_NAME, "client")
        for element in elements:
            WebDriverWait(driver, 30, ignored_exceptions=(NoSuchElementException,StaleElementReferenceException)).until(EC.element_to_be_clickable(element))
            event_name = element.text
            keywords = ['证监会', '中国证券监督管理委员会', '罚', '退市']
            combined_pattern = '|'.join(keywords)
            matches = re.findall(combined_pattern, event_name)
            if matches:
                link = element.get_attribute('href')
                events.append(event_name + '\n')
                links.append(link + '\n')
        WebDriverWait(driver, 40, ignored_exceptions=(NoSuchElementException,StaleElementReferenceException)).until(EC.element_to_be_clickable(next_page))
        next_page.click()
        time.sleep(3)
        print(page)
df = pd.DataFrame(data)
df.to_excel('a.xlsx', index=False, header=False)
driver.quit()
