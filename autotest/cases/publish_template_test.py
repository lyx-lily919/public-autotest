from lib.template_function import template_function
from lib.users_function import users_function
from cfg.config import config
import time
import datetime

class Test_publish_template:

    def setup_class(self):
        self.publish_template=template_function()
        self.register_user=users_function()
    
    def test_publish_template(self,driver):
        request_url,_,_,headers=config.requests_message(driver)
        #检测虚拟机初始状态
        tem_state=self.publish_template.get_vm_state(request_url,headers)
        print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]虚拟机初始状态为:{tem_state}")

        if tem_state == "Draft":
            self.publish_template.publish_vm(driver)
            while True:
                tem_state=self.publish_template.get_vm_state(request_url,headers)
                print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]虚拟机状态为:{tem_state}")
                if tem_state == "Published":
                    print("虚拟机已经发布完成，开始注册")
                    self.register_user.add_users_register_via_link(driver)
                    break
                time.sleep(60)
        elif tem_state == "Publishing":
            while True:
                tem_state=self.publish_template.get_vm_state(request_url,headers)
                print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]等待发布完成，虚拟机状态为:{tem_state}")
                if tem_state == "Published":
                    print("虚拟机已经发布完成，开始注册")
                    self.register_user.add_users_register_via_link(driver)
                    break
                time.sleep(60)
        elif tem_state == "Published":
            print("虚拟机已经发布完成，开始注册")
            self.register_user.add_users_register_via_link(driver)

# python -m pytest cases\publish_template_test.py --html=report.html --self-contained-html 
# python -m pytest cases\publish_template_test.py --login-portal=canvas --html=report.html --self-contained-html 

#python -m pytest -s cases\publish_template_test.py