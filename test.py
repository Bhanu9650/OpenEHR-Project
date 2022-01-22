import time 
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


BASE_URL = 'http://127.0.0.1:4005/'
USER_Email = 'abhi@gmail.com'
USER_PASSWORD = '123'
INVALID_USER_Email = 'adi2@gmail.com'
INVALID_PASSWORD = '123'
LOGIN_PAGE_TITLE = 'EAPR'
CHROME_PATH = '/usr/local/bin/chromedriver'
# dowload1-2
# driver = webdriver.Chrome(CHROME_PATH)
# driver.get(BASE_URL)
# driver.find_element_by_css_selector('#nav-menu > ul > li:nth-child(1) > a').click()
# time.sleep(5)
# driver.close()
testname="aaaa"
testemail='aaaa@gmail.com'
testpass="123"
testadd="noida 62"
testage=54
testgender="male"
testphone=9999391523
# driver.maximize_window()

class test(unittest.TestCase):
    def test_aavalid_login(self):
        
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--incognito")
        options = Options()
        options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox') # # Bypass OS security model
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")

        driver = webdriver.Chrome(CHROME_PATH,chrome_options=options)
        # driver = webdriver.Chrome(CHROME_PATH,chrome_options=chrome_options)

        # chrome_driver=driver.add_argument("--incognito")
        
        driver.get(BASE_URL)
        driver.find_element_by_xpath('//*[@id="home"]/div/div/button').click()
        driver.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(USER_Email)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(USER_PASSWORD)
        # time.sleep(1)
        #login_click
        driver.find_element_by_class_name('submit-btn').click()
        driver.maximize_window()
        driver.close()
    def test_invalid_login(self):
        options = Options()
        options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox') # # Bypass OS security model
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        # driver = webdriver.Chrome(CHROME_PATH)
        driver = webdriver.Chrome(CHROME_PATH,chrome_options=options)
        # driver = webdriver.Chrome(CHROME_PATH)
        driver.get(BASE_URL)
        #   browser = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
        #   browser.get(BASE_URL) 
        #   browser.maximize_window()
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="home"]/div/div/button').click()
        driver.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(INVALID_USER_Email)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(INVALID_PASSWORD)
        time.sleep(3)
        driver.find_element_by_class_name('submit-btn').click()
        time.sleep(3)
        driver.close()

        #patient_regiser
    def test_register_patient(self):
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options, executable_path="/usr/local/bin/geckodriver")
        
        # driver = webdriver.Chrome(CHROME_PATH)
        # driver.get(BASE_URL)
        #               # driver.find_element_by_css_selector('#nav-menu > ul > li:nth-child(1) > a').click()
        # driver.find_element_by_xpath('/html/body/header/nav/div[1]/ul/li[1]/a').click()
        # driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
        driver.get(BASE_URL) 
        driver.maximize_window()
        driver.find_element_by_xpath('/html/body/header/nav/div[1]/ul/li[1]/a').click()
        driver.find_element_by_name('uname').send_keys(testname)
        driver.find_element_by_name('mail').send_keys(testemail)
        driver.find_element_by_name('psw').send_keys(testpass)
        driver.find_element_by_name('age').send_keys(testage)
        driver.find_element_by_name('add').send_keys(testadd)
        driver.find_element_by_name('gen').send_keys(testgender)
        driver.find_element_by_name('phn').send_keys(testphone)
        time.sleep(2)
        # driver.find_element_by_xpath('/html/body/div/form/button').click()
        time.sleep(5)
        driver.close()
    def test_register_doc(self):
        dtestname="aaab"
        dtestemail='aaab@gmail.com'
        dtestpass="123"
        dtestadd="noida 62"
        dtestyoe=12
        dtestspl="phycharcist"
        dtestphone=9999291523
        dtestfee=1234
        dtestdesc="description"
        # driver = webdriver.Chrome(CHROME_PATH)
        # driver.get(BASE_URL)
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options, executable_path="/usr/local/bin/geckodriver")
        # driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
        driver.get(BASE_URL) 
        driver.maximize_window()
        # driver.find_element_by_css_selector('#nav-menu > ul > li:nth-child(2) > a').click()
        driver.find_element_by_xpath('/html/body/header/nav/div[1]/ul/li[2]/a').click()
        driver.find_element_by_name('uname').send_keys(dtestname)
        driver.find_element_by_name('mail').send_keys(dtestemail)
        driver.find_element_by_name('psw').send_keys(dtestpass)
        driver.find_element_by_name('add').send_keys(dtestadd)
        driver.find_element_by_name('yoe').send_keys(dtestyoe)
        driver.find_element_by_name('spl').send_keys(dtestspl)
        driver.find_element_by_name('phn').send_keys(dtestphone)
        driver.find_element_by_name('fee').send_keys(dtestfee)
        driver.find_element_by_name('desc').send_keys(dtestdesc)
        time.sleep(2)
        #---- driver.find_element_by_xpath('/html/body/form/div/div/button/span').click()
        # driver.find_element_by_xpath('/html/body/div/form/button/span').click()
        time.sleep(5)
        driver.close()
    def test_register_pharma(self):
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options, executable_path="/usr/local/bin/geckodriver")
        # driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
        driver.get(BASE_URL) 
        driver.maximize_window()
        pharma_testname="abc"
        pharma_testemail='abc@gmail.com'
        pharma_testpass="123"
        pharma_testadd="noida 62"
        pharma_testyoe=12
        pharma_testphone=9999991523
        pharma_rn=1234
        # driver = webdriver.Chrome(CHROME_PATH)
        # driver.get(BASE_URL)
                   # driver.find_element_by_css_selector('#nav-menu > ul > li:nth-child(3) > a').click()
        driver.find_element_by_xpath('/html/body/header/nav/div[1]/ul/li[3]/a').click()
        driver.find_element_by_name('uname').send_keys(pharma_testname)
        driver.find_element_by_name('mail').send_keys(pharma_testemail)
        driver.find_element_by_name('psw').send_keys(pharma_testpass)
        driver.find_element_by_name('add').send_keys(pharma_testadd)
        driver.find_element_by_name('yoe').send_keys(pharma_testyoe)
        driver.find_element_by_name('phn').send_keys(pharma_testphone)
        driver.find_element_by_name('rn').send_keys(pharma_rn)
        time.sleep(3)
        #----- driver.find_element_by_xpath('/html/body/form/div/div/button/span').click()
        driver.find_element_by_xpath('/html/body/div/form/button/span').click
        time.sleep(2)
        driver.close()
    def test_about(self):
        options = Options()
        options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox') # # Bypass OS security model
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        driver = webdriver.Chrome(CHROME_PATH,chrome_options=options)
        driver.get(BASE_URL)
        # driver.find_element_by_css_selector('#nav-menu > ul > li:nth-child(5) > a').click()
        driver.find_element_by_xpath('/html/body/header/nav/div[1]/ul/li[4]/a').click()
        time.sleep(3)
        driver.close()
    # def test_moon(self):
    #     driver = webdriver.Chrome(CHROME_PATH)
    #     driver.get(BASE_URL)
    #     driver.find_element_by_id('theme-button').click()
    #     time.sleep(3)
    #     driver.close()
 

    
        
        # driver.find_element_by_xpath('//*[@id="example-basic"]/section/div/div/table/tbody/tr[2]/td[6]/form/button').click()
    def test_patient_view(self):
        # time.sleep(2)
        options = Options()
        options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox') # # Bypass OS security model
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        driver = webdriver.Chrome(CHROME_PATH,chrome_options=options)
        driver.get(BASE_URL)
        driver.find_element_by_xpath('//*[@id="home"]/div/div/button').click()
        driver.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(USER_Email)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(USER_PASSWORD)
        # time.sleep(1)
        #login_click
        driver.find_element_by_class_name('submit-btn').click()
        #logout
        # driver.find_element_by_xpath('//*[@id="nav-menu"]/ul/li[5]/a').click()
        #profile
        driver.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[2]/a/span').click()
        time.sleep(1)
        driver.close()
    def test_doctor_logout(self):
        docmail='jagdish@gmail.com'
        options = Options()
        options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox') # # Bypass OS security model
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        driver = webdriver.Chrome(CHROME_PATH,chrome_options=options)
        driver.get(BASE_URL)
        driver.find_element_by_xpath('//*[@id="home"]/div/div/button').click()
        driver.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(docmail)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(USER_PASSWORD)
        # time.sleep(1)
        #login_click
        

        driver.find_element_by_class_name('submit-btn').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="nav-menu"]/ul/li[5]/a').click()
        time.sleep(2)
        driver.close()
    def test_patient_homeview(self):
        options = Options()
        options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox') # # Bypass OS security model
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        driver = webdriver.Chrome(CHROME_PATH,chrome_options=options)
        driver.get(BASE_URL)
        #back_to_home to view
        driver.find_element_by_xpath('//*[@id="home"]/div/div/button').click()
        driver.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(USER_Email)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(USER_PASSWORD)
        # time.sleep(1)
        #login_click
        driver.find_element_by_class_name('submit-btn').click()
        driver.find_element_by_xpath('//*[@id="nav-menu"]/ul/li[1]/a').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="example-basic"]/section/div/div/table/tbody/tr[2]/td[6]/form/button').click()
        time.sleep(2)
        driver.close()
    # def test_patient_logout(self):
    #     driver = webdriver.Chrome(CHROME_PATH)
    #     driver.get(BASE_URL)
        
    #      #logout
    #     driver.find_element_by_xpath('//*[@id="nav-menu"]/ul/li[5]/a').click()
    #     time.sleep(1)
    #     time.sleep(2)
    #     driver.close()
    def test_patient_logout(self):
        options = Options()
        options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox') # # Bypass OS security model
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        driver = webdriver.Chrome(CHROME_PATH,chrome_options=options)
        driver.get(BASE_URL)
        driver.find_element_by_xpath('//*[@id="home"]/div/div/button').click()
        driver.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(USER_Email)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(USER_PASSWORD)
        driver.find_element_by_xpath('/html/body/div/form/input').click()
         #logout
        driver.find_element_by_xpath('//*[@id="nav-menu"]/ul/li[3]/a').click()
        time.sleep(1)
        time.sleep(2)
        driver.close()
  
   
    def testmodule_doctor_login(self):
        #docter login 
        # browser = webdriver.Firefox(executable_path="./drivers/geckodriver")
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(options=options, executable_path="/usr/local/bin/geckodriver")
        # browser = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
        browser.get(BASE_URL) 
        browser.maximize_window()
        # browser = webdriver.Chrome(CHROME_PATH)
        # browser = webdriver.Chrome(CHROME_PATH)
        # browser.get(BASE_URL)
        docmail='jagdish@gmail.com'
        browser.find_element_by_xpath('//*[@id="home"]/div/div/button').click()
        browser.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(docmail)
        browser.find_element_by_xpath('//*[@id="password"]').send_keys(USER_PASSWORD)
        browser.find_element_by_class_name('submit-btn').click()
        time.sleep(2)
        #home->view_here
        browser.find_element_by_xpath('//*[@id="example-basic"]/section/div/div/table/tbody/tr[2]/td[6]/form/button').click()
        time.sleep(3)
        #home->patient
        browser.find_element_by_xpath('//*[@id="nav-menu"]/ul/li[1]/a').click()
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[2]/a/span').click()
        time.sleep(3)
        #click_to_view_summary
        browser.find_element_by_xpath('//*[@id="example-basic"]/section/div/div/table/tbody/tr[4]/td[6]/form/button').click()
        time.sleep(8)
        #to_download_prescription
        browser.find_element_by_xpath('//*[@id="cmd"]').click()
        time.sleep(8)
        print("hello")
        time.sleep(1)
        browser.close()
    def test_prescribe(self):
        # new_browser = webdriver.Chrome(CHROME_PATH)
        options = Options()
        options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox') # # Bypass OS security model
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        new_browser = webdriver.Chrome(CHROME_PATH,chrome_options=options)
        # new_browser = webdriver.Chrome(CHROME_PATH,chrome_options=options)
        new_browser.get(BASE_URL) 
        new_browser.maximize_window()
        docmail='jagdish@gmail.com'
        new_browser.find_element_by_xpath('//*[@id="home"]/div/div/button').click()
        new_browser.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(docmail)
        new_browser.find_element_by_xpath('//*[@id="password"]').send_keys(USER_PASSWORD)
        new_browser.find_element_by_class_name('submit-btn').click()
        time.sleep(2)
        new_browser.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[3]/a/span').click()
        time.sleep(3)
        new_browser.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[4]/a').click()
        time.sleep(3)
        #prescribe_tab1
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/a/button/img').click()
        time.sleep(3)
        new_browser.close()
    def test_pastillness_history(self):
        # browser.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[4]/a').click()
        # time.sleep(2)
        #enter_fields
        options = Options()
        options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox') # # Bypass OS security model
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        new_browser = webdriver.Chrome(CHROME_PATH,chrome_options=options)
        # new_browser = webdriver.Chrome(CHROME_PATH)
        new_browser.get(BASE_URL) 
        new_browser.maximize_window()
        docmail='jagdish@gmail.com'
        new_browser.find_element_by_xpath('//*[@id="home"]/div/div/button').click()
        new_browser.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(docmail)
        new_browser.find_element_by_xpath('//*[@id="password"]').send_keys(USER_PASSWORD)
        new_browser.find_element_by_class_name('submit-btn').click()
        time.sleep(2)
        new_browser.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[3]/a/span').click()
        time.sleep(3)
        new_browser.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[4]/a').click()
        time.sleep(3)
        #prescribe_tab1
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/a/button/img').click()
        time.sleep(3)
        id=1
        new_browser.find_element_by_xpath('//html/body/div[2]/div/div/div/div[2]/form/div/div[1]/div/input').send_keys(id)
        time.sleep(3)
        problem='Nausea'
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[2]/div/input').send_keys(problem)
        site='nose'
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[3]/div/input').send_keys(site)
        time.sleep(5)
        # new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[3]/div/input').send_keys(Keys.TAB)
        # new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[4]/div/input').send_keys('12')
        # new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[4]/div/input').send_keys('12')
        # new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[4]/div/input').send_keys('2012')
        # new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[4]/div/input').send_keys(Keys.TAB)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[4]/div/input').send_keys('20/01/2022')
        # browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[4]/div/input').send_keys('20/01/2022')
        time.sleep(3)
        # browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[4]/div/input').send_keys(date)
        # time.sleep(3)
        # browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[4]/div/input').send_keys('20012022')


        time.sleep(3)
        severity='moderate'
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[5]/div/input').send_keys(severity)
        procedure='xyz'
        # /html/body/div[2]/div/div/div/div[2]/form/div/div[6]/div/input
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[6]/div/input').send_keys(procedure)
        time.sleep(4)
        # browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[4]/div/input').click()
        time.sleep(3)
        new_browser.close()
    def test_allergyintolerence(self):
        options = Options()
        options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox') # # Bypass OS security model
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        new_browser = webdriver.Chrome(CHROME_PATH,chrome_options=options)
        # new_browser = webdriver.Chrome(CHROME_PATH)
        new_browser.get(BASE_URL) 
        new_browser.maximize_window()
        docmail='jagdish@gmail.com'
        
        new_browser.find_element_by_xpath('//*[@id="home"]/div/div/button').click()
        new_browser.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(docmail)
        new_browser.find_element_by_xpath('//*[@id="password"]').send_keys(USER_PASSWORD)
        new_browser.find_element_by_class_name('submit-btn').click()
        time.sleep(2)
        
        new_browser.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[3]/a/span').click()
        time.sleep(3)
        new_browser.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[4]/a').click()
        time.sleep(3)
        #prescribe_tab1
        # new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/a/button/img').click()
        time.sleep(3)
        #prescribe_tab2 
        new_browser.find_element_by_xpath('/html/body/div[1]/nav/div[3]/nav/ul/li/ul/li[4]/a/span').click()
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/a/button/img').click()
        time.sleep(3)
        id=1
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[1]/div/input').send_keys(id)
        time.sleep(3)
        substance='smoke'
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[2]/div/input').send_keys(substance)
        time.sleep(3)
        verification_status='confirm'
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[3]/div/input').send_keys(verification_status)
        intolerance='moderate'
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[4]/div/input').send_keys(intolerance)
        comment='be strict with doses'
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[5]/div/input').send_keys(comment)
        manifestation='red nose'
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[6]/div/input').send_keys(manifestation)
        time.sleep(3)
        new_browser.find_element_by_xpath('//*[@id="myForm4"]/div/div[7]/button').click()
        time.sleep(2)



        new_browser.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[4]/a').click()
        time.sleep(3)
        new_browser.close()
    
    def test_problem_diag(self):
        options = Options()
        options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox') # # Bypass OS security model
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        new_browser = webdriver.Chrome(CHROME_PATH,chrome_options=options)
        # new_browser = webdriver.Chrome(CHROME_PATH)
        new_browser.get(BASE_URL) 
        new_browser.maximize_window()
        docmail='jagdish@gmail.com'
        new_browser.find_element_by_xpath('//*[@id="home"]/div/div/button').click()
        new_browser.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(docmail)
        new_browser.find_element_by_xpath('//*[@id="password"]').send_keys(USER_PASSWORD)
        new_browser.find_element_by_class_name('submit-btn').click()
        time.sleep(2)
        new_browser.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[3]/a/span').click()
        time.sleep(3)
        new_browser.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[4]/a').click()
        time.sleep(3)
        #prescribe_tab1
        # new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/a/button/img').click()
        # time.sleep(3)
        #prescribe_tab3
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/a/button/img').click()
        time.sleep(3)
        id=1
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[1]/div/input').send_keys(id)
        time.sleep(3)
        problem='Nausea'
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[2]/div/input').send_keys(problem)
        site='nose'
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[3]/div/input').send_keys(site)
        time.sleep(5)

        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[4]/div/input').send_keys('20/01/2022')


        time.sleep(3)
        severity='moderate'
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[5]/div/input').send_keys(severity)
        procedure='xyz'

        new_browser.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[4]/a/span').click()
        time.sleep(3)
        new_browser.close()
    
    def test_eprescription(self):
        options = Options()
        options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox') # # Bypass OS security model
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        new_browser = webdriver.Chrome(CHROME_PATH,chrome_options=options)
        # new_browser = webdriver.Chrome(CHROME_PATH)
        new_browser.get(BASE_URL) 
        new_browser.maximize_window()
        docmail='jagdish@gmail.com'
        new_browser.find_element_by_xpath('//*[@id="home"]/div/div/button').click()
        new_browser.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(docmail)
        new_browser.find_element_by_xpath('//*[@id="password"]').send_keys(USER_PASSWORD)
        new_browser.find_element_by_class_name('submit-btn').click()
        time.sleep(2)
        new_browser.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[4]/a/span').click()
        time.sleep(3)
        new_browser.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[4]/a').click()
        time.sleep(3)
        #prescribe_tab1
        # new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/a/button/img').click()
        # time.sleep(3)
        
        #prescribe_tab4
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div[4]/a/button/img').click()
        time.sleep(3)
        # new_browser.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[1]/a').click()
        # time.sleep(3)
        ###########
        
        id=1
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[1]/div/input').send_keys(id)
        time.sleep(2)
        medication_term='nausea'
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[2]/div/input').send_keys(medication_term)
        route='xyz'
        time.sleep(2)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[3]/div/input').send_keys(route)
        dosage_instru='twice'
        time.sleep(2)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[4]/div/input').send_keys(dosage_instru)
        additional_instruction='be strict with doses'
        time.sleep(2)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[5]/div/input').send_keys(additional_instruction)
        reason='normal viral'
        time.sleep(2)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[6]/div/input').send_keys(reason)
        dose='dolo 650'
        time.sleep(2)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[7]/div/input').send_keys(dose)
        dose_unit='2'
        time.sleep(2)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[8]/div/input').send_keys(dose_unit)
        frequency=2
        time.sleep(2)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[9]/div/input').send_keys(frequency)
        status='active'
        time.sleep(2)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[10]/div/input').send_keys(status)
        time.sleep(2)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[11]/div/input').send_keys('25/01/2022')
        time.sleep(2)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[12]/div/input').send_keys('20/01/2022')
        time.sleep(2)
        # new_browser('//*[@id="menu1"]/li/ul/li[1]/a').click()
        time.sleep(4)
        #logout
        
        # new_browser.find_element_by_xpath('//*[@id="myForm"]/div/div[13]/button').click()
        time.sleep(1)
        time.sleep(2)
        new_browser.close()
        
    #     # <a href="/" class="nav__link">Logout</a>
        
   
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='local_host'))