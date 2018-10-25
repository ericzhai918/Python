import requests
from bs4 import BeautifulSoup

douban_url = "https://movie.douban.com/top250"



class DSpider(object):

    def getHtmlPage(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
        response = requests.get(url, headers=headers)
        htmlPage = response.text
        return htmlPage

    def getInfoFromOnePage(self,url):
        dog = self.getHtmlPage(douban_url)
        soup = BeautifulSoup(dog, 'html.parser')
        result = []
        movies = self.soup.find('ol', class_='grid_view').find_all('li')
        for i in range(0, 25):
            movieName = movies[i].find('span').string
            movieScore = movies[i].find('span', class_='rating_num').string
            movieNum = movies[i].find('div', class_='star').find_all('span')[-1].string.strip('人评价')
            movieQuote = movies[i].find('p', class_='quote').find('span').string
            result.append([i + 1, movieName, movieScore, movieNum, movieQuote])
        return result

    def get_other_url(self):
        dog = self.getHtmlPage(douban_url)
        soup = BeautifulSoup(dog, 'html.parser')
        for i in range(2, 10):
            page = soup.find('div', class_='paginator').find_all('a', href=True)[:-1]
        for i in page:
            newUrl = douban_url + i['href']
            print(newUrl)













