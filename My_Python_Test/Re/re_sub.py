import re

phone = '2004-959-559 # 这是一个电话号码'

num = re.sub(r'#.*$', '', phone)
print('My phone number:', num)

num = re.sub(r'\D','',phone)
print('My phone number:', num)
