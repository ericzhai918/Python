import requests
import re


def get_all(city_list):
    url = 'http://%s.meituan.com/meishi/pn%s/'
    for city in city_list.split(','):
        for i in range(32):
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
                'Host': '%s.meituan.com' % (city),
                'Referer': 'http://%s.meituan.com/meishi/' % (city),
                'Upgrade-Insecure-Requests': '1',
            }
            r = requests.get(url % (city, i + 1), headers=headers)
            find_poiId = re.findall('"poiId":(\d+.*?),', r.text)
            find_uuid = re.findall('"uuid":"(.*?)",', r.text)
            get_info(find_poiId, city, find_uuid)
            print(find_poiId)


def get_info(find_poiId, city, find_uuid):
    pass
