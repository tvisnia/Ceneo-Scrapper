import urllib.request
from bs4 import BeautifulSoup

prefix = "https://www.ceneo.pl/"
postfix = "/opinie-"
product_id = "45498942"
page_num = 1

url = prefix+product_id+postfix+str(page_num)

#pobranie zawartoœci strony
site = urllib.request.urlopen(url)
page = site.read()

page_tree = BeautifulSoup(page, 'html.parser')

opinions_num = int(page_tree.find("span",attrs={"itemprop": "reviewCount"}).string)
print(opinions_num)

#parsowanie kodu strony


#zapisanie danych do bazy

pojedynacza opinia: li.review-box
autor: div.reviewer-name-line
rekomendacja: div.product-review-summary > em
gwiazdki: span.reviw-score-count
data wystawienia opinii: time (wartoœæ atrybutu datetime) - pierwsze wyst¹pienie
data zakupu produktu: time (wartoœæ atrybutu datetime) - drugie wyst¹pienie
treœæ: p.product-review-body
wady: div.cons-cell > ul > li
zalety: div.cons-cell > ul > li
przydatna: [id^=votes-yes]
nieprzydatna: [id^=votes-no]
id opinii: li.review-box (wartoœæ atrybutu data-entry-id)
liczba opinii: span[itemprop=reviewCount]