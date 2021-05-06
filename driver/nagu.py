from selenium import webdriver
from datetime import datetime
import time

driver = webdriver.Chrome('C:/Users/SESA536323/PycharmProjects/task123/driver/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(20)
driver.get('https://sso.eservices.jud.ct.gov/foreclosures/Public/PendPostbyTownList.aspx')

def get_todays_date():
    date = datetime.today().strftime('%m/%d/%Y')
    formatted_todays_date = date[0:10]
    return datetime.strptime(formatted_todays_date, '%m/%d/%Y')
