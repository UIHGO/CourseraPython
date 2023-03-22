import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
position = int(input('Position - '))
count = int(input('Count - '))
for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    n = 1
    # s = 1
    for tag in tags:
        n = n+1
        if n < position+1:
            continue
        else:
            print('Going in', tag.get('href', None))
            url = tag.get('href', None)
            n = 0
            break
print('Last', tag.get('href', None))
print('gg')
