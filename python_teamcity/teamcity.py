
import json
import logging
import os
import re
import socket
import sys
import time
import warnings

from teamcity.teamcitybase import TeamcityBase
from teamcity.apirequest import ApiRequest
from teamcity.utils import api_url
# from teamcity import TeamcityBase
# from teamcity import ApiRequest
# from teamcity import api_url


class Teamcity(TeamcityBase):
    """Represents teamcity environment.
    
    :param TeamcityBase: Base class for all teamcity objects
    :type TeamcityBase: object
    """
    
    def __init__(self, url, username=None, password=None, ssl_verify=True, cert=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        """Initialize Teamcity connection
        
        :param url: Baseurl for teamcity instance including port
        :type url: str
        :param username: username for teamcity auth, defaults to None
        :param username: str, optional
        :param password: password for teamcity auth, defaults to None
        :param password: str, optional
        :param timeout: timeout for teamcity rest api request, defaults to socket._GLOBAL_DEFAULT_TIMEOUT
        :param timeout: int, optional
        """
        self.username = username
        self.password = password
        self.apirequest = ApiRequest(username, password, baseurl=url, ssl_verify=ssl_verify, cert=cert, timeout=time)
        self.apirequest.timeout = timeout
        self.projects_container = None
        super(Teamcity, self).__init__(url, True)
        # super().__init__(self, url, True)
    
    def get_teamcity_obj(self):
        return self

    def _poll(self, tree=None):
        url = api_url(self.baseurl)
        return self.get_data(url, tree='jobs[name, color, url]' if not tree else tree)
        
