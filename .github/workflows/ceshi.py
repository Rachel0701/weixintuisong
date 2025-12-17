# -*- coding: utf-8 -*-
import http.client, urllib
import json
# conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
# params = urllib.parse.urlencode({'key': 'd07bcb02de82927ec9c104e04998bcad'})
# headers = {'Content-type': 'application/x-www-form-urlencoded'}
# conn.request('POST', '/lzmy/index',params,headers)
# res = conn.getresponse()
# data = res.read()
# data = json.loads(data)  #转换成字典
# data = data.get("newslist", "未找到值")[0]
# data = data.get("saying", "未找到值")
# print(data)

conn = http.client.HTTPSConnection('api.tianapi.com')  # 接口域名
params = urllib.parse.urlencode({'key': 'd07bcb02de82927ec9c104e04998bcad', 'city': '宁波'})
headers = {'Content-type': 'application/x-www-form-urlencoded'}
conn.request('POST', '/tianqi/index', params, headers)
res = conn.getresponse()
print(res.status, res.reason)
data = res.read()
data = json.loads(data)
humidity = data["newslist"][0]["humidity"]
tips = data["newslist"][0]["tips"]
print(humidity)
print(tips)
