import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1115776.json'
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
js = json.loads(data)
sum=0
count=0
print(json.dumps(js, indent=4))
for item in js['comments']:
    sum = int(item['count'])+sum
    count = count+1
print('Count:', count)
print('Sum:', sum)