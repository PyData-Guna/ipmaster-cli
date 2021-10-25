import socket
from urllib.parse import urlparse
try:
    WebpageLink = input()
    url = 'http://www.example.com/site/section1/VAR1/VAR2' 
    WebpageLink = urlparse(url).netloc
    IP_addres = socket.gethostbyname(WebpageLink)
    print("IP Address is:" + IP_addres)
except:
    print("error occured")