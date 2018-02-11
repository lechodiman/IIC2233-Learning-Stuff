# Loading data from files
import matplotlib.pyplot as plt
import csv
import numpy as np
import urllib
import matplotlib.dates as mdates
# Part 1
'''
x = []
y = []

with open('example.txt') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.scatter(x, y, label='Loaded from file')
'''

# Part 2
'''
x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)

plt.scatter(x, y, label='Loaded from file')
'''

# Getting data from the internet


def bytespdate2num(fmt, enconding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)

    def bytesconverter(b):
        s = b.decode(enconding)
        return strconverter(s)

    return bytesconverter


def graph_data(stock):
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/' + stock + '/chartdata;type=quote;range=10y/csv'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
                                                          delimiter=",",
                                                          unpack=True,
                                                          converters={0: bytespdate2num('%Y%m%d')})

    plt.plot_date(date, volume, '-', label='price')

    plt.title('Epic Info')
    plt.ylabel('price')
    plt.xlabel('date')
    plt.legend()
    plt.show()


graph_data('TSLA')
