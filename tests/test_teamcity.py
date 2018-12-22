import pytest

from teamcity.teamcity import Teamcity


class TestTeamcity(object):

    def test_username_password(self):
        teamcity = Teamcity("srahul07", "rahul")
        assert teamcity.username == "srahul07"
        assert teamcity.password == "rahul"

    def test_default_initial_connect(self):
        teamcity = Teamcity("srahul07", "rahul")
        assert teamcity.api_endpoint != "http://localhost:8111/httpAuth"