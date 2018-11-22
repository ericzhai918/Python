import requests

url = 'http://www.weather.com.cn/data/sk/101020100.html'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
}

html = requests.get(url, headers=headers)
html.encoding = 'utf-8'
html = html.json()
print(html)

city = html['weatherinfo']['city']
time = html['weatherinfo']['time']
temperature = html['weatherinfo']['temp']
print('{}市,今天{},温度是：{}'.format(city,time,temperature))

