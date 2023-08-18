import gitlab
import yaml
import os

class gitlab_contact(object):

    def __init__(self):

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
            adminPersonalSecret = self.configData["gitlab"]["adminPersonalSecret"]
            gitlabEndpoint = self.configData["gitlab"]["gitlabEndpoint"]
            protocols = self.configData["gitlab"]["protocols"]
            port = self.configData["gitlab"]["port"]
            self.info = {
                "adminPersonalSecret":adminPersonalSecret,
                "gitlabEndpoint":gitlabEndpoint,
                "protocols":protocols,
                "port":port
                }

        except Exception():
            raise RuntimeError("The content of the provided yaml does not conform to the specification")

    def gitlab_connect(self):
        '''
            Build gitlab connection
        '''
        targetUrl = f"{self.info['protocols']}://{self.info['gitlabEndpoint']}:{self.info['port']}"
        gl = gitlab.Gitlab(url=targetUrl, private_token=self.info['adminPersonalSecret'], keep_base_url=True)
        return gl
        