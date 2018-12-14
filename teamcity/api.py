import os
import platform

import requests
from requests.auth import HTTPBasicAuth

if int(platform.python_version_tuple()[0]) >= 3:
    from urllib.parse import urlparse
else:
    from urlparse import urlparse


class TeamcityApi(object):
    """Api request, to send requests to server
    
    :param object: default python object
    :type object: obj
    """
    def __init__(self, username, password, scheme="http", host="localhost", port=8111, **kwargs):
        """Initialize teamcity object
        
        :param username: Teamcity username
        :type username: str
        :param password: Teamcity password for username
        :type password: str
        :param scheme: scheme / protocol to access server, defaults to "http"
        :param scheme: str, optional
        :param host: host for server, defaults to "localhost"
        :param host: str, optional
        :param port: port number to access teamcity, defaults to 8111
        :param port: int, optional
        """
        self.username = username if username else os.environ.get('TEAMCITY_USERNAME')
        self.password = password if password else os.environ.get('TEAMCITY_PASSWORD')
        self.protocol = scheme
        self.host = host
        self.port = port
         
        self.session = kwargs.get('session', requests.Session())
        self.session.auth = HTTPBasicAuth(self.username, self.password)
        self.session.headers['Accept'] = "application/json"
        self.timeout = kwargs.get('timeout', os.environ.get('TIMEOUT'))
        self.api_endpoint = None
        self.auth = None

        self.base_url = self._generate_url()
        # self.ssl_verify = kwargs.get('ssl_verify', True)
        # self.cert = kwargs.get('cert', None)
    
    def _generate_url(self):
        """Generate base URL from protocol, host and port
        
        :return: base url
        :rtype: str
        """
        base_url = "{scheme}://{host}".format(scheme=self.protocol, host=self.host)
        if self.port not in [80, 443]:
            base_url += ":{port}".format(port=self.port)
        return base_url
    
    def _update_url_scheme(self, url):
        """Updates scheme of given url to the one used in Teamcity baseurl.
        
        :param url: URL for which scheme needs to be changed
        :type url: str
        :return: Updated URL
        :rtype: str
        """
        if self.base_scheme and not url.startswith("{scheme}://".format(scheme=self.base_scheme)):
            url_split = urlparse.urlsplit(url)
            url = urlparse.urlunsplit(
                [
                    self.base_scheme,
                    url_split.netloc,
                    url_split.path,
                    url_split.query,
                    url_split.fragment
                ]
            )
        return url
    
    def get_request_dict(self, params=None, data=None, files=None, headers=None, **kwargs):
        request_kwargs = kwargs
        if self.username:
            request_kwargs['auth'] = (self.username, self.password)

        if params:
            assert isinstance(params, dict), "Params must be a dict, got {error}".format(error=repr(params))
            request_kwargs['params'] = params

        if headers:
            assert isinstance(headers, dict), "Headers must be a dict, got {error}".format(error=repr(headers))
            request_kwargs['headers'] = headers

        request_kwargs['verify'] = self.ssl_verify
        request_kwargs['cert'] = self.cert

        if data:
            request_kwargs['data'] = data

        if files:
            request_kwargs['files'] = files

        request_kwargs['timeout'] = self.timeout

        return request_kwargs

    def get(self, url, params=None, headers=None, allow_redirects=True, stream=False):
        request_kwargs = self.get_request_dict(
            params=params,
            headers=headers,
            allow_redirects=allow_redirects,
            stream=stream
        )
        
        return self.session.get(self._update_url_scheme(url), **request_kwargs)

    def post(self, url, params=None, data=None, files=None, headers=None, allow_redirects=True, **kwargs):
        request_kwargs = self.get_request_dict(
            params=params,
            data=data,
            files=files,
            headers=headers,
            allow_redirects=allow_redirects,
            **kwargs)

        return self.session.post(self._update_url_scheme(url), **request_kwargs)
