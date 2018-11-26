import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'dog', line, re.M | re.I)
searchObj = re.search(r'dog', line, re.M | re.I)

if matchObj:
    print(matchObj.group())
else:
    print('No match')

if searchObj:
    print(searchObj.group())
else:
    print('No match')