import platform

from teamcity.config import TEAMCITY_API

class Utils(object):
    """Utility functionalities for teamcity
    
    :param object: default inherited features
    :type object: obj
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def python_version(version_type="major"):
        """Get version of the python used
        
        :param version_type: version type, defaults to "major"
        :param version_type: str, optional
        :return: version number
        :rtype: str
        """
        version = platform.python_version_tuple()
        return version[0] if version_type == "major" else version[1]
    
    @classmethod
    def api_url(url):
        """Get API URL
        
        :param url: URL to be checked if proper in format
        :type url: str
        :return: Stripped URL
        :rtype: str
        """
        if not url.endswith(TEAMCITY_API):
            fmt = None
            if url.endswith(r"/"):
                fmt = "{url}{api}"
            else:
                fmt = "{url}/{api}"
            url = fmt.format(url=url, api=TEAMCITY_API)

        return url

    @classmethod
    def strip_trailing_slash(url):
        """Strip trailing slash from the url
        
        :param url: URL to be checked for slash at the end
        :type url: str
        :return: Stripped URL
        :rtype: str
        """
        while url.endswith('/'):
            url = url[:-1]
        return url


if __name__=="__main__":
    print(Utils.python_version("minor"))
