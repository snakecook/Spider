import requests
from requests import Session
import re
import execjs


with open('Js_safe.js','r',encoding='utf-8') as f1:
    JS_safe = f1.read()

call_Func = '''

function getPostParamCode(method, city, type, startTime, endTime) {
    var param = {};
    param.city = city;
    param.type = type;
    param.startTime = startTime;
    param.endTime = endTime;
    return %s(method, param);
}
'''


url_content = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
url_encryption = 'https://www.aqistudy.cn/js/jquery.min.js?v=1.2'
url_detail = 'https://www.aqistudy.cn/html/city_detail.php'


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
}

session = Session()
# # 获取加密方式，提取一次即可
# c = session.get(url_encryption).text
# print(c)

a = session.get(url_detail).text
# print(a.text)



base_url = 'https://www.aqistudy.cn'
url_js = base_url + re.findall('(/js/encrypt.*?)">',a)[0]
# filter = 'endTime = endTime;\W+(.*?)\('
# js_func = re.findall(filter,a)[0]
# # print(js_func)

JS_code = session.get(url_js).text
print(JS_code)
param = re.findall('var param = (.*?)\(m',JS_code)[0]
visit_key = re.findall('data: {(.*?):',JS_code)[0].strip()
data_decode = re.findall('\nfunction (.*?)\(data\)',JS_code)[0]
call_Func = call_Func %(param)

with open('JS_updata.js','w',encoding='utf-8') as f2:
    f2.write(JS_safe)
    f2.write(JS_code)
    f2.write(call_Func)


# 执行JS代码
node = execjs.get(execjs.runtime_names.Node)
# Params
# method = 'GETDETAIL'
method = 'GETCITYWEATHER'
city = '昆明'
type = 'DAY'
start_time = '2020-05-20 00:00:00'
end_time = '2020-06-30 00:00:00'

# Compile javascript
file = 'JS_updata.js'
ctx = node.compile(open(file,encoding='utf-8').read())

# Get visit_value
js = f"getPostParamCode('{method}', '{city}', '{type}', '{start_time}', '{end_time}')"
visit_value = ctx.eval(js)
post_data = {f'{visit_key}': f'{visit_value}'}

# Get post response
response = requests.post(url_content,data=post_data).text

# decode data
js = f'{data_decode}("{response}")'
decrypted_data = ctx.eval(js)
print(decrypted_data)