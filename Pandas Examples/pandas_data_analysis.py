import pandas as pd
import datetime
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

# Demo
'''
style.use('ggplot')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 1, 1)

df = web.DataReader("XOM", "yahoo", start, end)

print(df.head())
df['Adj Close'].plot()
plt.show()
'''
# Pandas Basics

web_stats = {'Day': [1, 2, 3, 4, 5, 6],
             'Visitors': [43, 53, 34, 45, 64, 34],
             'Bounce_Rate': [65, 72, 62, 64, 54, 66]}

df = pd.DataFrame(web_stats)

# print(df.head())
# print(df.tail())
# print(df.head(2))

# this returns a new data frame with a new index
# print(df.set_index('Day'))

# df = df.set_index('Day')
# df.set_index('Day', inplace=True)
# print(df.head())

# print(df['Visitors'])
# print(df.Visitors)

print(df[['Bounce_Rate', 'Visitors']])

print(df.Visitors.tolist())
print(np.array(df[['Bounce_Rate', 'Visitors']]))

df2 = pd.DataFrame(np.array(df[['Bounce_Rate', 'Visitors']]))
print(df2)
