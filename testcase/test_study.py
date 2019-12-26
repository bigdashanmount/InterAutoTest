#coding:utf-8
# 动态关联
# 1、验证前置条件
# if pre_exec:
# pass
# 2、找到执行用例
# 3、发送请求，获取前置用例结果
# 发送获取前置测试用例，用例结果
# 数据初始化，get/post，重构
# 4、替换Headers变量
# 1、验证请求中是否${}$，返回${}$内容
import re
str2 = '{"Authorization": "JWT ${token}$"}'
str1 ='{"appKey":"201820011141153","isAdmin":"2","signature":"79E48482F30ED5CA96DCBB4DFA43D1576DBC2B74","token":"${token}$","userId":"${userId}$"}'
if "${" in str1:
    print(str1)

pattern = re.compile('\${(.*?)}\$')
re_res = pattern.findall(str1)
print(re_res[0])
print(re_res[1])
print(type(re_res))
     #2、根据内容token，查询 前置条件测试用例返回结果token = 值
token = "123"
userId="00000"
     #3、根据变量结果内容，替换

res = re.sub(pattern,token,str1)
res = re.sub(pattern,userId,str1)
print(res)
