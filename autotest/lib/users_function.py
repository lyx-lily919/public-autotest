from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import pytest
import pyperclip
import time

class users_function():

    #先添加用户，然后再通过链接注册
    def add_users_register_via_link(self,driver):
        users_module=driver.find_element(By.XPATH,"//span[text()='Users']")
        users_module.click()

        try:
            #等待第一个按钮出现并点击
            add_users_button=WebDriverWait(driver,3).until(
                EC.presence_of_element_located((By.XPATH,"//span[text()='Add users']"))
            )
            add_users_button.click()
        except TimeoutException:
            #如果第一个按钮不存在，则点击第二个按钮
            add_users_manually_button=WebDriverWait(driver,3).until(
                EC.presence_of_element_located((By.XPATH,"//span[text()='Add users manually']"))
            )
            add_users_manually_button.click()

        #在文本框输入要添加的用户邮箱
        email_textarea=driver.find_element(By.TAG_NAME,"textarea")
        email_textarea.send_keys("v-yixueli@microsoft.com")
        email_textarea.send_keys(Keys.ENTER)
        email_textarea.send_keys("yixuelie@outlook.com")
        email_textarea.send_keys(Keys.ENTER)
        email_textarea.send_keys("lyx-lily@outlook.com")
        #点击Add按钮
        time.sleep(1)
        add_button=driver.find_element(By.XPATH,"//span[text()='Add']")
        add_button.click()

        #复制Registration link链接
        time.sleep(3)
        registration_link=driver.find_element(By.XPATH,"//span[text()='Registration link']")
        registration_link.click()
        copy_button=driver.find_element(By.XPATH,"//span[text()='Copy']")
        copy_button.click()
        done_button=driver.find_element(By.XPATH,"//span[text()='Done']")
        done_button.click()
        time.sleep(1)

        try:
            #获取剪贴板的内容
            clipboard_content=pyperclip.paste()

            #Edge浏览器进入学生端页面
            driver.get(clipboard_content)
        except Exception as e:
            pytest.fail(f"发生错误：{e}")
        finally:
            time.sleep(3)
            print("注册成功")

        #chrome浏览器进入学生端页面
        # chrome_driver=webdriver.Chrome(options=chrome_options)
        # chrome_driver.maximize_window()
        # chrome_driver.get(clipboard_content)

        # #firefox浏览器进入学生端页面
        # firefox_driver=webdriver.Firefox()
        # firefox_driver.maximize_window()
        # firefox_driver.get(clipboard_content)
