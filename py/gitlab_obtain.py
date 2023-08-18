import gitlab

class gitlab_obtain(object):

    def __init__(self,gitlabLinks):

        self.gl=gitlabLinks

    def get_userName(self):
        '''
            Obtain all users info with returns like [(id,commit_email)...] 
        '''
        return self.gl.users.list(iterator=True)

    