from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import logging
import time
import pytest

class create_lab_function:

    # 初始化 create_lab 变量为当前类的实例变量
    def __init__(self):
        self.create_lab=self

    #关闭弹窗
    def close_button(self,driver):
        try:
            close_buttons=WebDriverWait(driver,1).until(
            EC.presence_of_all_elements_located((By.XPATH,"//button[@class='closeButton']"))
            )

            for button in close_buttons:
                if button.is_displayed() and button.is_enabled():
                    button.click()
                    return
        except Exception as e:
            logging.info("没找到需要关闭的弹窗")

    # 创建lab
    def create_lab_button(self,driver):
        try:
            #等待New lab按钮出现并点击
            new_lab_button=WebDriverWait(driver,1).until(
            EC.presence_of_element_located((By.XPATH,"//span[text()='New lab']"))
            )
            new_lab_button.click()
        except TimeoutException:
            #如果New lab按钮不存在，则点击Create lab按钮
            create_lab_button=WebDriverWait(driver,1).until(
            EC.presence_of_element_located((By.XPATH,"//span[text()='Create lab']"))
            )
            create_lab_button.click()
    
    # 输入lab name
    def lab_name_input(self,driver):
        lab_name = driver.find_element(By.XPATH, "//input[@placeholder='Lab name (visible to students)']")
        current_lab_name=lab_name.get_attribute("value")
        if current_lab_name!=None:
            lab_name.send_keys(Keys.CONTROL+"a")
            lab_name.send_keys(Keys.BACKSPACE)
        return lab_name
    
    #选择命名含有ml的lab plan
    def lab_plan_ml(self,driver):
        lab_plan=driver.find_element(By.XPATH,"//label[text()='Which plan will be used for this lab?']/following-sibling::div")
        lab_plan.click()
        ml_lab_plan=driver.find_element(By.XPATH,"//span[contains(text(),'ml')]")
        ml_lab_plan.click()

    #选择tag为uniform的lab plan
    def lab_plan_uniform(self,driver):
        lab_plan=driver.find_element(By.XPATH,"//label[text()='Which plan will be used for this lab?']/following-sibling::div")
        lab_plan.click()
        uniform_lab_plan=driver.find_element(By.XPATH,"//span[contains(text(),'uniform')]")
        uniform_lab_plan.click()

    #选择命名含有region的lab plan
    def lab_plan_region(self,driver):
        lab_plan=driver.find_element(By.XPATH,"//label[text()='Which plan will be used for this lab?']/following-sibling::div")
        lab_plan.click()
        uniform_lab_plan=driver.find_element(By.XPATH,"//span[contains(text(),'region')]")
        uniform_lab_plan.click()

    #选择standard small的 vm size
    def size_standard_small(self,driver):
        vm_size=driver.find_element(By.XPATH,"//label[text()='Virtual machine size']/following-sibling::div//span[1]/div")
        vm_size.click()
        search_sizes=driver.find_element(By.XPATH,"//input[@placeholder='Search sizes']")
        search_sizes.send_keys("standard small")
        time.sleep(1)
        confirm_size=driver.find_element(By.XPATH,"(//div[contains(text(),'Standard Small')])[1]")
        confirm_size.click()

    #点击next按钮
    def next_button(self,driver):
        time.sleep(1)
        next=driver.find_element(By.XPATH, "//span[text()='Next']")
        next.click()

    #点击finish按钮
    def finish_button(self,driver):
        finish_button=driver.find_element(By.XPATH, "//button//span[text()='Finish']")
        finish_button.click()

    #输入lyx的username和password
    def username_and_password(self,driver):
        #输入username
        username=driver.find_element(By.XPATH, "//input[@placeholder='Default username']")
        username.send_keys("lyx")
        #输入Password
        password=driver.find_element(By.XPATH, "//input[@placeholder='Default password']")
        password.send_keys("Lyx123456")

    #选择rdp
    def rdp_connection(self,driver):
        connection_types=driver.find_element(By.XPATH,"//label[text()='Enabled connection types']/../../following-sibling::div")
        connection_types.click()
        connection_rdp=driver.find_element(By.XPATH,"//span[text()='Client connection (RDP)']")
        connection_rdp.click()
        continue_rdp=driver.find_element(By.XPATH,"//span[text()='Continue with Remote Desktop']")
        continue_rdp.click()

    #选择rdp in browser
    def web_access(self,driver):
        connection_types=driver.find_element(By.XPATH,"//span[text()='Client connection (RDP)']")
        connection_types.click()
        connection_rdp=driver.find_element(By.XPATH,"//span[text()='Web access (RDP in browser)']")
        connection_rdp.click()

    #添加non admin账号
    def non_admin(self,driver):
        non_admin=driver.find_element(By.XPATH,"//span[text()='Give lab users a non-admin account on their virtual machines']")
        non_admin.click()
        time.sleep(1)
        username2=driver.find_element(By.XPATH, "(//input[@placeholder='Default username'])[2]")
        username2.send_keys("non-lyx")
        password2=driver.find_element(By.XPATH, "(//input[@placeholder='Default password'])[2]")
        password2.send_keys("Password01")

    #取消选择same password
    def diff_password(self,driver):
        same_password_checkbox=driver.find_element(By.XPATH,"//span[text()='Use same password for all virtual machines']")
        same_password_checkbox.click()

    #等待overlay遮挡层消失
    def overlay_disappear(self,driver):
        WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.CLASS_NAME, "ms-Overlay")))

    #点击"Azure Lab Services"按钮，返回首页
    def ALS_button(self,driver):
        ALS_button=driver.find_element(By.XPATH, "//*[@id='page-header-container']/div/div/div/div/div[1]/div[1]/div/button")
        ALS_button.click()

    #选择vs的image
    def vs_image(self,driver):
        vs_image=driver.find_element(By.XPATH,"//div[contains(text(),'Ubuntu')]")
        vs_image.click()
        vs_image_choose=driver.find_element(By.XPATH,"//div[contains(text(),'Visual Studio')]")
        vs_image_choose.click()

    #选择wins的image
    def wins_image(self,driver):
        wins_image=driver.find_element(By.XPATH,"//div[contains(text(),'Ubuntu')]")
        wins_image.click()
        wins_image_choose=driver.find_element(By.XPATH,"//div[contains(text(),'Windows Server')]")
        wins_image_choose.click()

    #选择linux image
    def ubuntu_image(self,driver):
        ubuntu_image=driver.find_element(By.XPATH,"//label[text()='Virtual machine image']/following-sibling::div")
        ubuntu_image.click()
        ubuntu_image_choose=driver.find_element(By.XPATH,"//div[text()='Ubuntu Server 20.04 LTS']")
        ubuntu_image_choose.click()
