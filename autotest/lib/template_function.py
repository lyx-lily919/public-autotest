from selenium.webdriver.common.by import By
import requests
import time

class template_function:
    
    def publish_vm(self,driver):
        #点击publish按钮
        publish_button=driver.find_element(By.XPATH,"//span[text()='Publish']")
        publish_button.click()

        #设置lab的虚拟机最大数量
        # num_vm=driver.find_element(By.XPATH,"//div[@aria-label='Set the maximum number of machines in the lab']/input")
        # time.sleep(1)
        # driver.execute_script("arguments[0].value='3';",num_vm)
        num_vm_up=driver.find_element(By.XPATH,"//i[@data-icon-name='ChevronUpSmall']")
        for _ in range(3):
            num_vm_up.click()
            time.sleep(1)

        #点击设置好虚拟机数量后的publish按钮
        time.sleep(1)
        publish_template_button=driver.find_element(By.XPATH,"(//span[text()='Publish'])[2]")
        publish_template_button.click()


    def get_vm_state(self,request_url,headers):
        state="未开始检测"
        response=requests.get(url=request_url,headers=headers)
        if response.status_code==200:
            data=response.json()
            # print(f"完整的数据内容为：{response.text}")
            state=data.get("properties",{}).get("state","未知")
            # print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]虚拟机状态:{state}")
        else:
            print(f"请求失败:{response.status_code},{response.text}")
        return state     
