import os

from requests.auth import HTTPBasicAuth
from teamcity.api import TeamcityApi
from teamcity.exceptions import TCException
from teamcity.utils import Utils


class Teamcity(TeamcityApi):
    """Teamcity connector and environment
    
    :param object: Default class inherited
    :type object: obj
    """
    def __init__(self, *args, **kwargs):
        """Initialize Teamcity object

        """
        super().__init__(*args, **kwargs)
        self._generate_api_endpoint()
    
    def _generate_api_endpoint(self):
        auth = os.environ.get('TEAMCITY_GUEST_AUTH')
        if self.username and self.password:
            auth = os.environ.get('TEAMCITY_BASIC_AUTH')
            self.auth = HTTPBasicAuth(self.username, self.password)
        self.api_endpoint = "{base_url}/{auth}".format(base_url=self.base_url, auth=auth)
    
    @classmethod
    def from_environ(cls):
        return Api(
            username=os.environ.get('TEAMCITY_USERNAME'),
            password=os.environ.get('TEAMCITY_PASSWORD'),
            scheme=os.environ.get('TEAMCITY_SCHEME'),
            host=os.environ.get('TEAMCITY_HOST')
        )
    
    @property
    def server_info(self):
        url = "{api}/{server}".format(api=self.api_endpoint, server="app/rest/server")
        response = self.session.get(url)
        if not response.ok:
            raise TCException(status_code=response.status_code, reason=response.reason, message=response.text)
        
        data = response.json()
        version_dict={
            'version': data['version'],
            'version_major': data['versionMajor'],
            'version_minor': data['versionMinor'],
        }
        time_dict = {
            'start_time_str': data['startTime'],
            'current_time_str': data['currentTime'],
            'build_date_str': data['buildDate']
        }
        return TeamcityServer(
            build_number=data['buildNumber'],
            internal_id=data['internalId'],
            web_url=data['webUrl'],
            version_dict=version_dict,
            time_dict=time_dict
        )
    
    def plugins(self):
        url = "{api}/{plugin}".format(api=self.api_endpoint, plugin="app/rest/server/plugins")
        response = self.session.get(url)
        if not response.ok:
            raise TCException(status_code=response.status_code, reason=response.reason, message=response.text)
        
        data = response.json()
        plugins = []
        for plugin in data['plugin']:
            plugin_obj = Plugin(
                name=plugin.get("name"),
                display_name=plugin.get("displayName"),
                version=plugin.get("version"),
                load_path=plugin.get("loadPath")
            )
            if "parameters" in plugin:
                prop_list = []
                plugin_property = plugin["parameters"]["property"]
                for prop in plugin_property:
                    prop_list.append(
                        Properties(
                            name=prop["name"],
                            value=prop["value"]
                        )
                    )
                plugin_obj.add_properties(prop_list)

            plugins.append(plugin_obj)
        return plugins
    
    def get_all_projects(self):
        self.get("/projects")


class Properties(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def __repr__(self):
        return "{0}:{1} name={2}, value={3}".format(self.__module__, self.__class__.__name__, self.name, self.value)

class Plugin(object):
    def __init__(self, name, display_name, version, load_path, properties=None):
        self.name = name
        self.display_name = display_name
        self.version = version
        self.load_path = load_path
        self.properties = properties
        self.property_count = len(properties) if properties else 0
    
    def __repr__(self):
        return "{0}:{1}: name={2}, display_name={3}, version={4}, parameters={5}".format(
            self.__module__, self.__class__.__name__, self.name, self.display_name, 
            self.version, self.property_count)
    
    def add_properties(self, properties):
        if properties:
            self.property_count = len(properties)
            self.properties = properties

class TeamcityServer(object):
    def __init__(self, build_number, internal_id, web_url, version_dict, time_dict):
        self.build_number = build_number
        self.internal_id = internal_id
        self.web_url = web_url
        self.version = version_dict['version']
        self.version_major = version_dict['version_major']
        self.version_minor = version_dict['version_minor']
        self.start_time_str = time_dict['start_time_str']
        self.current_time_str = time_dict['current_time_str']
        self.build_date_str = time_dict['build_date_str']
    
    def __repr__(self):
        return "<{0}.{1}: web_url={2} version={3}>".format(
            self.__module__, self.__class__.__name__, self.web_url, self.version)
    
    @property
    def start_time(self):
        return Utils.parse_date_str(self.start_time_str)
    
    @property
    def current_time(self):
        return Utils.parse_date_str(self.current_time_str)
    
    @property
    def build_date(self):
        return Utils.parse_date_str(self.build_date_str)
