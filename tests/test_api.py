import pytest

from teamcity.api import TeamcityApi


@pytest.fixture
def username():
    ''' Username for the tests
    '''
    return "srahul07"

@pytest.fixture
def password():
    """ Password for the tests
    """
    return "rahul"

class TestTeamcityApi(object):

    def test_default_initial_connect(self, username, password):
        teamcity_api = TeamcityApi(username, password)
        assert teamcity_api.protocol == "http"
        assert teamcity_api.host == "localhost"
        assert teamcity_api.port == 8111

    @pytest.mark.parametrize("scheme, host, port", [
        ("http", "localhost", "8111")
        ])
    def test_setting_initial_connect(self, username, password, scheme, host, port):
        teamcity_api = TeamcityApi(username, password, scheme, host, port)
        assert teamcity_api.protocol == "http"
        assert teamcity_api.host == "localhost"
        assert teamcity_api.port == 8111