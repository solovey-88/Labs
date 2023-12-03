import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import csv

# Задание 1

# Генерируем прямоугольный сигнал
t = np.linspace(0, 1, 500, endpoint=False)
square_wave = signal.square(2 * np.pi * 5 * t)

# Отрисовываем сигнал
plt.plot(t, square_wave)
plt.ylim(-2, 2)
plt.show()

# Задание 2

mu, sigma = 0, 0.1
s = np.random.normal(mu, sigma, 1000)

# Строим гистограмму
count, bins, ignored = plt.hist(s, 30, density=True)
plt.show()

# Задание 3

with open('passengers.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    data = list(reader)

months = [row[0] for row in data]
passengers = [int(row[1]) for row in data]

plt.figure()
plt.plot(months, passengers)
plt.title('Пассажиропоток за все время')
plt.xlabel('Месяц')
plt.ylabel('Пассажиры')
plt.show()

months_1951_1955 = [months[i] for i in range(len(months)) if '1951' <= months[i][:4] <= '1955']
passengers_1951_1955 = [passengers[i] for i in range(len(months)) if '1951' <= months[i][:4] <= '1955']

plt.figure()
plt.hist(passengers_1951_1955, bins=12)
plt.title('Распределение пассажиров по месяцам, 1951 - 1955 гг.')
plt.xlabel('Пассажиры')
plt.ylabel('Частота')
plt.show()


