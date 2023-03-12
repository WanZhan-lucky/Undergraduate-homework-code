#-*- coding = utf-8 -*-
#@Time : 2021/11/7 14:45
#@Author : 万战
#@File : rename.py
#@Software : PyCharm
import re
pat = re.compile(r'_(\d{1,2})')
s = "/meinvtupian/meinvxiezhen/20894_10.htm"
t = re.findall(pat, s)
print(t)
#t = pat.serach(sk)


# import re
#
# pat = re.compile("AA") #正则表达式
# s = "ABC"
# d = "AABCAAAADAA"
# m = pat.search(s)
# print(m)
# mt = pat.search(d)
# print(mt)

# #前是正则，后是被匹配的
# print(re.findall('a', "abdacdga"))
# print(re.sub('a', 'A', 'abcdadfka'))