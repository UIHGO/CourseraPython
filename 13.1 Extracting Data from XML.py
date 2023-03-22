import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
url = 'http://py4e-data.dr-chuck.net/comments_1115775.xml'
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
tree = ET.fromstring(data)
results = tree.findall('comments/comment')
print('Count', len(results))
sum = 0
for result in results:
    sum = sum+int(result.find('count').text)
print('Sum', sum)
# results = tree.findall('.//count')
# print(len(results))
# sum = 0
# for result in results:
#     sum = sum+int(result.text)
# print('Sum', sum)