import requests
from bs4 import BeautifulSoup
import xlwt

def get_douban_list():
    for i in range(0, 250, 25):
        douban_url = "https://movie.douban.com/top250?start={0}&filter=".format(i)
        douban_list.append(douban_url)
    return douban_list

def getHtmlPage(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
    response = requests.get(url, headers=headers)
    htmlPage = response.text
    return htmlPage

def getInfoFromOnePage(htmlPage):
    soup = BeautifulSoup(htmlPage, 'html.parser')
    movies = soup.find('ol', class_='grid_view').find_all('li')
    for i in range(0, 25):
        movieName = movies[i].find('span').string
        movieScore = movies[i].find('span', class_='rating_num').string
        movieNum = movies[i].find('div', class_='star').find_all('span')[-1].string.strip('人评价')
        movieQuote = movies[i].find('p', class_='quote').find('span').string
        result.append([movieName, movieScore, movieNum, movieQuote])
    return result

if '__main__':
    douban_list = []
    result = []

    #得到豆瓣电影list
    for i in get_douban_list():
        htmlPage = getHtmlPage(i)
        result = getInfoFromOnePage(htmlPage)
    result.insert(0, ['电影名', '评分', '评价人数', '短评'])

    #存入excel
    book = xlwt.Workbook()
    sheet = book.add_sheet('movie_sheet')
    for row in range(0, 251):
        for col in range(0, 4):
            sheet.write(row, col, result[row][col])
    book.save('test.xls')
