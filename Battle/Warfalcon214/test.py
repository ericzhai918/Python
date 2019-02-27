import requests
from test_db import *

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; JSN-AL00a Build/HONORJSN-AL00a; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 MicroMessenger/7.0.3.1400(0x27000336) Process/appbrand0 NetType/WIFI Language/zh_CN',
    'apsid': '2d5cbd781531499fd0da16dcffb10170',
    'appid': 'wxf605def94f6a058b'
}


def get_html():
    for page in range(121):
        url = "https://apiopen.jingdaka.com/user/submitlist?limit=10&offset={}&search_user_name=&course_id=230969&record_at=2019-02-14".format(page * 10)

        try:
            response = requests.get(url, headers=headers, verify='F:\\charles-proxy-ssl-proxying-certificate.crt')
            if response.status_code == 200:
                # return response.json()
                get_messages(response.json())
            else:
                return -1
        except:
            return None


def get_messages(htmlPage):
    if htmlPage:
        items = htmlPage['data']['submit_list']
        info_box = {}
        for item in items:
            info_box['user_id'] = item.get('user_id')
            info_box['user_name'] = item.get('user_name')
            info_box['user_content'] = item.get('content')
            info_box['user_profile'] = item.get('avatar_url')
            info_box['user_pic'] = item.get('picture_list')
            info_box['user_createTime'] = item.get('created_at')
            if info_box['user_id']:
                insert_data(info_box)
            info_box = {}
            # yield info_box
    else:
        return None


def save_info_to_html(results):
    rows = ''

    for info_box in results:
        row = '<tr><td>{}</td><td>{}</td><td>{}</td><td><img src={} width=200 height=200></td><td><img src={} width=240px height=200px></td></tr>'.format(
            info_box['user_id'],
            info_box['user_name'],
            info_box['user_content'],
            info_box['user_profile'],
            info_box['user_pic'][0] if info_box['user_pic'] else '')
        rows = rows + '\n' + row
    info_box_html = '''
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>电影票房</title>

    </head>
    <body>
        <style>
        .table1_5 table {
            width:100%;
            margin:15px 0
        }
        .table1_5 th {
            background-color:#00BFFF;
            color:#FFFFFF
        }
        .table1_5,.table1_5 th,.table1_5 td
        {
            font-size:0.95em;
            text-align:center;
            padding:4px;
            border:1px solid #dddddd;
            border-collapse:collapse
        }
        .table1_5 tr:nth-child(odd){
            background-color:#aae9fe;
        }
        .table1_5 tr:nth-child(even){
            background-color:#fdfdfd;
        }
        </style>
        <table class='table1_5'>
        <tr>
        <th>用户ID</th>
        <th>用户昵称</th>
        <th>个人信息</th>
        <th>用户头像</th>
        <th>用户照片</th>
        </tr>
        ''' + rows + '''
        </table>
    </body>
    </html> 
        '''
    with open('E:\\PythonTest\\info_box.html', 'w', encoding='utf-8') as f:
        f.write(info_box_html)

if __name__ == '__main__':
    get_html()
    # htmlPage = get_html()
    # results = get_messages(htmlPage)
    # results = get_messages(get_html())
    #
    # save_info_to_html(results)
