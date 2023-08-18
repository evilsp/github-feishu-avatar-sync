import gitlab

class gitlab_changes(object):

    def __init__(self,gitlabLinks):

        self.gl=gitlabLinks

    def changeAvater(self,info:dict):
        '''
            change user avatar by input dicts formatted like {{"id":id,"filePath":path}}
        '''
        commitEmailList = []
        for gitlabObject in self.gl.users.list(iterator=True):
            info = gitlabObject.asdict()
            commitEmailList.append(info["id"],info["commit_email"])