import pytest
import logging
import sys

# 自定义命令行参数 --login-portal.
def pytest_addoption(parser):
    parser.addoption(
        "--login-portal",# 参数名
        action="store",# 存储值
        default="lab_portal",# 默认值为lab portal
        help="Login portal:lab portal or canvas" # 参数说明
    )

@pytest.fixture(scope="class")
def driver(request):
    login_portal=request.config.getoption("--login-portal")
    
    if login_portal=="lab_portal":
        from lib.login_lab_portal import login_lab_portal
        driver=login_lab_portal()
        setattr(driver,"lab_portal_name","")
    elif login_portal=="canvas":
        from lib.login_canvas import login_canvas
        driver=login_canvas()
        setattr(driver,"lab_portal_name","canvas-")
    else:
        raise ValueError(f"Unknown login portal:{login_portal}")

    yield driver
    driver.quit()

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "CreateLab: 标记与创建实验室相关的测试用例"
    )
    config.addinivalue_line(
        "markers", "DeleteLab: 标记与删除实验室相关的测试用例"
    )


@pytest.fixture(scope="class")
def request_url():
    return request_url

@pytest.fixture(scope="class")
def headers():
    return headers

@pytest.fixture(scope="session",autouse=True)
def setup_logging():
    #配置pytest日志
    log_path="pytest_log.txt"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8",
        handlers=[
            logging.FileHandler(log_path,mode="w"), #输出到文件
            logging.StreamHandler(sys.stdout) #输出到终端
        ]
    )

    logging.info("测试开始")
    yield
    logging.info("测试结束")

