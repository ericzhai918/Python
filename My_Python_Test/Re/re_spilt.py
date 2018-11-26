import re

line = 'asdf fjdk; afed, fjek,asdf, foo'

a = re.split(r'[;,\s]\s*', line)
print(a)
