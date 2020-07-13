import execjs

node = execjs.get(execjs.runtime_names.Node)

# Params
method = 'GETDETAIL'
city = '昆明'
type = 'HOUR'
start_time = '2020-03-25 00:00:00'
end_time = '2020-04-25 00:00:00'

# Compile javascript
file = 'D:/Spider/test.js'
ctx = node.compile(open(file,encoding='utf-8').read())

# Get params
js = f"getPostParamCode('{method}', '{city}', '{type}', '{start_time}', '{end_time}')"
print(js)
params = ctx.eval(js)
print(params)