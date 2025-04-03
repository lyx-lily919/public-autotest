from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
from lib.create_lab_function import create_lab_function

def login_canvas():
    options=webdriver.EdgeOptions()
    options.add_experimental_option('excludeSwitches',['enable-logging'])

    # 启动浏览器并打开目标页面
    driver = webdriver.Edge(options=options)
    driver.maximize_window()

    #url需要改！！！
    driver.get("https://office365.instructure.com/courses/2515/external_tools/2661")
    driver.implicitly_wait(50)

    #输入用户名和密码后登录
    email=driver.find_element(By.XPATH,"//label[text()='Email']/following-sibling::input")
    email.send_keys("Carac")
    password=driver.find_element(By.XPATH,"//label[text()='Password']/following-sibling::input")
    password.send_keys("BETT!2020")
    login=driver.find_element(By.XPATH,"//input[@value='Log In']")
    login.click()
    main_window=driver.current_window_handle

    #登录azure lab services
    driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[@class="tool_launch"]'))
    sign_in=driver.find_element(By.XPATH,"//span[text()='Sign in']")
    sign_in.click()
    WebDriverWait(driver,10).until(lambda d:len(d.window_handles)>1)
    windows_handles=driver.window_handles
    for handle in windows_handles:
        if handle!=main_window:
            driver.switch_to.window(handle)
            break
    account=driver.find_element(By.XPATH,"//small[text()='v-yixueli@microsoft.com']")
    account.click()
    driver.switch_to.window(main_window)
    driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[@class="tool_launch"]'))

    create_lab=create_lab_function()

    #如果弹窗出现，则关闭
    create_lab.close_button(driver)

    return driver