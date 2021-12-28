import urllib.request
import json
import ast
from settings import SMASHRUN_TOKEN
byte_str = urllib.request.urlopen("https://api.smashrun.com/v1/my/activities/search/briefs?count=1&access_token=" + SMASHRUN_TOKEN).read()

str_str = byte_str.decode('utf-8').strip("[]")

json_str = json.loads(str_str)

print(type(json_str))
print(len(json_str))
print(json_str["distance"])
