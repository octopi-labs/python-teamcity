from teamcity import Teamcity
from teamcity.config import TEAMCITY_URL, TEAMCITY_USERNAME, TEAMCITY_PASSWORD

teamcity = Teamcity(TEAMCITY_URL, TEAMCITY_USERNAME, TEAMCITY_PASSWORD)
print(teamcity)