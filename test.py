from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf")
bsObject=BeautifulSoup(html,"html.parser")
#c책의 상세 웹페이지 주소를 추출하여 리스트에 저장
#a태그: 다른웹페이지로 이동하거나 문서 내에서 이동
#href태그:연결할 주소를 지정
book_page_urls=[]
for cover in bsObject.find_all('div',{'class':'detail'}):
    link=cover.select('a')[0].get('href')
    book_page_urls.append(link)
#meta태그::문서의 내용,키워드,누가 만들었는지의 특성을 담고 있음
#http-equiv=항목명:서버에 명령을 내리는 속성으로 name대신 사용
#content=정보값:meta정보의 내용을 저장
#name=정보이름:정보의 이름을 저장
#name=keywords:검색엔진에 의해 검색되는 단어를 지정
#name=description:검색결과에 표시되는 문자를 지정
#name=rebots:검색로봇제어
for index, book_page_url in enumerate(book_page_urls):
    html=urlopen(book_page_url)
    bsObject=BeautifulSoup(html,"html.parser")
    title=bsObject.find('meta',{'property':'rb:itemName'}).get('content')
    author=bsObject.select('span.name a')[0].text
    image=bsObject.find('meta',{'property':'rb:itemImage'}).get('content')
    url=bsObject.find('meta',{'property':'rb:itemUrl'}).get('content')
    originalPrice=bsObject.find('meta',{'property':'rb:originalPrice'}).get('content')
    salePrice=bsObject.find('meta',{'property':'rb:salePrice'}).get('content')

    print(index+1,title,author,image,url,originalPrice,salePrice)

    urlretrieve()