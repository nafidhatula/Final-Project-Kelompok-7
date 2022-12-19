import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLeave(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_add_entitlements(self): 
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[1]/div//input[@name='username']").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[2]/div//input[@name='password']").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']/li[3]").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[3]").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-topbar-body']/nav[@role='navigation']/ul/li[3]/ul[@role='menu']/li[1]").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[1]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--grouped-field']/div[1]//label").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//div[@class='oxd-autocomplete-wrapper']/div/input[@placeholder='Type for hints...']").send_keys("L") # isi nama 
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div[2]/div[4]").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div[2]/div[5]/span").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div[2]/div[6]").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[3]/div/div[3]/div//input").send_keys("7") # isi deskripsi
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@role='dialog']//div[@role='document']/div[@class='orangehrm-modal-footer']/button[2]").click()
        time.sleep(3)

        #validasi
        #response_message = browser.find_element(By.ID, "oxd-toaster_1").text
        #self.assertEqual(response_message, 'Success- Successfully Saved')
    
         #validasi
        response_data = browser.find_element(By.CLASS_NAME, "oxd-text oxd-text--p oxd-text--toast-title oxd-toast-content-text").text
        response_message = browser.find_element(By.CLASS_NAME, "oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text").text
        
        self.assertIn('Success', response_data)
        self.assertEqual(response_message, 'Successfully')

    def test_b_failed_add_entitlements(self): 
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[1]/div//input[@name='username']").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[2]/div//input[@name='password']").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']/li[3]").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[3]").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-topbar-body']/nav[@role='navigation']/ul/li[3]/ul[@role='menu']/li[1]").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[1]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--grouped-field']/div[1]//label").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[2]/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//div[@class='oxd-autocomplete-wrapper']/div/input[@placeholder='Type for hints...']").send_keys("L") # isi nama 
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div[2]/div[4]").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div[2]/div[5]/span").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div[2]/div[6]").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[3]/div/div[3]/div//input").send_keys("7") # isi deskripsi
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@role='dialog']//div[@role='document']/div[@class='orangehrm-modal-footer']/button[1]").click()
        time.sleep(3)

    def test_c_failed_add_entitlements_with_empty_data(self): 
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[1]/div//input[@name='username']").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[2]/div//input[@name='password']").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']/li[3]").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"//div[@id='app']//header[@class='oxd-topbar']//nav[@role='navigation']/ul/li[3]").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']//div[@class='oxd-topbar-body']/nav[@role='navigation']/ul/li[3]/ul[@role='menu']/li[1]").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']//form[@class='oxd-form']/div[3]/div/div[3]/div//input").send_keys("7") # isi deskripsi
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']/div[@class='oxd-form-actions']/button[@type='submit']").click()
        time.sleep(3)
    def tearDown(self):     
        self.browser.close()

if __name__ == '__main__':
    unittest.main()