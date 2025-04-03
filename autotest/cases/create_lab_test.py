from lib.create_lab_function import create_lab_function
import time
import pytest

@pytest.mark.CreateLab
class Test_create_lab:

    # 初始化 create_lab_function 实例，并作为实例变量(如果测试类中定义了 __init__ 方法，pytest 会认为该类不是测试类，从而跳过测试。因此使用setup_class初始化共享变量)
    def setup_class(self):
        self.create_lab=create_lab_function()

    #创建lab。image为"ubuntu"，使用相同的密码，连接类型为SSH和RDP。
    def test_create_lab_linux(self,driver):
        try:

            #点击new lab按钮，若不存在，点击create lab按钮
            self.create_lab.create_lab_button(driver)

            #输入lab name
            lab_name=self.create_lab.lab_name_input(driver)
            lab_name.send_keys(driver.lab_portal_name+"linux-samepwd")

            #选择命名含有ml的lab plan
            self.create_lab.lab_plan_ml(driver)

            #选择vm size
            self.create_lab.size_standard_small(driver)

            #点击"Step 1 of 4"的next按钮
            self.create_lab.next_button(driver)

            #输入username和password
            self.create_lab.username_and_password(driver)

            #点击"Step 2 of 4"的next按钮
            self.create_lab.next_button(driver)

            #选择rdp
            self.create_lab.rdp_connection(driver)

            #点击"Step 3 of 4"的next按钮
            self.create_lab.next_button(driver)
            
            #点击Finish按钮
            self.create_lab.finish_button(driver)

            #等待overlay遮挡层消失
            self.create_lab.overlay_disappear(driver)

            #点击"Azure Lab Services"按钮，返回首页
            self.create_lab.ALS_button(driver)

            #所有步骤结束，打印创建lab成功信息
            print("创建linux lab成功")

        except Exception as e:
            pytest.fail(f"发生错误: {e}")
        finally:
            time.sleep(1)

    #创建lab。image为"Visual studio on windows 11"，使用相同的密码，连接类型为RDP和RDP in browser。
    def test_create_lab_vs(self,driver):
        try:

            #点击new lab按钮，若不存在，点击create lab按钮
            self.create_lab.create_lab_button(driver)
        
            #输入lab name
            lab_name=self.create_lab.lab_name_input(driver)
            lab_name.send_keys(driver.lab_portal_name+"vs-samepwd-webaccess")

            #选择命名含有ml的lab plan
            self.create_lab.lab_plan_ml(driver)

            #选择VS image
            self.create_lab.vs_image(driver)

            #选择vm size
            self.create_lab.size_standard_small(driver)

            #点击"Step 1 of 4"的next按钮
            self.create_lab.next_button(driver)

            #输入username和password
            self.create_lab.username_and_password(driver)

            #点击"Step 2 of 4"的next按钮
            self.create_lab.next_button(driver)

            #选择rdp in browser
            self.create_lab.web_access(driver)

            #点击"Step 3 of 4"的next按钮
            self.create_lab.next_button(driver)
            
            #点击Finish按钮
            self.create_lab.finish_button(driver)

            #等待overlay遮挡层消失
            self.create_lab.overlay_disappear(driver)

            #点击"Azure Lab Services"按钮，返回首页
            self.create_lab.ALS_button(driver)

            #所有步骤结束，打印创建lab成功信息
            print("创建vs lab成功")

        except Exception as e:
            pytest.fail(f"发生错误: {e}")
        finally:
            time.sleep(3)

    #创建lab。image为"windows server"，添加non-admin账户，使用不同的密码，连接类型为RDP。
    def test_create_lab_wins(self,driver):
        try:

            #点击new lab按钮，若不存在，点击create lab按钮
            self.create_lab.create_lab_button(driver)
        
            #输入lab name
            lab_name=self.create_lab.lab_name_input(driver)
            lab_name.send_keys(driver.lab_portal_name+"wins-diffpwd-non-admin")

            #选择命名含有ml的lab plan
            self.create_lab.lab_plan_ml(driver)

            #选择wins image
            self.create_lab.wins_image(driver)

            #选择vm size
            self.create_lab.size_standard_small(driver)

            #点击"Step 1 of 4"的next按钮
            self.create_lab.next_button(driver)

            #输入username和password
            self.create_lab.username_and_password(driver)

            #添加non admin账号
            self.create_lab.non_admin(driver)

            #取消选择same password
            self.create_lab.diff_password(driver)

            #点击"Step 2 of 4"的next按钮
            self.create_lab.next_button(driver)

            #点击"Step 3 of 4"的next按钮
            self.create_lab.next_button(driver)
            
            #点击Finish按钮
            self.create_lab.finish_button(driver)

            #等待overlay遮挡层消失
            self.create_lab.overlay_disappear(driver)

            #点击"Azure Lab Services"按钮，返回首页
            self.create_lab.ALS_button(driver)

            #所有步骤结束，打印创建lab成功信息
            print("创建windows server lab成功")

        except Exception as e:
            pytest.fail(f"发生错误: {e}")
        finally:

            time.sleep(3)

    #创建lab。image为"Ubuntu"，使用tag为uniform的lab plan,添加admin账户，使用相同的密码，连接类型为SSH和RDP。
    def test_create_lab_uniform(self,driver):
        try:

            #点击new lab按钮，若不存在，点击create lab按钮
            self.create_lab.create_lab_button(driver)
            
            #输入lab name
            lab_name=self.create_lab.lab_name_input(driver)
            lab_name.send_keys(driver.lab_portal_name+"uniform-linux-non-admin")

            #选择tag为uniform的lab plan(在创建lab plan的时候命名含有uniform)
            self.create_lab.lab_plan_uniform(driver)

            #选择linux image
            self.create_lab.ubuntu_image(driver)

            #选择vm size
            self.create_lab.size_standard_small(driver)

            #点击"Step 1 of 4"的next按钮
            self.create_lab.next_button(driver)

            #输入username和password
            self.create_lab.username_and_password(driver)

            #添加non admin账号
            self.create_lab.non_admin(driver)

            #点击"Step 2 of 4"的next按钮
            self.create_lab.next_button(driver)

            #选择rdp
            self.create_lab.rdp_connection(driver)

            #点击"Step 3 of 4"的next按钮
            self.create_lab.next_button(driver)
            
            #点击Finish按钮
            self.create_lab.finish_button(driver)

            #等待overlay遮挡层消失
            self.create_lab.overlay_disappear(driver)

            #点击"Azure Lab Services"按钮，返回首页
            self.create_lab.ALS_button(driver)

            #所有步骤结束，打印创建lab成功信息
            print("创建uniform lab成功")

        except Exception as e:
            pytest.fail(f"发生错误: {e}")
        finally:
            time.sleep(3)

    #创建lab。image为"Visual studio on windows 11"，使用相同的密码，连接类型为RDP。
    def test_create_lab_uniform_vs(self,driver):
        try:

            #点击new lab按钮，若不存在，点击create lab按钮
            self.create_lab.create_lab_button(driver)
            
            #输入lab name
            lab_name=self.create_lab.lab_name_input(driver)
            lab_name.send_keys(driver.lab_portal_name+"uniform-vs")

            #选择tag为uniform的lab plan(在创建lab plan的时候命名含有uniform)
            self.create_lab.lab_plan_uniform(driver)

            #选择VS image
            self.create_lab.vs_image(driver)

            #选择vm size
            self.create_lab.size_standard_small(driver)

            #点击"Step 1 of 4"的next按钮
            self.create_lab.next_button(driver)

            #输入username和password
            self.create_lab.username_and_password(driver)

            #点击"Step 2 of 4"的next按钮
            self.create_lab.next_button(driver)

            #点击"Step 3 of 4"的next按钮
            self.create_lab.next_button(driver)
            
            #点击Finish按钮
            self.create_lab.finish_button(driver)

            #等待overlay遮挡层消失
            self.create_lab.overlay_disappear(driver)

            #点击"Azure Lab Services"按钮，返回首页
            self.create_lab.ALS_button(driver)

            #所有步骤结束，打印创建lab成功信息
            print("创建uniform lab vs成功")

        except Exception as e:
            pytest.fail(f"发生错误: {e}")
        finally:
            time.sleep(3)

    #创建lab。image为"windows server",使用相同的密码，连接类型为RDP。
    def test_create_lab_uniform_wins(self,driver):
        try:

            #点击new lab按钮，若不存在，点击create lab按钮
            self.create_lab.create_lab_button(driver)
            
            #输入lab name
            lab_name=self.create_lab.lab_name_input(driver)
            lab_name.send_keys(driver.lab_portal_name+"uniform-wins")

            #选择tag为uniform的lab plan(在创建lab plan的时候命名含有uniform)
            self.create_lab.lab_plan_uniform(driver)

            #选择wins image
            self.create_lab.wins_image(driver)

            #选择vm size
            self.create_lab.size_standard_small(driver)

            #点击"Step 1 of 4"的next按钮
            self.create_lab.next_button(driver)

            #输入username和password
            self.create_lab.username_and_password(driver)

            #点击"Step 2 of 4"的next按钮
            self.create_lab.next_button(driver)

            #点击"Step 3 of 4"的next按钮
            self.create_lab.next_button(driver)
            
            #点击Finish按钮
            self.create_lab.finish_button(driver)

            #等待overlay遮挡层消失
            self.create_lab.overlay_disappear(driver)

            #点击"Azure Lab Services"按钮，返回首页
            self.create_lab.ALS_button(driver)

            #所有步骤结束，打印创建lab成功信息
            print("创建uniform lab wins成功")

        except Exception as e:
            pytest.fail(f"发生错误: {e}")
        finally:
            time.sleep(3)

    #创建lab。image为"linux"，使用相同的密码，连接类型为SSH。
    def test_create_lab_diff_region(self,driver):
        try:

            #点击new lab按钮，若不存在，点击create lab按钮
            self.create_lab.create_lab_button(driver)
            
            #输入lab name
            lab_name=self.create_lab.lab_name_input(driver)
            lab_name.send_keys(driver.lab_portal_name+"diff-region")

            #选择名字含有region的lab plan
            self.create_lab.lab_plan_region(driver)

            #选择linux image
            self.create_lab.ubuntu_image(driver)

            #选择vm size
            self.create_lab.size_standard_small(driver)

            #点击"Step 1 of 4"的next按钮
            self.create_lab.next_button(driver)

            #输入username和password
            self.create_lab.username_and_password(driver)

            #点击"Step 2 of 4"的next按钮
            self.create_lab.next_button(driver)

            #点击"Step 3 of 4"的next按钮
            self.create_lab.next_button(driver)

            #点击Finish按钮
            self.create_lab.finish_button(driver)

            #等待overlay遮挡层消失
            self.create_lab.overlay_disappear(driver)

            #点击"Azure Lab Services"按钮，返回首页
            self.create_lab.ALS_button(driver)

            #所有步骤结束，打印创建lab成功信息
            print("创建uniform lab成功")

        except Exception as e:
            pytest.fail(f"发生错误: {e}")
        finally:
            time.sleep(1)

# python -m pytest cases\create_lab_test.py --html=report.html --self-contained-html 
# python -m pytest cases\create_lab_test.py --login-portal=canvas --html=report.html --self-contained-html 
