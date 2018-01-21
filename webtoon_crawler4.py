import requests
from bs4 import BeautifulSoup as Soup

def main():
    total_result = []
    page_number = 1
    base_url = 'http://webtoon.naver.com/webtoon/list.nhn?titleId=20853&page='
    while True:
        target_url = base_url + str(page_number)

        r = requests.get(target_url)
        soup = Soup(r.text, 'lxml')

        total_result += get_list(soup)

        next_page = soup.find(class_='next')
        if next_page is None:
            break
        else:
            page_number += 1

    write_file(total_result)

def write_file(webtoon_list):
    f = open("C:/dev/dokyung/마음의소리.html", 'w')
    for webtoon in webtoon_list:
        f.write(webtoon + '\n')
    f.close()

def get_list(soup):
    title_td_list = soup.find_all(class_='title')
    template = '<div><img src="{img_url}" /><a href="{a_href}">{title}</a></div>'

    result = []

    for td in title_td_list:
        img_url = td.parent.td.img.attrs['src']
        a_href = td.a.attrs['href']
        title = td.a.get_text()
        output = template.format(img_url=img_url, a_href=a_href, title=title)
        result.append(output)
    return result

if __name__ == '__main__':
    main()
