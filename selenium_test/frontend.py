from filecmp import cmp
from lib2to3.pgen2.token import COMMENT
import time 
import unittest
import pytest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


CHROME_PATH = '/usr/local/bin/chromedriver'


BASE_URL = 'http://15.207.115.222/'
USER_Email = 'adi@gmail.com'
USER_PASSWORD = '123'
INVALID_USER_Email = 'adi2@gmail.com'
INVALID_PASSWORD = '123'
LOGIN_PAGE_TITLE = 'EAPR'
TEST_NAME="abc"
TEST_EMAIL='abc@gmail.com'
TEST_PASS="123"
TEST_ADDRESS="noida 62"
TEST_AGE=54
TEST_GENDER="male"
TEST_PHONE=9999391523

class test(unittest.TestCase):

    # Test Invalid Login
    @pytest.mark.run(order=1)
    def test_invalid_login(self):
       
        driver = webdriver.Chrome(CHROME_PATH)
        driver.get(BASE_URL)
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="home"]/div/div/button').click()
        driver.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(INVALID_USER_Email)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(INVALID_PASSWORD)
        time.sleep(3)
        driver.find_element_by_class_name('submit-btn').click()
        time.sleep(3)
        driver.close()

    # Test Patient Register
    @pytest.mark.run(order=2)
    def test_register_patient(self):
        TEST_NAME="abcee"
        TEST_EMAIL='ab33cs@gmail.com'
        TEST_PASS="123"
        TEST_ADDRESS="noida 62"
        TEST_AGE=54
        TEST_GENDER="male"
        TEST_PHONE=9939391523
        
        driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
        driver.get(BASE_URL) 
        driver.maximize_window()
        driver.find_element_by_xpath('/html/body/header/nav/div[1]/ul/li[1]/a').click()
        driver.find_element_by_name('uname').send_keys(TEST_NAME)
        driver.find_element_by_name('mail').send_keys(TEST_EMAIL)
        driver.find_element_by_name('psw').send_keys(TEST_PASS)
        driver.find_element_by_name('age').send_keys(TEST_AGE)
        driver.find_element_by_name('add').send_keys(TEST_ADDRESS)
        driver.find_element_by_name('gen').send_keys(TEST_GENDER)
        driver.find_element_by_name('phn').send_keys(TEST_PHONE)
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div/form/button/span').click()
        time.sleep(5)
        driver.close()

    # Test Doctor Registration
    @pytest.mark.run(order=3)
    def test_register_doctor(self):
        dTEST_NAME="aaaba"
        dTEST_EMAIL='aaa33bs@gmail.com'
        dTEST_PASS="1232"
        dTEST_ADDRESS="noida 62"
        dTEST_YOE=12
        dTEST_SPECIALIST="phycharcist"
        dTEST_PHONE=9999291523
        dTEST_FEE=1234
        dTEST_DESCRIPTION="description"

        driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
        driver.get(BASE_URL) 
        driver.maximize_window()
        driver.find_element_by_xpath('/html/body/header/nav/div[1]/ul/li[2]/a').click()
        driver.find_element_by_name('uname').send_keys(dTEST_NAME)
        driver.find_element_by_name('mail').send_keys(dTEST_EMAIL)
        driver.find_element_by_name('psw').send_keys(dTEST_PASS)
        driver.find_element_by_name('add').send_keys(dTEST_ADDRESS)
        driver.find_element_by_name('yoe').send_keys(dTEST_YOE)
        driver.find_element_by_name('spl').send_keys(dTEST_SPECIALIST)
        driver.find_element_by_name('phn').send_keys(dTEST_PHONE)
        driver.find_element_by_name('fee').send_keys(dTEST_FEE)
        driver.find_element_by_name('desc').send_keys(dTEST_DESCRIPTION)
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div/form/button/span').click()
        time.sleep(5)
        driver.close()
    
    @pytest.mark.run(order=4)
    # Test Pharmacist Registration   
    def test_register_pharmasist(self):
        driver = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
        driver.get(BASE_URL) 
        driver.maximize_window()

        pharma_TEST_NAME="abch"
        pharma_TEST_EMAIL='abce35s@gmail.com'
        pharma_TEST_PASS="123"
        pharma_TEST_ADDRESS="noida 62"
        pharma_TEST_YOE=12
        pharma_TEST_PHONE=9599991523
        pharma_rn=1234


        driver.find_element_by_xpath('/html/body/header/nav/div[1]/ul/li[3]/a').click()
        driver.find_element_by_name('uname').send_keys(pharma_TEST_NAME)
        driver.find_element_by_name('mail').send_keys(pharma_TEST_EMAIL)
        driver.find_element_by_name('psw').send_keys(pharma_TEST_PASS)
        driver.find_element_by_name('add').send_keys(pharma_TEST_ADDRESS)
        driver.find_element_by_name('yoe').send_keys(pharma_TEST_YOE)
        driver.find_element_by_name('phn').send_keys(pharma_TEST_PHONE)
        driver.find_element_by_name('rn').send_keys(pharma_rn)
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div/form/button/span').click()
        
        time.sleep(2)
        driver.close()

    @pytest.mark.run(order=5)
    # Test About Us 
    def test_about(self):
    

        driver = webdriver.Chrome(CHROME_PATH)
        driver.get(BASE_URL)
        driver.find_element_by_xpath('/html/body/header/nav/div[1]/ul/li[4]/a').click()
        time.sleep(3)
        driver.close()

    @pytest.mark.run(order=6)
    # Test Valid Patient Login
    def test_patient_valid_login(self):
        driver = webdriver.Chrome(CHROME_PATH)
        driver.get(BASE_URL)
        driver.find_element_by_xpath('//*[@id="home"]/div/div/button').click()
        driver.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(USER_Email)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(USER_PASSWORD)
        driver.find_element_by_class_name('submit-btn').click()
        driver.maximize_window()
        driver.close()
        
    # Test Invalid Patient Login
    @pytest.mark.run(order=7)
    def test_patient_invalid_login(self):
       
        driver = webdriver.Chrome(CHROME_PATH)
        driver.get(BASE_URL)
        driver.find_element_by_xpath('//*[@id="home"]/div/div/button').click()
        driver.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(USER_Email)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(USER_PASSWORD)

        driver.find_element_by_class_name('submit-btn').click()

        driver.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[2]/a/span').click()
        time.sleep(1)
        driver.close()


    # Test Doctor Logout
    @pytest.mark.run(order=8)
    def test_doctor_logout(self):
        DOCTOR_EMAIL='jagdish@gmail.com'
       
        driver = webdriver.Chrome(CHROME_PATH)
        driver.get(BASE_URL)
        driver.find_element_by_xpath('//*[@id="home"]/div/div/button').click()
        driver.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(DOCTOR_EMAIL)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(USER_PASSWORD)
        driver.find_element_by_class_name('submit-btn').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="nav-menu"]/ul/li[5]/a').click()
        time.sleep(2)
        driver.close()
    
    # Test Patient Dashboard
    @pytest.mark.run(order=9)
    def test_patient_homeview(self):
   
        driver = webdriver.Chrome(CHROME_PATH)
        driver.get(BASE_URL)
        driver.find_element_by_xpath('//*[@id="home"]/div/div/button').click()
        driver.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(USER_Email)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(USER_PASSWORD)

        driver.find_element_by_class_name('submit-btn').click()
        driver.find_element_by_xpath('//*[@id="nav-menu"]/ul/li[1]/a').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="example-basic"]/section/div/div/table/tbody/tr[2]/td[6]/form/button').click()
        time.sleep(2)
        driver.close()

    # Test Valid Patient Logout
    @pytest.mark.run(order=10)
    def test_patient_logout(self):

        driver = webdriver.Chrome(CHROME_PATH)
        driver.get(BASE_URL)
        driver.find_element_by_xpath('//*[@id="home"]/div/div/button').click()
        driver.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(USER_Email)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(USER_PASSWORD)
        driver.find_element_by_xpath('/html/body/div/form/input').click()
        driver.find_element_by_xpath('//*[@id="nav-menu"]/ul/li[3]/a').click()
        time.sleep(1)
        time.sleep(2)
        driver.close()
  
    # Test to download prescription for Doctor
    @pytest.mark.run(order=11)
    def testmodule_doctor_prescription(self):

        browser = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
        browser.get(BASE_URL) 
        browser.maximize_window()

        DOCTOR_EMAIL='jagdish@gmail.com'
        browser.find_element_by_xpath('//*[@id="home"]/div/div/button').click()
        browser.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(DOCTOR_EMAIL)
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
    
   # Test to check prescription tab in Doctor Dashboard
    @pytest.mark.run(order=12)
    def test_prescribe(self):
 
        new_browser = webdriver.Chrome(CHROME_PATH)
        new_browser.get(BASE_URL) 
        new_browser.maximize_window()

        DOCTOR_EMAIL='jagdish@gmail.com'

        new_browser.find_element_by_xpath('//*[@id="home"]/div/div/button').click()
        new_browser.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(DOCTOR_EMAIL)
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

   # Test to write Past Illness in Doctor Dashboard
    @pytest.mark.run(order=13)
    def test_pastillness_history(self):

        new_browser = webdriver.Chrome(CHROME_PATH)
        new_browser.get(BASE_URL) 
        new_browser.maximize_window()
        DOCTOR_EMAIL='jagdish@gmail.com'
        new_browser.find_element_by_xpath('//*[@id="home"]/div/div/button').click()
        new_browser.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(DOCTOR_EMAIL)
        new_browser.find_element_by_xpath('//*[@id="password"]').send_keys(USER_PASSWORD)
        new_browser.find_element_by_class_name('submit-btn').click()
        time.sleep(2)
        new_browser.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[3]/a/span').click()
        time.sleep(3)
        new_browser.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[4]/a').click()
        time.sleep(3)

        ID=1
        PROBLEM='Nausea'
        SITE='nose'
        SEVERITY='moderate'
        PROCEDURE='xyz'


        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/a/button/img').click()
        time.sleep(3)
        new_browser.find_element_by_xpath('//html/body/div[2]/div/div/div/div[2]/form/div/div[1]/div/input').send_keys(ID)
        time.sleep(3)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[2]/div/input').send_keys(PROBLEM)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[3]/div/input').send_keys(SITE)
        time.sleep(5)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[4]/div/input').send_keys('20/01/2022')
        time.sleep(3)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[5]/div/input').send_keys(SEVERITY)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[6]/div/input').send_keys(PROCEDURE)
        time.sleep(4)
        time.sleep(3)
        new_browser.close()
    
   # Test to write Allergy Intolerance in Doctor Dashboard
    @pytest.mark.run(order=14)
    def test_allergyintolerence(self):

        new_browser = webdriver.Chrome(CHROME_PATH)
        new_browser.get(BASE_URL) 
        new_browser.maximize_window()
        DOCTOR_EMAIL='jagdish@gmail.com'
        
        new_browser.find_element_by_xpath('//*[@id="home"]/div/div/button').click()
        new_browser.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(DOCTOR_EMAIL)
        new_browser.find_element_by_xpath('//*[@id="password"]').send_keys(USER_PASSWORD)
        new_browser.find_element_by_class_name('submit-btn').click()
        time.sleep(2)
        
        new_browser.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[3]/a/span').click()
        time.sleep(3)
        new_browser.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[4]/a').click()
        time.sleep(3)
        time.sleep(3)
        new_browser.find_element_by_xpath('/html/body/div[1]/nav/div[3]/nav/ul/li/ul/li[4]/a/span').click()
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/a/button/img').click()
        time.sleep(3)

        ID=1
        SUBSTANCE='smoke'
        VERIFICATION_STATUS='confirm'
        INTOLERANCE='moderate'
        COMMENT='be strict with doses'
        MANIFESTATION='red nose'


        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[1]/div/input').send_keys(ID)
        time.sleep(3)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[2]/div/input').send_keys(SUBSTANCE)
        time.sleep(3)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[3]/div/input').send_keys(VERIFICATION_STATUS)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[4]/div/input').send_keys(INTOLERANCE)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[5]/div/input').send_keys(COMMENT)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[6]/div/input').send_keys(MANIFESTATION)
        time.sleep(3)
        new_browser.find_element_by_xpath('//*[@id="myForm4"]/div/div[7]/button').click()
        time.sleep(2)



        new_browser.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[4]/a').click()
        time.sleep(3)
        new_browser.close()

   # Test to write Problem/Diagonosis List in Doctor Dashboard
    @pytest.mark.run(order=15)
    def test_problem_diag(self):
     
        new_browser = webdriver.Chrome(CHROME_PATH)
        new_browser.get(BASE_URL) 
        new_browser.maximize_window()
        DOCTOR_EMAIL='jagdish@gmail.com'
        new_browser.find_element_by_xpath('//*[@id="home"]/div/div/button').click()
        new_browser.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(DOCTOR_EMAIL)
        new_browser.find_element_by_xpath('//*[@id="password"]').send_keys(USER_PASSWORD)
        new_browser.find_element_by_class_name('submit-btn').click()
        time.sleep(2)
        new_browser.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[3]/a/span').click()
        time.sleep(3)
        new_browser.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[4]/a').click()
        time.sleep(3)

        ID=1
        PROBLEM='Nausea'
        SITE='nose'
        SEVERITY='moderate'
        PROCEDURE='xyz'



        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/a/button/img').click()
        time.sleep(3)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[1]/div/input').send_keys(ID)
        time.sleep(3)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[2]/div/input').send_keys(PROBLEM)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[3]/div/input').send_keys(SITE)
        time.sleep(5)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[4]/div/input').send_keys('20/01/2022')
        time.sleep(3)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[5]/div/input').send_keys(SEVERITY)
        new_browser.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[4]/a/span').click()
        time.sleep(3)
        new_browser.close()

   # Test to write Prescription in Doctor Dashboard
    @pytest.mark.run(order=16)
    def test_eprescription(self):

        new_browser = webdriver.Chrome(CHROME_PATH)
        new_browser.get(BASE_URL) 
        new_browser.maximize_window()

        DOCTOR_EMAIL='jagdish@gmail.com'

        new_browser.find_element_by_xpath('//*[@id="home"]/div/div/button').click()
        new_browser.find_element_by_xpath('//*[@id="inputEmail"]').send_keys(DOCTOR_EMAIL)
        new_browser.find_element_by_xpath('//*[@id="password"]').send_keys(USER_PASSWORD)
        new_browser.find_element_by_class_name('submit-btn').click()
        time.sleep(2)
        new_browser.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[4]/a/span').click()
        time.sleep(3)
        new_browser.find_element_by_xpath('//*[@id="menu1"]/li/ul/li[4]/a').click()
        time.sleep(3)  
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div[4]/a/button/img').click()
        time.sleep(3)

        
        ID=1
        MEDICATION_TERM='nausea'
        ROUTE='xyz'
        DOSAGE_INSTRUCTIONS='twice'
        ADDITIONAL_INSTRUCTION='be strict with doses'
        REASON='normal viral'
        DOSE='dolo 650'
        DOSE_UNIT='2'
        FREQUENCY=2
        STATUS='active'

        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[1]/div/input').send_keys(ID)
        time.sleep(2)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[2]/div/input').send_keys(MEDICATION_TERM)
        time.sleep(2)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[3]/div/input').send_keys(ROUTE)
        time.sleep(2)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[4]/div/input').send_keys(DOSAGE_INSTRUCTIONS)
        time.sleep(2)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[5]/div/input').send_keys(ADDITIONAL_INSTRUCTION)
        time.sleep(2)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[6]/div/input').send_keys(REASON)
        time.sleep(2)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[7]/div/input').send_keys(DOSE)
        time.sleep(2)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[8]/div/input').send_keys(DOSE_UNIT)
        time.sleep(2)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[9]/div/input').send_keys(FREQUENCY)
        time.sleep(2)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[10]/div/input').send_keys(STATUS)
        time.sleep(2)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[11]/div/input').send_keys('25/01/2022')
        time.sleep(2)
        new_browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/form/div/div[12]/div/input').send_keys('20/01/2022')
        time.sleep(4)

        new_browser.close()
                
   
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Test/frontend'))