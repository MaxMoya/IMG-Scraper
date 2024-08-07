import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

img = urllib.request.urlopen('https://content.osgnetworks.tv/infisherman/content/photos/Huge-Texas-bass-Lead.jpg')
fhand = open('bigbass.jpg', 'wb')
size = 0
while True:
    info = img.read(1000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied.')
fhand.close
