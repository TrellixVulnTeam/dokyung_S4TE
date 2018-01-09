import requests
from bs4 import BeautifulSoup as Soup


base_url = 'http://webtoon.naver.com'
page_number = 501
target_url = base_url + '/webtoon/list.nhn?titleId=20853&weekday=tue&page=' + str(page_number)

template = '<div><img src="{img_url}" /><a href="{a_href}">{title}</a></div>'

r = requests.get(target_url)
soup = Soup(r.text, 'lxml')

title_td_list = soup.find_all(class_='title')
for td in title_td_list:
    img_url = td.parent.td.img.attrs['src']
    a_href = td.a.attrs['href']
    title = td.a.get_text()

    output = template.format(img_url=img_url, a_href=a_href, title=title)
    print(output)
