import platform
import re

import dateutil
from teamcity.config import TEAMCITY_API


class Utils(object):
    """Utility functionalities for teamcity
    
    :param object: default inherited features
    :type object: obj
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def python_version(cls, version_type="major"):
        """Get version of the python used
        
        :param version_type: version type, defaults to "major"
        :param version_type: str, optional
        :return: version number
        :rtype: str
        """
        version = platform.python_version_tuple()
        return version[0] if version_type == "major" else version[1]
    
    @classmethod
    def api_url(cls, url):
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
    def strip_trailing_slash(cls, url):
        """Strip trailing slash from the url
        
        :param url: URL to be checked for slash at the end
        :type url: str
        :return: Stripped URL
        :rtype: str
        """
        while url.endswith('/'):
            url = url[:-1]
        return url
    
    @classmethod
    def parse_date_str(cls, date_str):
        """Parse string to date
        
        :param date_str: date in string
        :type date_str: str
        :return: date object
        :rtype: obj
        """
        return dateutil.parser.parse(date_str)
    
    @classmethod
    def cleanhtml(cls, raw_html):
        """clean html from response and retrieve text message
        
        :param raw_html: raw html string
        :type raw_html: str
        :return: clean message string
        :rtype: str
        """
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', raw_html)
        return cleantext


if __name__=="__main__":
    print(Utils.python_version("minor"))
