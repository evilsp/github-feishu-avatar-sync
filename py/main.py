import go_ldap_obtain as g_l_obt
import gitlab_contact as g_cta
import gitlab_changes as g_cge
import gitlab_obtain  as g_obt
import os
import sys

os.environ.setdefault("config_loc","./config.yaml")
sys.path.append('./')


gitlab_contact=g_cta.gitlab_contact()
go_ldap_obtain=g_l_obt.go_ldap_obtain()
gl=gitlab_contact.gitlab_connect()
gitlab_obtain=g_obt.gitlab_obtain(gl)
iterator=gitlab_obtain.get_userName()
gitlab_changes=g_cge.gitlab_changes(gl)
print(gitlab_changes.changeAvater(iterator))
    

