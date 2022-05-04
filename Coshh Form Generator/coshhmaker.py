# COSHH form generator

# example input (will be processed from excel file in future)
chemicals = {
    'Dichloromethane':'10mL',
    'THF':'',
}



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    # 'From': "youremail@domain.com" This is another valid field
}


import requests
from requests_html import HTML

loc = 'Pages/test.txt'
url = 'https://www.sigmaaldrich.com/GB/en/substance/chromiumiiiacetylacetonate3493221679312?context=product'


response = requests.get(url, headers=headers)
page_read = response.text

# Cache the webpage
print(page_read)
with open(loc, 'w+', encoding='utf-8') as fhandle:
    fhandle.seek(0)
    fhandle.write(page_read)

# Analyse the html
with open(loc, 'r') as fhandle:

    html = HTML(html=fhandle.read())

    matches = html.find('div.fop-item')
    for match in matches:
        reduced_html = HTML(html=match.html)
        name = reduced_html.find('.fop-title')[0].attrs['title']
        link = [lnk for lnk in match.absolute_links][0]







