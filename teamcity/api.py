import platform

import requests
from requests.auth import HTTPBasicAuth
from teamcity.config import (TEAMCITY_API, TEAMCITY_BASIC_AUTH,
                             TEAMCITY_GUEST_AUTH, TIMEOUT)

if int(platform.python_version_tuple()[0]) >= 3:
    from urllib.parse import urlparse
else:
    from urlparse import urlparse



class Api(object):
    """Api request, to send requests to server
    
    :param object: default python object
    :type object: obj
    """
    def __init__(self, *args, **kwargs):
        """Initialize Api request
        """
        if args:
            try:
                username, password = args
            except ValueError as error:
                raise error
        else:
            username = None
            password = None
        
        self.base_scheme = kwargs.get('scheme')
        self.baseurl = self._generate_url(kwargs.get('scheme'), kwargs.get('host'), kwargs.get('port'))
        self.username = username
        self.password = password
        self.timeout = kwargs.get('timeout', TIMEOUT)
        self.ssl_verify = kwargs.get('ssl_verify', True)
        self.cert = kwargs.get('cert', None)
        self.session = requests.Session()
        self.connector = self._connect()
    
    def _generate_url(self, scheme, host, port):
        return "{scheme}://{host}:{port}".format(scheme=scheme, host=host, port=port)

    def _create_session(self):
        if not self.session.cookies:
            self.session.auth = HTTPBasicAuth(self.username, self.password)

    def _connect(self):
        auth = TEAMCITY_BASIC_AUTH if self.username else TEAMCITY_GUEST_AUTH
        url = self.baseurl + "/{auth}/{api}".format(auth=auth, api=TEAMCITY_API)
        return self.get(url)
    
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
        self._create_session()
        request_kwargs = self.get_request_dict(
            params=params,
            headers=headers,
            allow_redirects=allow_redirects,
            stream=stream
        )
        
        return self.session.get(self._update_url_scheme(url), **request_kwargs)

    def post(self, url, params=None, data=None, files=None, headers=None, allow_redirects=True, **kwargs):
        self._create_session()
        request_kwargs = self.get_request_dict(
            params=params,
            data=data,
            files=files,
            headers=headers,
            allow_redirects=allow_redirects,
            **kwargs)

        return self.session.post(self._update_url_scheme(url), **request_kwargs)
