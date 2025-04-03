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
        headers={
            "Content-type" : "application/json",
            "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
            "authorization" : "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IkNOdjBPSTNSd3FsSEZFVm5hb01Bc2hDSDJYRSIsImtpZCI6IkNOdjBPSTNSd3FsSEZFVm5hb01Bc2hDSDJYRSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuYXp1cmUuY29tIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNzJmOTg4YmYtODZmMS00MWFmLTkxYWItMmQ3Y2QwMTFkYjQ3LyIsImlhdCI6MTc0MzQwOTcxOCwibmJmIjoxNzQzNDA5NzE4LCJleHAiOjE3NDM0MTQ5NDMsImFjciI6IjEiLCJhaW8iOiJBYVFBVy84WkFBQUFHVDA3MUc1VnVPV2s4UDVkMU5IejF0aXllUGp3dkdFbXUvQjBqUHZPcjlSY05sSjMvQjYzOHNmem16U3JiSlZIdkJ5NzNJTVplZ0ZiL1dxS1hEK0cvU3diZUhJZnVRNVJqZ0RMbWthV0lIb2VWWm91VXBoTHk2OTZjay80TEZObCtlNUJEb05zeUNTUS9qcVg2SjNGY05ScEJleUI0bk5zaHZsbkl0Vnl4dUtOZitjWkVvM1duay9vNnBDeFlzNXFuSzJhMHY5SDVEZVhFK1pTRHVRa2NBPT0iLCJhbXIiOlsicnNhIiwibWZhIl0sImFwcGlkIjoiODM1YjJhNzMtNmUxMC00YWE1LWE5NzktMjFkZmRhNDUyMzFjIiwiYXBwaWRhY3IiOiIwIiwiZGV2aWNlaWQiOiJiNzhkZDFlZS0xMjdiLTRiY2UtYTBlZC05M2IzNDUxZmZlMmUiLCJmYW1pbHlfbmFtZSI6IkxpIiwiZ2l2ZW5fbmFtZSI6IllpeHVlIiwiaGFzZ3JvdXBzIjoidHJ1ZSIsImlkdHlwIjoidXNlciIsImlwYWRkciI6IjExMi4yNTMuMTguMjA0IiwibmFtZSI6IllpeHVlIExpIChXSUNSRVNPRlQgTk9SVEggQU1FUklDQSBMVEQpIiwib2lkIjoiMjkyZGIyYTYtNDY2Ny00ZTE5LTg0MDYtYWYzZWI5Nzc4YjY0Iiwib25wcmVtX3NpZCI6IlMtMS01LTIxLTIxMjc1MjExODQtMTYwNDAxMjkyMC0xODg3OTI3NTI3LTc3MzQxNDEyIiwicHVpZCI6IjEwMDMyMDAzOEU3N0U5QzUiLCJyaCI6IjEuQVJvQXY0ajVjdkdHcjBHUnF5MTgwQkhiUjBaSWYza0F1dGRQdWtQYXdmajJNQk1hQUxrYUFBLiIsInNjcCI6InVzZXJfaW1wZXJzb25hdGlvbiIsInNpZCI6IjAwMGZiZjU5LWQyNDAtNjA0Yy0wMWNlLTg3NGRkYmE3MjYyZiIsInN1YiI6ImMxUU5NZXJmVTlwdXM5N0ZWV3JiUi1TUk5iLTY3T2pGZ0VCclB5TlM5R1EiLCJ0aWQiOiI3MmY5ODhiZi04NmYxLTQxYWYtOTFhYi0yZDdjZDAxMWRiNDciLCJ1bmlxdWVfbmFtZSI6InYteWl4dWVsaUBtaWNyb3NvZnQuY29tIiwidXBuIjoidi15aXh1ZWxpQG1pY3Jvc29mdC5jb20iLCJ1dGkiOiJiNEg2VU5IWlUwbV84bV96Ujg0c0FBIiwidmVyIjoiMS4wIiwieG1zX2lkcmVsIjoiMjYgMSIsInhtc190Y2R0IjoxMjg5MjQxNTQ3fQ.S28hD8ih8LTu9_TdiIrQ0-J6Ok-jEHu0Zpz9Vs9nx6gBimAvOdpTnyMz50gr-SmwRvtDz602xoXwYnIcUXOIRCqpYBwQyNDWfEXStpHVWp2eTX-ueCp7izfEJ4zflHBF2O0W8RaRHo18sq_Pjl3DqxHetSl5KEr5pySn9gy-XQYIA3aDY3wfqHjehFKKzVH6rsRWxF7Fx1HkWx0_tmvy09VKns25L776fv548SvoWrJ4h1Q1K_OuCvSvTjZRK0DLpsQnEcIaTrKcK-N2vI0kaX0b1plT3tp8iBaA0LxidY1UHS21sR2S_EntSA565drxQTzcf8lKoUsUSyhIEEG9hQ"
        }

        return request_url,vm_pool_url,users_url,headers