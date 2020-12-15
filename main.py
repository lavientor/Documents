from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import warnings  # warning 무시를 위한 import

print('==== main.py =====')

# warning 무시
warnings.filterwarnings(action='ignore')

# URL
url = 'https://bitinfocharts.com/bitcoin/address/3JZq4atUahhuA9rLhXLMhhTo133J9rF97j'

# 현재 Balance 가져오기
res = requests.get(url,verify=False,headers={"User-Agent" : "Mozilla/5.0"})

print(res)
print(res.status_code)
print(res.content.decode('utf-8'))


soup = BeautifulSoup(res.text,'html.parser')

print(soup)
# soup.h1 : h1태그를 찾는다 (Tag 탐색)
# soup.h1.find(attrs={'itemprop':'name'}) : h1태그 중에서 itmsprop라는 attribute값으로 name을 가지는 대상을 찾는다
# soup.h1.find(attrs={'itemprop':'name'}).string : 위 찾은 대상에서 텍스트만을 가져온다

# BeautifulSoup 탐색 가이드
# 1. Tag 탐색
# soup.p : p태그를 탐색
# soup.h1 : h1태그를 탐색
# soup.h1.string : h1태그의 텍스트를 탐색
# soup.h1.children : 트리구조의 하위항목을 모두 탐색
# soup.h1.parents : 트리구조의 상위항목을 모두 탐색


# 2. find_all() 탐색 : find()로 대체 가능
# find_all('ul') : ul 태그를 탐색
# find_all(re.compile('[ou]l') : (정규식) ul, ol 태그를 탐색
# find_all(['ul','ol']) : (리스트) ul, ol 태그를 탐색
# find_all(attrs={'class':'card-title'},'id':'footer-address-list') : (html속성) 딕셔너리 형태로 attrs 파라미터를 지정

# def search_function(tag):
#   return tag.attr('class') == 'card-title'; and tag.string == 'Hello World'
# soup.find_all(search_function) : (함수) 조건이나 규칙을 지정할 수 있다

# find()로 대체하는 것이 가능하다
# find_all(attrs={'class':'card-title'},'id':'footer-address-list').string : 탐색된 첫번째 결과의 텍스트를 탐색
print(soup.h1.find(attrs={'itemprop':'name'}).string)
title = soup.h1.find(attrs={'itemprop':'name'}).string


print(soup.find_all('div', attrs={'itemprop':'offers'}))
# for i in soup.find_all('div'):
#     print(i)

# CSS 선택자 탐색
print(soup.find_all('div b'))
print(soup.select('div b')[1])
print(soup.select('div b')[1].get_text())


