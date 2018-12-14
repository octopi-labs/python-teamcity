import os
from teamcity import Teamcity

from teamcity.config import TEAMCITY_BASIC_AUTH, TEAMCITY_GUEST_AUTH

os.environ['TEAMCITY_USERNAME'] = "srahul07"
os.environ['TEAMCITY_PASSWORD'] = "rahul"
os.environ['TEAMCITY_SCHEME'] = "http"
os.environ['TEAMCITY_HOST'] = "localhost"
os.environ['TEAMCITY_PORT'] = str(8111)

os.environ['TEAMCITY_BASIC_AUTH'] = TEAMCITY_BASIC_AUTH
os.environ['TEAMCITY_GUEST_AUTH'] = TEAMCITY_GUEST_AUTH

test = Teamcity("srahul07", "rahul", scheme="http", host="localhost", port=8111)
print(test.server_info)
# print(test.plugins())
