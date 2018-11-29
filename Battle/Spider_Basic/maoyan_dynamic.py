import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}

def get_html():
    url = 'https://box.maoyan.com/promovie/api/box/second.json'
    try:
        response =requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return -1
    except:
        return None

def parse_infor(json):
    if json:
        items = json.get('data').get('list')
        for item in items:
            box_office = {}
            box_office['电影名'] = item.get('movieName')
            box_office['上映信息'] = item.get('releaseInfo')
            box_office['综合票房'] = item.get('boxInfo')
            box_office['票房占比'] = item.get('boxRate')
            box_office['累计票房'] = item.get('sumBoxInfo')
            yield box_office
    else:
        return None

def save_infor(results):
    pass
    rows = ''
    for box_office in results:
        row = '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(box_office['电影名'],box_office['上映信息'],box_office['综合票房'],box_office['票房占比'],box_office['累计票房'])
        rows = rows + '\n' + row
    box_office_html = '''
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
    <th>电影名</th>
    <th>上映信息</th>
    <th>综合票房</th>
    <th>票房占比</th>
    <th>累计票房</th>
    </tr>
    ''' + rows + '''
    </table>
</body>
</html> 
    '''
    with open('E:\\PythonTest\\box_office.html','w',encoding='utf-8') as f:
        f.write(box_office_html)

if __name__ == "__main__":
    json = get_html()
    results = parse_infor(json)
    save_infor(results)
