import requests

import platform

if platform.python_version() < 3:
    from urlparse import urlparse
else:
    from urllib.parse import urlparse

import config

class ApiRequest(object):
    """Api Request object
    """

    def __init__(self, *args, **kwargs):
        """Initialize API request
        
        :raises error: Value error, if username and password is not provided
        """
        if args:
            try:
                username, password = args
            except ValueError as error:
                raise error
        else:
            username = None
            password = None
        
        baseurl = kwargs.get('baseurl', None)
        self.base_scheme = urlparse(baseurl).scheme if baseurl else None
        self.username = username
        self.password = password
        self.timeout = kwargs.get('timeout', config.TIMEOUT)
        self.ssl_verify = kwargs.get('ssl_verify', True)
        self.cert = kwargs.get('cert', None)
    
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

    def get_request(self, url, params=None, headers=None, allow_redirects=True, stream=False):
        request_kwargs = self.get_request_dict(
            params=params,
            headers=headers,
            allow_redirects=allow_redirects,
            stream=stream
        )

        return requests.get(self._update_url_scheme(url), **request_kwargs)

    def post_request(self, url, params=None, data=None, files=None, headers=None, allow_redirects=True, **kwargs):
        request_kwargs = self.get_request_dict(
            params=params,
            data=data,
            files=files,
            headers=headers,
            allow_redirects=allow_redirects,
            **kwargs)

        return requests.post(self._update_url_scheme(url), **request_kwargs)

