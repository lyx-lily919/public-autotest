from lib.vm_pool_function import vm_pool_function
from cfg.config import config
from datetime import datetime,timedelta
import logging
import time

class Test_all_vm_state:

    def setup_class(self):
        self.all_vm_state=vm_pool_function()

    def test_all_vm_state(self,driver):
        _,vm_pool_url,users_url,headers=config.requests_message(driver)

        vm_detect_time=datetime.now()+timedelta(minutes=25)

        while datetime.now()<vm_detect_time:
            logging.info(f"Checking VM status at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            self.all_vm_state.all_vm_state(vm_pool_url,users_url,headers)
            logging.info("-"*50)
            time.sleep(60)

#python -m pytest -s --log-cli-level=INFO --log-file=pytest_log.txt --log-file-level=INFO cases\all_vm_state_test.py