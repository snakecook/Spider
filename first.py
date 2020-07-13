import requests
from requests import Session

url = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
url2 = 'https://www.aqistudy.cn/js/encrypt_ewtlmdc45MCb.js?t=1594608902'
url3 = 'https://www.aqistudy.cn/js/encrypt_enYKZ8dpEP4f.min.js?t=1594609501'
url4 = 'https://www.aqistudy.cn/js/jquery.min.js?v=1.2'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'h4hJRoRXu': "vYAPZSRHeiRiOXxrpxnKN/jpQyRdBSNhmCb3BwQKxPI7LgFSkmFFhbgwsEGChhs3CTLDAwT9SO98PcYfKFoyVGjhcmUs07PbhdSbBFLN+s6GLrbgxx9mqeI+hLlIupCsr681mzZ6+t3wlNpLmdkWR2MNKgVmuXRfVnKJHHmzBSqkHKziFTBPJCy+QkwduNKmGoKvZYkw2zEFIEceDFAvpOHdAaziF0BtuJGtKW11nCVkQVBZ3xCpZj0q9SWbCyzOrPsqxDo8OK+EAOT/kfVG5hK86V4nur9QXXOw1jdGlsy48HGrci4GKCqObhFEePjhPOI8xso8lmex2FsLZdS/6Y0QbgvwIXRGuU2Q3AsDaZ6gULzntAP65oy+TU/zJZP6rEJ6vS7VJZgcEZuEdsHS+v4UjodI2BAubz5lZsHIxYoTvjK7j965qTJfv2VqyA4KEx2RcDpt/2FQCn2tNamvzQ==",
}

session = Session()
a = session.get(url4)

print(a.text)
