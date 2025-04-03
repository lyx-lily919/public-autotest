from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime,timedelta
import logging
import time

class schedule_function:

    #添加schedule event
    def add_schedule_event(self,driver):
        #选择到schedule页面
        schedule_module=driver.find_element(By.XPATH,"//span[text()='Schedule']")
        schedule_module.click()
        #点击add scheduled event按钮
        add_schedule_event=driver.find_element(By.XPATH,"//span[text()='Add scheduled event']")
        add_schedule_event.click()
        #获取当前时间
        current_time=datetime.now()
        #设置开始时间并将开始时间转为字符串形式
        start_time=current_time + timedelta(minutes=10)
        formatted_time_start=start_time.strftime("%I:%M %p")
        formatted_time_start=formatted_time_start.lstrip("0")
        #设置停止时间并将停止时间转为字符串形式
        stop_time=start_time + timedelta(minutes=15)
        formatted_time_stop=stop_time.strftime("%I:%M %p")
        formatted_time_stop=formatted_time_stop.lstrip("0")
        #设置检测虚拟机(virtual machine pool)时间为35分钟（可自由调整检测时间）。功能正常情况下开始检测后10分钟虚拟机打开，15分钟后虚拟机关闭，共耗时25分钟，再预留10分钟开关机可能延迟的时间，（加10分钟），35分钟足够看清虚拟机状态变化。
        vm_stop_detect_time=current_time+timedelta(minutes=35)
        #将开始时间填入input框
        start_time_input=driver.find_element(By.XPATH,"//label[text()='Start time']/following-sibling::div/input")
        start_time_input.click()
        start_time_input.send_keys(Keys.CONTROL+"a")
        start_time_input.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        start_time_input.send_keys(formatted_time_start)
        #将停止时间填入input框
        stop_time_input=driver.find_element(By.XPATH,"//label[text()='Stop time']/following-sibling::div/input")
        stop_time_input.click()
        stop_time_input.send_keys(Keys.CONTROL+"a")
        stop_time_input.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        stop_time_input.send_keys(formatted_time_stop)
        #点击save按钮，保存schedule event
        save_button=driver.find_element(By.XPATH,"//span[text()='Save']")
        save_button.click()

        logging.info(f"当前时间为：{current_time}\n上课时间为：{start_time}-{stop_time}\n")

        return vm_stop_detect_time
        