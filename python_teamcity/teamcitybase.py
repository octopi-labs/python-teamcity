import ast

from teamcity.utils import api_url, strip_trailing_slash
from teamcity.exceptions import TeamcityAPIException


class TeamcityBase(object):
    """Base object for all teamcity objects. 
    All teamcity objects are inherited from this object.
    """

    def __init__(self, baseurl, poll=True):
        self._data = None
        self.baseurl = strip_trailing_slash(baseurl)
        if poll:
            self.poll()
    
    def _poll(self, tree=None):
        url = api_url(self.baseurl)
        return self.get_data(url, tree=tree)
    
    def get_teamcity_obj(self):
        raise NotImplementedError("Please implement this method on {error}".format(error=self.__class__.__name__))

    def poll(self, tree=None):
        data = self._poll(tree)
        # if 'projects' in data:
        #     data['projects'] = self.
        if not tree:
            self._data = data
            
        return data
    
    def get_data(self, url, params=None, tree=None):
        apirequest = self.get_teamcity_obj().apirequest
        if tree:
            if not params:
                params = {'tree': tree}
            else:
                params.update({'tree': tree})
        
        response = apirequest.get_request(url, params)
        if response.status_code != 200:
            response.raise_for_status()
        try:
            ast.literal_eval(response.text)
        except Exception as e:
            raise TeamcityAPIException('Cannot parse %s' % response.content)
