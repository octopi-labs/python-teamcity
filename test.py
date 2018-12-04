from teamcity import Teamcity

test = Teamcity("srahul07", "rahul", scheme="http", host="localhost", port=8111)
print(test.session.cookies.get_dict())
