from matplotlib import pyplot as plt
import numpy as np
import random
# s = np.random.poisson(5, 10000)
# plt.hist(s, 14, normed=True)
# Plotting to our canvas

# Normal plot
'''
x = [1, 2, 3]
y = [5, 7, 4]

x2 = [1, 2, 3]
y2 = [10, 14, 12]

plt.plot(x, y)
plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')


plt.show()
'''

# Bar charts

x = [2, 4, 6, 8, 10]
y = [6, 7, 8, 2, 4]

x2 = [1, 3, 5, 7, 9]
y2 = [7, 8, 2, 4, 2]

# plt.bar(x, y, label='Bars1', color='blue')
# plt.bar(x2, y2, label='Bars2', color='c')

# Histograms

population_ages = [random.sample(range(131), 30)]

ids = [x for x in range(len(population_ages))]

bins = [n for n in range(0, 131, 10)]

# plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

# Scatter Plots
x = [num for num in range(9)]
y = [random.sample(range(10), 9)]

# plt.scatter(x, y, label='skitscat', color='k', marker='*', s=100)

# Stack Plots

days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

# plt.plot([], [], color='m', label='Sleeping', linewidth=4)
# plt.plot([], [], color='c', label='Eating', linewidth=4)
# plt.plot([], [], color='r', label='Working', linewidth=4)
# plt.plot([], [], color='k', label='Playing', linewidth=4)

# plt.stackplot(days, sleeping, eating, working, playing,
#               colors=['m', 'c', 'r', 'k'],
#               labels=['Sleeping', 'Eating', 'Working', 'Playing'])

# Pie Charts

slices = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'b']

# plt.pie(slices, labels=activities, colors=cols, startangle=90,
#         shadow=True, explode=(0, 0.1, 0, 0), autopct='%1.1f%%')

plt.title('Epic Info')
# plt.ylabel('Y axis')
# plt.xlabel('X axis')
plt.legend()
plt.show()
