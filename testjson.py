from jsonparse import *
some_json = '{"lol":69,"rofl":420,"omg":"wtf","stuff":[69,"four-twenty"],"another":"thing","even-more":["stuff",420]}'
a = separate_json(some_json)
b = parse_json(a)
print(b)