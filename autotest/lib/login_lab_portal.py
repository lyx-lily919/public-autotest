from selenium import webdriver
from selenium.webdriver.common.by import By
from lib.create_lab_function import create_lab_function

def login_lab_portal():
    options=webdriver.EdgeOptions()
    options.add_experimental_option('excludeSwitches',['enable-logging'])

    # 启动浏览器并打开目标页面
    driver = webdriver.Edge(options=options)
    driver.maximize_window()

    #url需要改！！！
    driver.get("https://labs.azure.com/subscriptions/2d5eedc9-8509-41fe-aac8-f16d54583ac6/resourcegroups/lyx-ml-0331/providers/microsoft.labservices/labs/linux-samepwd/template")
    driver.implicitly_wait(50)

    #点击账号进入
    account=driver.find_element(By.XPATH,"//div[text()='Yixue Li (WICRESOFT NORTH AMERICA LTD)']")
    account.click()

    #点击关闭弹窗
    create_lab=create_lab_function()
    create_lab.close_button(driver)

    return driver

