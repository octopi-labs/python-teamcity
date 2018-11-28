
from teamcity import config

def api_url(url):
    """Get API URL
    
    :param url: URL to be checked if proper in format
    :type url: str
    :return: Stripped URL
    :rtype: str
    """
    if not url.endswith(config.TEAMCITY_API):
        fmt = None
        if url.endswith(r"/"):
            fmt = "{url}{api}"
        else:
            fmt = "{url}/{api}"
        url = fmt.format(url=url, api=config.TEAMCITY_API)

    return url


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