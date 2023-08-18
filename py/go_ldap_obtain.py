import requests
import jwt
import yaml
import os

class go_ldap_obtain(object):

    def __init__(self):

        '''
            Get config location from env "config_loc" 
        '''

        config_location = os.getenv("config_loc")
        with open(config_location, 'r') as yaml_file:
            self.configData = yaml.safe_load(yaml_file)

        '''
            Get the necessary parameters from the provided yaml with "ldap"
        '''

        try:
            loginEndpoint = self.configData["ldap"]["ldapWebEndpoint"]
            username = self.configData["ldap"]["username"]
            password = self.configData["ldap"]["password"]
            protocols = self.configData["ldap"]["protocols"]
            port = self.configData["ldap"]["port"]
            self.info = {
                "ldapLoginEndpoint":loginEndpoint,
                "username":username,
                "password":password,
                "protocols":protocols,
                "port":port
                }

        except Exception():
            raise RuntimeError("The content of the provided yaml does not conform to the specification")
        
    def jwt_token_access(self):

        '''
            Get jwt token from server with provided info
        '''

        targetUrl = f"{self.info['protocols']}://{self.info['ldapWebEndpoint']}:{self.info['port']}/api/base/login"
        headers = {
            "Content-Type": "application/json; charset=utf-8"
        }
        data = {
            "username": self.info["username"],
            "password": self.info["password"]
        }

        response = requests.post(targetUrl, headers=headers, json=data)

        if response.status_code == 200:
            print("Request was successful!")
            return response["data"]["token"] 
        else:
            raise RuntimeError("Request failed with status code:", response.status_code)
        
    def avatar_url_request(self,access_token):

        '''
            Request for target avatar url
        '''

        targetUrl = f"{self.info['protocols']}://{self.info['ldapWebEndpoint']}:{self.info['port']}/api/user/avatar"
        headers = {
            "Content-Type" : "application/json; charset=utf-8",
            "Authorization": f"Bearer {access_token}"
        }
        cookies = {
            "gowebmini-Token" : access_token
        }

        response = requests.get(targetUrl, headers = headers, cookies = cookies)
