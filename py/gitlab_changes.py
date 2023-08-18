import os
import yaml
from datetime import datetime
import pytz
from gitlab.base import RESTObjectList
import go_ldap_obtain as g_l_obt
import png_compress

class gitlab_changes(object):

    def __init__(self,gitlabLinks):

        self.gl=gitlabLinks

    def parse(self):

        '''
            Get config location from env "config_loc" 
        '''

        config_location=os.getenv("config_loc")
        with open(config_location, 'r') as yaml_file:
            self.configData = yaml.safe_load(yaml_file)

        '''
            Get the necessary parameters from the provided yaml with "gitlab"
        '''

        try:
            self.avatarSaveLocation = self.configData["gitlab"]["avatarSaveLocation"]
            self.timeZone = self.configData["timeZone"]

        except Exception():
            raise RuntimeError("The content of the provided yaml does not conform to the specification")
        
    def timeGet(self):
        '''
            Get time at targetTimeZone from timeZone values
        '''
        target_timezone = pytz.timezone(self.timeZone)
        current_time = datetime.now(target_timezone)
        self.formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S %Z %z')

    def changeAvater(self,info:RESTObjectList):
        '''
            change user avatar by input dicts formatted like {{"id":id,"filePath":path}}
        '''
        go_ldap_obtain=g_l_obt.go_ldap_obtain()
        self.parse()
        os.makedirs(f"{self.avatarSaveLocation}",exist_ok=True)
        for gitlabObject in self.gl.users.list(iterator=True):
            info = gitlabObject.asdict() # Obtain username
            url = go_ldap_obtain.avatar_url_request(info["username"]) # Obtain url
            pngSaveAsSource = f"{self.avatarSaveLocation}/{info['username']}_source.png"
            pngSaveAscompressed = f"{self.avatarSaveLocation}/{info['username']}_compressed.png"
            result=go_ldap_obtain.file_reserve_request(pngSaveAsSource,url) # Save avatar file at target location
            if result == "None":
                continue
            else:
                png_compress.compress_png(pngSaveAsSource,pngSaveAscompressed,200) #compress png file
                user = self.gl.users.get(info["id"]) # get user
                with open(pngSaveAscompressed,'rb') as avatarFile: # changeAvatar
                    user.avatar = avatarFile
                    user.save()
        print(f"Update success at {self.formatted_time}")
        return "Success"