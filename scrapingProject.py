import bs4, requests

headers = { ###Trick Amazon into thinking program is human via HEADERS
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip', 
'DNT' : '1', # Do Not Track Request Header 
'Connection' : 'close'
}           ###Trick Amazon into thinking program is human via HEADERS

print('Enter an Amazon page to price scrape.')
urlAddress = input() 


def getAmazonPrice(productUrl):
    res = requests.get(productUrl, headers=headers)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#priceInsideBuyBox_feature_div > div.a-section.a-spacing-micro > span.a-size-medium.a-color-price')
    return elems[0].text.strip()
    
    
    
    

price = getAmazonPrice(urlAddress)
print('The price is ' + price)



#mediaNoAccordion > div.a-row > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price