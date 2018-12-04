from teamcity.api import Api
from teamcity.config import (TEAMCITY_API, TEAMCITY_BASIC_AUTH,
                             TEAMCITY_GUEST_AUTH, TIMEOUT)


class Teamcity(Api):
    """Teamcity connector and environment
    
    :param object: Default class inherited
    :type object: obj
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        auth = TEAMCITY_BASIC_AUTH if self.username else TEAMCITY_GUEST_AUTH
        self.url = self.baseurl + "/{auth}/{api}".format(auth=auth, api=TEAMCITY_API)
    
    def get_all_projects(self):
        self.get("/projects")
