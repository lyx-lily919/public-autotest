import requests
import logging

class vm_pool_function():

    def all_vm_state(self,vm_pool_url,users_url,headers):

        users_response=requests.get(users_url,headers=headers)
        users_data=users_response.json()
        user_map={user["id"]:user["properties"]["email"] for user in users_data["value"]}  

        all_vm_response=requests.get(url=vm_pool_url,headers=headers)
        all_vm_data=all_vm_response.json()

        for i in all_vm_data["value"]:
            if i["properties"].get("vmType")=="Template":
                vm_state=i["properties"]["state"]
                vm_type=i["properties"]["vmType"]
                logging.info(f"vmType:{vm_type},state:{vm_state}")
            if i["properties"].get("vmType")=="User":
                vm_state=i["properties"]["state"]
                vm_type=i["properties"]["vmType"]
                if "claimedByUserId" in i["properties"]:
                    user_id=i["properties"]["claimedByUserId"]
                    user_name=user_map.get(user_id,"Unknown User")
                    logging.info(f"vmType:{vm_type},{user_name}:{vm_state}")
                else:
                    logging.info(f"vmType:{vm_type},User not claimed:{vm_state}")
