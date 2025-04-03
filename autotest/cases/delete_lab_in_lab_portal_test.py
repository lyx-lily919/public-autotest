from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

@pytest.mark.DeleteLab
class Test_delete_lab_in_lab_portal:
    def test_delete_lab_in_lab_portal(self,driver):
        try:
        
            #获取所有lab_menu按钮元素
            lab_menu_buttons=driver.find_elements(By.XPATH,"//button[@aria-label='Lab menu']")

            #遍历"Lab menu"按钮，依次点击
            for lab_menu_button in lab_menu_buttons:
                #点击"Lab menu"按钮
                lab_menu_button.click()
                #点击“delete”按钮
                delete_lab_button=driver.find_element(By.XPATH,"//span[text()='Delete']")
                delete_lab_button.click()
                #点击确认删除的"delete"按钮
                confirm_delete_button=driver.find_element(By.XPATH,"//span[text()='Delete']")
                confirm_delete_button.click()

                #等待overlay遮挡层消失
                WebDriverWait(driver, 20).until(
                    EC.invisibility_of_element((By.CLASS_NAME, "ms-Overlay"))
                )

                #确保删除操作完成，即确保"Lab menu"按钮数量减少
                lambda driver: len(driver.find_elements(By.XPATH,"//button[@aria-label='Lab menu']"))<len(lab_menu_buttons)
                #重新获取更新后的"Lab menu"按钮列表
                lab_menu_buttons=driver.find_elements(By.XPATH,"//button[@aria-label='Lab menu']")
        except Exception as e:
            pytest.fail(f"发生错误：{e}")
        finally:
            time.sleep(3)

# python -m pytest cases\delete_lab_in_lab_portal_test.py --html=report.html --self-contained-html 
# python -m pytest cases\delete_lab_in_lab_portal_test.py --login-portal=canvas --html=report.html --self-contained-html 