from teamcity import Teamcity

# test = Teamcity("http", "localhost", 8111, "srahul07", "rahul")
# print(test.connector.text)

test = Teamcity("srahul07", "rahul", scheme="http", host="localhost", port=8111)
print(test.connector.text)
