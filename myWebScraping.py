import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.in/Acer-AN515-54-15-6-inch-Notebook-processor/dp/B088FLW4TW/ref=sr_1_1?dchild=1&pf_rd_i=7198569031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=a5eff984-3f37-4c61-859a-ce773ce75496&pf_rd_r=QWCZ2PQ7ZP385C95SDNM&pf_rd_s=merchandised-search-7&pf_rd_t=101&qid=1593883365&sr=8-1'

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
#google - my user agent. this is trick amazon server that request is from a browser and get all data as in browser

page = requests.get(url, headers=header)
print(page.status_code)
if page.ok:
    print(page.status_code)
# Informational responses (100–199), -ok
# Successful responses (200–299), -ok
# Redirects (300–399), -ok
# Client errors (400–499), - fail
# and Server errors (500–599). - fail
soup = BeautifulSoup(page.content, 'html.parser')

titel_id = soup.find(id='productTitle')        
title = titel_id.get_text()  
print(title.strip())

price_id = soup.find(id='priceblock_ourprice') 
price = price_id.get_text()
price_int = (int(float(price.replace(',','').lstrip('₹').strip())))
print(price_int)
if price_int > 65000:
    print('high')
elif price_int == 59990:
    print('same price!')
else:
    print('less')