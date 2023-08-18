import gitlab

class gitlab_obtain(object):

    def __init__(self,gitlabLinks):

        self.gl=gitlabLinks

    def get_commitEmails(self):
        '''
            Obtain all users info with returns like [(id,commit_email)...] 
        '''
        commitEmailList=[]
        for gitlabObject in self.gl.users.list(iterator=True):
            info = gitlabObject.asdict()
            commitEmailList.append({"id":info["id"],"commit_email":info["commit_email"]})

    