import numpy as np
from itertools import groupby
import sys
from scipy.stats import multivariate_normal
import timeit

# задание 1
print("ЗАДАНИЕ 1")
matrix = np.genfromtxt('matrix.txt', delimiter=',')

print("Матрица:",'\n',matrix)

print("Сумма всех элементов:", np.sum(matrix))
print("Максимальный элемент:", np.max(matrix))
print("Минимальный элемент:", np.min(matrix))

# задание 2
print("ЗАДАНИЕ 2")
def run_length_encoding(x):
    x = x.tolist()
    groups = [(len(list(group)), key) for key, group in groupby(x)]

    numbers = [group[1] for group in groups]
    counts = [group[0] for group in groups]

    numbers = np.array(numbers)
    counts = np.array(counts)

    return numbers, counts


x = np.array([2, 2, 2, 3, 3, 3, 5])
numbers, counts = run_length_encoding(x)
print(numbers)
print(counts)

# задание 3
print("ЗАДАНИЕ 3")
array = np.random.normal(size=(10, 4))
print("Массив случайных чисел нормального распределения:", '\n', array)

print("Минимальное значение:", np.min(array))

print("Максимальное значение:",np.max(array))

print("Среднее значение:",np.mean(array))

print("Стандартное отклонение:",np.std(array))

first_rows = array[:5]
print("Первые 5 строк:",'\n', first_rows)

# задание 4
print("ЗАДАНИЕ 4")
x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])

zero_indices = np.where(x == 0)[0]

max_after_zero = -sys.maxsize - 1

for i in zero_indices:
    if i + 1 < len(x):
        if x[i + 1] > max_after_zero:
            max_after_zero = x[i + 1]

print("Максимальный элемент перед которым стоит нулевой:", max_after_zero)

# задание 5
print("ЗАДАНИЕ 5")
def log_pdf_multivariate_normal(X, m, C):
    dimension = X.shape[1]
    determinantC = np.linalg.det(C)  # определитель матрицы ковариаций
    invdeterminantC = np.linalg.inv(C)  # обратная матрица ковариаций

    const = -0.5 * dimension * np.log(2 * np.pi) - 0.5 * np.log(determinantC)
    subtractxm = X - m
    exp = -0.5 * np.sum(np.dot(subtractxm, invdeterminantC) * subtractxm, axis=1)

    log_pdf = const + exp

    return log_pdf


X = np.random.randn(1000, 2)  # точки X
m = np.array([0, 0])  # мат. ожидание
C = np.array([[1, 0], [0, 1]])  # матрица ковариаций

log_pdf = log_pdf_multivariate_normal(X, m, C)
scipy_log_pdf = multivariate_normal(m, C).logpdf(X)

print("Логарифм плотности многомерного нормального распределения (numpy):", '\n', log_pdf_multivariate_normal(X, m, C), '\n')

print("Логарифм плотности многомерного нормального распределения (scipy):", '\n', multivariate_normal(m, C).logpdf(X))

numpy_time = timeit.timeit(lambda: log_pdf_multivariate_normal(X, m, C), number=1000)
scipy_time = timeit.timeit(lambda: multivariate_normal(m, C).logpdf(X), number=1000)

print("Время работы NumPy:", numpy_time)
print("Время работы SciPy:", scipy_time)

# задание 6
print("ЗАДАНИЕ 6")
a = np.arange(16).reshape(4, 4)
print("Исходный массив:",'\n', a)
a[[0, 2]] = a[[2, 0]]
print("Массив после обмена строк:", '\n',a)

# задание 7
print("ЗАДАНИЕ 7")
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

print("Уникальные значения в столбце species:", np.unique(iris[:, 4]))
print("Количество уникальных значений:", len(np.unique(iris[:, 4])))

# задание 8
print("ЗАДАНИЕ 8")
a = np.array([0, 1, 2, 0, 0, 4, 0, 6, 9])
indices = np.nonzero(a)
print("Список индексов ненулевых элементов:", indices[0].tolist())
