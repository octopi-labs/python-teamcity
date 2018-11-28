import requests

from teamcity.config import TEAMCITY_API, TEAMCITY_BASIC_AUTH

class Teamcity(object):
    """Teamcity connector and environment
    
    :param object: Default class inherited
    :type object: obj
    """
    def __init__(self, scheme, host, port, username, password):
        self.baseurl = self._generate_url(scheme, host, port)
        self.username = username
        self.password = password
        self.connector = self._connect()
    
    def _generate_url(self, scheme, host, port):
        return "{scheme}://{host}:{port}".format(scheme=scheme, host=host, port=port)
    
    def _connect(self):
        return requests.get(self.baseurl + "/{auth}/{api}".format(auth=TEAMCITY_BASIC_AUTH, api=TEAMCITY_API), data={}, auth=(self.username, self.password))