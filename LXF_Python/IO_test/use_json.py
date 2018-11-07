import json

#Python对象到JSON格式的转换
d = dict(name='Bob',age=20,score=88)
json_str= json.dumps(d)
print("Python内置的数据类型为:",d)
print(type(d))
print('经Json格式转换后:',b)
print(type(json_str))

#JSON格式转换Python对象
json_str = '{"age":20,"score":88,"name":"bob"}'
d = json.loads(json_str)
print(d)
print(type(json_str))
print(type(d))
