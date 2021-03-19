from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import pytest
from selenium.webdriver.common.keys import Keys


class Test_latent_view_home_page:

    #Fixture method, will execute before and after each test case
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
        driver.find_element_by_css_selector('div[id="enquirypopup"]>div>div>div>button').click()  #css selector
        time.sleep(3)
        assert driver.title == 'Leading Digital Analytics Service Providers | LatentView'
        yield driver
        driver.close()

    # @pytest.mark.skip
    #Hover menu items of the home page and printing sub menus inside them
    def test01_hover_menu_items(self,driver):
        # mouse Hover
        act = ActionChains(driver)
        # mouse hover to Services
        act.move_to_element(driver.find_element_by_id('menu-item-9905')).perform()  #By ID
        ls1 = driver.find_elements_by_xpath('//li[@id="menu-item-9905"]/ul/li')
        for i in ls1:
            print("Type in Services", i.text)
        time.sleep(5)

        # hover to Products
        act.move_to_element(driver.find_element_by_xpath('//li[@id="menu-item-9906"]/a')).perform()  #by XPATH
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

    #Checking the privacy policy page
    def test02_check_privacy_policy(self,driver):
        # Link text
        driver.find_element_by_link_text('privacy policy.').click()     #link text
        driver.implicitly_wait(20)
        time.sleep(5)
        w1 = driver.window_handles[0]
        w2 = driver.window_handles[1]
        driver.switch_to.window(w2)
        time.sleep(10)
        assert driver.title == 'Privacy Policy - Latentview'
        driver.close()
        driver.switch_to.window(w1)
        time.sleep(5)

        #To go footer
        driver.find_element_by_tag_name('html').send_keys(Keys.END)   #by Tag name
        time.sleep(5)

        #Check partial link
        ele=driver.find_element_by_partial_link_text('Privacy').is_displayed()  # by partial link text
        if ele==True:
            print("Partial link text found successfully")
        time.sleep(5)

        #click on enquiry
        driver.find_element_by_xpath('//*[@id="customid"]/section/button[2]').click()
        time.sleep(5)
        driver.find_element_by_name('input_1.3').send_keys('adithya')           #find element by name
        time.sleep(3)
        #close
        driver.find_element_by_xpath('(//div[@id="myModal"]/div)[1]/div/div/button').click()
        time.sleep(5)
























