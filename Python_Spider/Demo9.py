import csv
f = open("./demo.csv", "r", newline = "", encoding = 'utf-8')
# writer = csv.writer(f)
# writer.writerow(['电影', '豆瓣'])
# #调用writer对象的writerow()方法，可以在csv文件里写入一行文字 “电影”和“豆瓣评分”。
# writer.writerow(['银河护卫队','8.0'])
# #在csv文件里写入一行文字 “银河护卫队”和“8.0”。
# writer.writerow(['复仇者联盟','8.1'])
reader = csv.reader(f)
for row in reader:
    print(row)
f.close()
