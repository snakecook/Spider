import execjs


# 执行JS代码
node = execjs.get(execjs.runtime_names.Node)
# Params
a = '111111'
b = '123321'

# Compile javascript
file = 'MG.js'
ctx = node.compile(open(file,encoding='utf-8').read(),cwd=r'C:\Users\admin\AppData\Roaming\npm\node_modules')

# Get visit_value
js1 = f"gPa('{a}')"
js2 = f"gPa('{a}')"
js3 = "rsaFingerprint(a.result.modulus, a.result.publicExponent)"
logID = ctx.eval(js1)
enPwd = ctx.eval(js2)
tem = ctx.eval(js3)

# END
print('logID：',logID)
print('enPwd：',enPwd)
print('tem：',tem)