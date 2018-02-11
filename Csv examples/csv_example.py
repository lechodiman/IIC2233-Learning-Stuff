import csv
from datetime import datetime
'''
with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    dates = []
    colors = []
    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

    whatColor = input("'What color do you wish?: ")
    coldex = colors.index(whatColor.lower())

    theDate = dates[coldex]

    print('The date of ', whatColor, 'is', theDate)

'''

with open('google_stock_data.csv') as f:
    reader = csv.reader(f)

    header = next(reader)
    data = []
    for row in reader:
        # row = [Date, Open, High, Low , Close, Volume, Adj Close]
        date = datetime.strptime(row[0], '%m/%d/%Y')
        open_price = float(row[1])
        high = float(row[2])
        low = float(row[3])
        close = float(row[4])
        volume = int(row[5])
        adj_close = float(row[6])

        data.append([date, open_price, high, low, close, volume, adj_close])

    print(data[0])

with open('google_returns.csv', 'w', newline='') as wf:
    writer = csv.writer(wf)
    writer.writerow(["Date", "Return"])

    for i in range(len(data) - 1):
        todays_row = data[i]
        todays_date = todays_row[0]
        todays_price = todays_row[-1]
        yesterday_row = data[i + 1]
        yesterdays_price = yesterday_row[-1]

        daily_return = (todays_price - yesterdays_price) / yesterdays_price
        formatted_date = todays_date.strftime("%m/%d/%Y")
        writer.writerow([formatted_date, daily_return])
