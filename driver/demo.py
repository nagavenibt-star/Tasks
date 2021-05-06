from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

var_path = os.path.abspath(os.getcwd())
print(var_path)
driver = webdriver.Chrome(var_path + '/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(20)
driver.get('https://sso.eservices.jud.ct.gov/foreclosures/Public/PendPostbyTownList.aspx')


def get_todays_date():
    date = datetime.today().strftime('%m/%d/%Y')
    formatted_todays_date = date[0:10]
    return datetime.strptime(formatted_todays_date, '%m/%d/%Y')


cities = ['New Milford','Trumbull', 'Norwalk','Stamford', 'Shelton', 'Fairfield']

for city in cities:
    try:

        driver.find_element_by_link_text(city).click()
        notice_links = driver.find_elements_by_xpath("//a[contains(@href,'PendPostDetailPublic.aspx?PostingId')]")
        record_date_fields = \
            driver.find_elements_by_xpath("//a[contains(@href,'PendPostDetailPublic.aspx?PostingId')]"
                                          "/ancestor::tr[@style='color:Black;background-color:#DEDFDE;']//td[2]/span")
        for notice in range(0, len(notice_links)):
            record_date = record_date_fields[notice].text
            formatted_record_date = record_date[0:10]
            record_date_in_date_format = datetime.strptime(formatted_record_date, '%m/%d/%Y')

            if (record_date_in_date_format - get_todays_date()).days <= 7:
                print('Sale is within 7 days')
                href = notice_links[notice].get_attribute('href')
                driver.execute_script("window.open('"+href+"');")
                driver.switch_to.window(driver.window_handles[0])

            else:
                print('Sale is NOT within 7 days')
                href = notice_links[notice].get_attribute('href')
                driver1 = webdriver.Chrome(var_path + '/chromedriver.exe')
                driver1.get(href)
                #driver1.execute_script("window.open('"+href+"');")
                #driver1.switch_to.window(driver.window_handles[0])
                #driver.execute_script("window.open('"+href+"');")
                #driver1.switch_to.window(driver.window_handles[0])

        driver.get("https://sso.eservices.jud.ct.gov/Foreclosures/Public/PendPostbyTownList.aspx")
    except NoSuchElementException:
        print('City  {0} Not Found'.format(city))



