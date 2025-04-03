from selenium import webdriver
from selenium.webdriver.common.by import By
from lib.login_lab_portal import login_lab_portal

class config:

    def requests_message(driver):
        #获取资源组名称
        get_rg_name=driver.find_element(By.XPATH,"//span[text()='Select an item']/following-sibling::div/div/following-sibling::div")
        rg_name=get_rg_name.text

        #获取lab名称
        get_lab_name=driver.find_element(By.XPATH,"//span[text()='Select a lab']/following-sibling::div/div/span")
        lab_name=get_lab_name.text

        #request url
        request_url=f"https://management.azure.com/subscriptions/2d5eedc9-8509-41fe-aac8-f16d54583ac6/resourceGroups/{rg_name}/providers/Microsoft.LabServices/labs/{lab_name}?api-version=2023-06-07"
        vm_pool_url=f"https://management.azure.com/subscriptions/2d5eedc9-8509-41fe-aac8-f16d54583ac6/resourceGroups/{rg_name}/providers/Microsoft.LabServices/labs/{lab_name}/virtualMachines?api-version=2023-06-07"
        users_url=f"https://management.azure.com/subscriptions/2d5eedc9-8509-41fe-aac8-f16d54583ac6/resourceGroups/{rg_name}/providers/Microsoft.LabServices/labs/{lab_name}/users?api-version=2023-06-07"

        #authorization需要改！！！



        

        return request_url,vm_pool_url,users_url,headers
