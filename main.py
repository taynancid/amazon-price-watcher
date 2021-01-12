from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError 
from urllib.error import URLError
import re

def BRLStringToFloat(priceTag):
  price = re.split(r'R\$',priceTag.get_text())[1]
  price = float(price.replace('.','').replace(',','.'))
  return price

def findPriceTag(bs):
  priceTag = bs.find('span', {'class':'offer-price'})
  if(priceTag == None) :
    priceTag = bs.find(id = 'price_inside_buybox')
  return priceTag

try:
  html = urlopen('https://www.amazon.com.br/Smartphone-Xiaomi-Redmi-Note-9S/dp/B085S4DSZH?ref_=Oct_s9_apbd_otopr_hd_bw_bHjJLCl&pf_rd_r=JWQF2RTA8ACR6ND0X2EK&pf_rd_p=1da659a0-948a-52ba-a216-243433981446&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=16243803011')
except HTTPError as e:
  print(e)
except URLError as e:
  print('The server could not be found!')
else:
  priceTag = findPriceTag(BeautifulSoup(html.read(), 'html.parser'))
  price = BRLStringToFloat(priceTag)
  print(price > 10)

