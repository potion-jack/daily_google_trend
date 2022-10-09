import warnings
import numpy as np
from crwals.daily_trend import *
import csv
warnings.filterwarnings(action='ignore')

today_trends = np.array(trends_retriever())

f = open('crwals/result.csv', 'a', encoding='utf-8', newline='')
wr = csv.writer(f)
for i in range(len(today_trends)):
    wr.writerow(today_trends[i])
f.close()
