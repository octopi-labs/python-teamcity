from teamcity import Teamcity

test = Teamcity("http", "localhost", 8111, "srahul07", "rahul")
print(test.connector.text)