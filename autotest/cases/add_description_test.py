from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
import pytest

class Test_add_description:

    #检查并设置description
    def set_description(driver,excepted_text):
        try:
            wait=WebDriverWait(driver,10)
            #等待description文本框可见并点击
            description=wait.until(
                EC.element_to_be_clickable((By.XPATH,"//textarea[@placeholder='Enter your description of the virtual machine for the class. The title and this description will be visible to students.']"))
            )

            #获取当前的文本值
            current_text=description.get_attribute("value")
            print(f"当前文本框内容：{current_text}")

            #如果内容不是预期内容，则清空重新设置
            if current_text!=excepted_text:
                print("文本框内容与预期不符，正在更新。。。")
                description.click()
                description.send_keys(Keys.CONTROL+"a")
                description.send_keys(Keys.BACKSPACE)
                time.sleep(1)
                description.send_keys(excepted_text)
                time.sleep(1)
            else:
                print("文本框内容已符合预期，无需更新。")

        except Exception as e:
            pytest.fail(f"处理description出现错误：{e}")

    def test_add_description(self,driver):
        #获取资源组名称
        get_rg_name=driver.find_element(By.XPATH,"//span[text()='Select an item']/following-sibling::div/div/following-sibling::div")
        rg_name=get_rg_name.text

        #主程序
        #找到所有符合条件的div元素
        divs=driver.find_elements(By.XPATH,"//div[@class='lab-list__card-title-overflow-vnext']")

        #依次点击每个div
        for index in range(len(divs)):
            try:
                #重新获取div列表，获取lab名称
                divs=driver.find_elements(By.XPATH,"//div[@class='lab-list__card-title-overflow-vnext']")
                lab_name=divs[index].text
                print(f"点击{lab_name}")
                divs[index].click()

                #进入template页面
                template=driver.find_element(By.XPATH,"//span[text()='Template']")
                template.click()

                #添加description
                wait=WebDriverWait(driver,10)
                description=wait.until(
                    EC.element_to_be_clickable((By.XPATH,"//textarea[@placeholder='Enter your description of the virtual machine for the class. The title and this description will be visible to students.']"))
                    )
                
                time.sleep(1)
                description.send_keys(Keys.CONTROL+"a")
                description.send_keys(Keys.BACKSPACE)
                time.sleep(1)
                description.send_keys(rg_name)
                time.sleep(1)

                #点击"Azure Lab Services"按钮，返回首页
                ALS_button=driver.find_element(By.XPATH, "//*[@id='page-header-container']/div/div/div/div/div[1]/div[1]/div/button").click()

            except Exception as e:
                pytest.fail(f"点击第{index+1}个元素时出现错误{e}，该lab的名称为{lab_name}")

        #验证循环：检查并修正所有div的description
        all_correct=False
        while not all_correct:
            all_correct=True
            print("\n------开始验证循环------")
            for index in range(len(divs)):
                try:
                    #重新获取所有div列表
                    divs=driver.find_elements(By.XPATH,"//div[@class='lab-list__card-title-overflow-vnext']")
                    lab_name=divs[index].text
                    print(f"\n点击{lab_name}")
                    divs[index].click()

                    #进入template页面
                    template=driver.find_element(By.XPATH,"//span[text()='Template']")
                    template.click()

                    #检查并设置description内容
                    wait=WebDriverWait(driver,10)
                    description=wait.until(
                        EC.element_to_be_clickable((By.XPATH,"//textarea[@placeholder='Enter your description of the virtual machine for the class. The title and this description will be visible to students.']"))
                    )
                    current_text=description.get_attribute("value")
                    print(f"当前文本框内容：{current_text}")

                    if current_text!=rg_name:
                        print(f"{lab_name}的文本框内容与预期不符，正在更新。。。")
                        self.set_description(driver,rg_name)
                        all_correct=False
                    else:
                        print(f"{lab_name}的文本框内容正确。")
                    
                    #点击"Azure Lab Services"按钮，返回首页
                    ALS_button=driver.find_element(By.XPATH, "//*[@id='page-header-container']/div/div/div/div/div[1]/div[1]/div/button").click()
                except Exception as e:
                    pytest.fail(f"验证{lab_name}时出现错误：{e}")

# python -m pytest cases\add_description_test.py --html=report.html --self-contained-html 
# python -m pytest cases\add_description_test.py --login-portal=canvas --html=report.html --self-contained-html