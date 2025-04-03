from lib.schedule_function import schedule_function
from lib.create_lab_function import create_lab_function
from selenium.webdriver.common.by import By
from cfg.config import config
from datetime import datetime
import requests
import logging
import time

class Test_schedule:
    def setup_class(self):
        self.schedule=schedule_function()
        self.overlay_disappear=create_lab_function()

    def test_schedule(self,driver):
        _,vm_pool_url,users_url,headers=config.requests_message(driver)

        #添加schedule event
        vm_stop_detect_time=self.schedule.add_schedule_event(driver)

        #等待overlay遮挡层消失
        self.overlay_disappear.overlay_disappear(driver)

        #点击进入virtual_machine_pool
        vm_pool_module=driver.find_element(By.XPATH,"//span[text()='Virtual machine pool']")
        vm_pool_module.click()

        #获取users API的响应内容
        users_response=requests.get(users_url,headers=headers)
        users_data=users_response.json()

        user_map={user["id"]:user["properties"]["email"] for user in users_data["value"]}

        #检测循环35分钟后停止
        while datetime.now()<vm_stop_detect_time:
            logging.info(f"Checking VM status at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

            vm_pool_response=requests.get(vm_pool_url,headers=headers)
            vm_pool_data=vm_pool_response.json()

            for i in vm_pool_data["value"]:

                if i["properties"].get("vmType")=="User":
                    state=i["properties"]["state"]

                    if "claimedByUserId" in i["properties"]:
                        user_id=i["properties"]["claimedByUserId"]
                        user_name=user_map.get(user_id,"Unknown User")
                        logging.info(f"User:{user_name} :{state}")
                    else:
                        logging.info(f"User not claimed:{state}")
            logging.info("-"*50)
            time.sleep(60)
        

#python -m pytest -s cases\schedule_test.py
#python -m pytest -s --log-cli-level=INFO --log-file=pytest_log.txt --log-file-level=INFO cases\schedule_test.py
#(--log-cli-level=INFO 防止pytest捕获日志。--log-filr=pytest_log.txt把日志写入文件。 --log-file-level=INFO确保INFO级别日志也能写入文件)
