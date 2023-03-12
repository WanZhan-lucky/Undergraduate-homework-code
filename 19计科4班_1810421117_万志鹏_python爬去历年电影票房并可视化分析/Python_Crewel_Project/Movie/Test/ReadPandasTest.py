#-*- coding = utf-8 -*-
#@Time : 2021/11/8 9:46
#@Author : 万战
#@File : ReadPandasTest.py
#@Software : PyCharm

import pandas as pd
data = pd.read_csv("./finalMovieData.csv")
print(data)
datadict = data.to_dict(orient="records")
print(datadict)
data1 = data['1'].tolist()
data2 = data['3'].tolist()
print(data1)
print(data2)
