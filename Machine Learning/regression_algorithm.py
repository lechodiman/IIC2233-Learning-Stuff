from statistics import mean
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

xs = np.array([1, 2, 3, 4, 5, 6], dtype=np.float64)
ys = np.array([5, 4, 6, 5, 6, 7], dtype=np.float64)


def best_fit_slope_and_intercept(xs, ys):
    m = (((mean(xs) * mean(ys)) - mean(xs * ys)) /
         (mean(xs) ** 2 - mean(xs ** 2)))
    n = mean(ys) - m * mean(xs)
    return np.array([n, m])


def vectorial_best_fit_slope_and_intercept(x, y):
    xty = x.transpose().dot(y)
    xtx_inv = inv((x.transpose()).dot(x))
    betas = xtx_inv.dot(xty)

    return betas


def squared_error(ys_original, ys_line):
    return sum((ys_line - ys_original) ** 2)


def coefficient_of_determination(ys_original, ys_line):
    y_mean_line = [mean(ys_original) for y in ys_original]
    squared_error_regr = squared_error(ys_original, ys_line)
    squared_error_y_mean = squared_error(ys_original, y_mean_line)
    return 1 - (squared_error_regr / squared_error_y_mean)


n, m = best_fit_slope_and_intercept(xs, ys)
print(n, m)

regression_line = [(m * x) + n for x in xs]
r_squared = coefficient_of_determination(ys, regression_line)
print(r_squared)

plt.scatter(xs, ys)
plt.plot(xs, regression_line)
plt.show()

# now with slope and intercept
xs = np.array([[1, 1, 1, 1, 1, 1],
               [1, 2, 3, 4, 5, 6]]).transpose()
m_2 = vectorial_best_fit_slope_and_intercept(xs, ys)
# print(m, m_2)
