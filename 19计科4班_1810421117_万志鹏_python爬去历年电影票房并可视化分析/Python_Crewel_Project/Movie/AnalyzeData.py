#-*- coding = utf-8 -*-
#@Time : 2021/11/7 18:08
#@Author : 万战
#@File : AnalyzeData.py
#@Software : PyCharm

import pandas as pd

initData = pd.read_csv("movie1994-2021.csv",header = None)
print("initdata: ", initData)

dealData = initData.loc[:,[1,3]]
print("dealData:" , dealData)

finalData = dealData.groupby(1).mean().round(2)
print("dataFinal: ", finalData)

finalData.to_csv("./finalMovieData.csv")