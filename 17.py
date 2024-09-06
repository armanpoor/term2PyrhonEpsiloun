#json
# import json
# json_data = '{"name":"mehrzaz", "age":26, "isteacher":True, "isstudent":False, "adreses":["bnd,sdfsdf,sdfsf,sdfd", "esfahan,sdfsdsf,sdfsdf"]}'

# data = json.loads(json_data)

# print(type(data))


import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
print(type(y))

