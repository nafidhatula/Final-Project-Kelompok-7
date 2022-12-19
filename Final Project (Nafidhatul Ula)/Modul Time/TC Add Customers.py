import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestCustomers(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_c_success_add_customers(self): 
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[1]/div//input[@name='username']").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[2]/div//input[@name='password']").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']//aside/nav[@role='navigation']//ul[@class='oxd-main-menu']/li[4]/a[@href='/web/index.php/time/viewTimeModule']/span[.='Time']").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[4]/span[@class='oxd-topbar-body-nav-tab-item']").click()
        time.sleep(1)
        browser.find_element(By.LINK_TEXT,"Customers").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-header-container']/div/button[@type='button']").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']//input").send_keys("Google") # isi nama customer
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']//textarea[@placeholder='Type description here']").send_keys("Leading apparel manufacturing chain.") # isi deskripsi
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(3)

        #validasi
        response_data = browser.find_element(By.CLASS_NAME, "oxd-text oxd-text--p oxd-text--toast-title oxd-toast-content-text").text
        response_message = browser.find_element(By.CLASS_NAME, "oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text").text
        
        self.assertIn('Success', response_data)
        self.assertEqual(response_message, 'Successfully')



    def test_a_failed_add_customers_with_empty_name(self): 
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[1]/div//input[@name='username']").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[2]/div//input[@name='password']").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']//aside/nav[@role='navigation']//ul[@class='oxd-main-menu']/li[4]/a[@href='/web/index.php/time/viewTimeModule']/span[.='Time']").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[4]/span[@class='oxd-topbar-body-nav-tab-item']").click()
        time.sleep(1)
        browser.find_element(By.LINK_TEXT,"Customers").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-header-container']/div/button[@type='button']").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']//input").send_keys("") # isi nama customer
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(3)
        
    def test_b_failed_add_customers_with_same_name(self): 
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[1]/div//input[@name='username']").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[2]/div//input[@name='password']").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']//aside/nav[@role='navigation']//ul[@class='oxd-main-menu']/li[4]/a[@href='/web/index.php/time/viewTimeModule']/span[.='Time']").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[4]/span[@class='oxd-topbar-body-nav-tab-item']").click()
        time.sleep(1)
        browser.find_element(By.LINK_TEXT,"Customers").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-header-container']/div/button[@type='button']").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']//input").send_keys("Fresh Books Software Ltd") # isi nama customer
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//form[@class='oxd-form']//textarea[@placeholder='Type description here']").send_keys("Leading apparel manufacturing chain.") # isi deskripsi
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']//button[@type='submit']").click()
        time.sleep(3) 

    

    def tearDown(self):     
        self.browser.close()

if __name__ == '__main__':
    unittest.main()

    