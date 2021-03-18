import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
import time
import pytest
from selenium.webdriver.support.select import Select


class Test_latent_view_home_page:

    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome("C:\\Users\\aleti1a\\Downloads\\chromedriver_win32\\chromedriver.exe")
        driver.get('http://latentview.com/')
        driver.implicitly_wait(15)
        driver.maximize_window()
        time.sleep(10)
        # close popup
        driver.find_element_by_xpath('//button[@id="onesignal-slidedown-cancel-button"]').click()
        time.sleep(3)
        # close subscribe
        driver.find_element_by_css_selector('div[id="enquirypopup"]>div>div>div>button').click()
        time.sleep(3)
        assert driver.title == 'Leading Digital Analytics Service Providers | LatentView'
        yield driver
        print("complted testcase execution")
        driver.close()

    def test01_hover_menu_items(self,driver):
        # mouse Hover
        act = ActionChains(driver)
        # mouse hover to Services
        act.move_to_element(driver.find_element_by_xpath('//li[@id="menu-item-9905"]/a')).perform()
        ls1 = driver.find_elements_by_xpath('//li[@id="menu-item-9905"]/ul/li')
        for i in ls1:
            print("Type in Services", i.text)
        time.sleep(5)

        # hover to Products
        act.move_to_element(driver.find_element_by_xpath('//li[@id="menu-item-9906"]/a')).perform()
        ls2 = driver.find_elements_by_xpath('//li[@id="menu-item-9906"]/ul/li')
        for i in ls2:
            print("Type in Products", i.text)
        time.sleep(5)

        # hover to Team x
        act.move_to_element(driver.find_element_by_xpath('//li[@id="menu-item-11073"]/a')).perform()
        ls2 = driver.find_elements_by_xpath('//li[@id="menu-item-11073"]/ul/li')
        for i in ls2:
            print("Type in Team", i.text)
        time.sleep(5)

        # hover to INSIGHTS
        act.move_to_element(driver.find_element_by_xpath('//li[@id="menu-item-10437"]')).perform()
        ls3 = driver.find_elements_by_xpath('//li[@id="menu-item-10437"]/ul/li')
        for i in ls3:
            print("Type in Insights", i.text)
        time.sleep(5)

        # hover to INNOVation
        act.move_to_element(driver.find_element_by_xpath('//li[@id="menu-item-2589"]')).perform()
        ls4 = driver.find_elements_by_xpath('//li[@id="menu-item-2589"]/ul/li')
        for i in ls4:
            print("Type in Innovation", i.text)
        time.sleep(5)



    def test02_blog(self,driver):
        driver.find_element_by_xpath('//*[@id="customid"]/header/div/div[3]/div/a[1]').click()
        time.sleep(3)
        w1 = driver.window_handles[0]
        w2 = driver.window_handles[1]
        driver.switch_to.window(w2)
        time.sleep(5)
        assert driver.title == 'Blogs on Data Science and Analytics | LatentView Analytics'
        time.sleep(5)
        driver.close()
        time.sleep(5)
        driver.switch_to.window(w1)
        time.sleep(5)






















