from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.keys import Keys
class task:
    def var(self):
     browser = webdriver.Chrome('C:/Users/SESA536323/PycharmProjects/task123/driver/chromedriver.exe')
     browser.get("https://sso.eservices.jud.ct.gov/foreclosures/Public/PendPostbyTownList.aspx")
     browser.maximize_window()
     browser.refresh()
     time.sleep(10)
     btn = browser.find_element_by_link_text("New Milford")
     browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
     btn.click()
     b1 = datetime.date.today()
     print(b1)
     b2 = datetime.datetime.now() + datetime.timedelta(days=7)
     print(b2)
     b3= browser.find_element_by_id("ctl00_cphBody_GridView1_ctl02_Label1").text
     print(b3)
     #Select date = new Select(driver.findElement(By.linkText("the date want to select")));
     #date.click();
     #if ndate > saledate :
     #print(saledate)

     #if b2 > b3 :
      #print(b3)
task.var(object)