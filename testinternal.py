from jsonparse import *
#some_json = '{"key":{"internal-key":69,"another-key":420},"wtf":69420}'
some_json = '{"foo": [1, 2, {"bar": 2}]}'
a = separate_json(some_json)
b,c = parse_json(a)
print(b)