import requests
from requests import Session

url = 'http://www.86pm25.com/city/kunshan.html'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
}

session = Session()
a = session.get(url)

print(a)
