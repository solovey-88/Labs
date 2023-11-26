import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider
from scipy.special import legendre

# Задание 1
x = np.linspace(-1, 1, 1000)

plt.figure(figsize=(10, 6))
plt.title('Полиномы Лежандра')

for i in range(1, 8):
    y = legendre(i)(x)
    plt.plot(x, y, label=f'n = {i}')

plt.legend(loc='upper right')
plt.grid(True)
plt.show()

# Задание 2
t = np.linspace(0, 2 * np.pi, 1000)

fig, axs = plt.subplots(2, 2, figsize=(10, 10))

axs[0, 0].plot(np.sin(3 * t), np.sin(2 * t))
axs[0, 0].set_title('3:2')

axs[0, 1].plot(np.sin(3 * t), np.sin(4 * t))
axs[0, 1].set_title('3:4')

axs[1, 0].plot(np.sin(5 * t), np.sin(4 * t))
axs[1, 0].set_title('5:4')

axs[1, 1].plot(np.sin(5 * t), np.sin(6 * t))
axs[1, 1].set_title('5:6')

for ax in axs.flat:
    ax.label_outer()

plt.show()

# Задание 3
fig, ax = plt.subplots()

t = np.linspace(0, 2 * np.pi, 1000)
line, = ax.plot(np.sin(t), np.sin(t))


def animate(i):
    line.set_ydata(np.sin(i * t))
    return line,


ani = animation.FuncAnimation(fig, animate, interval=20, blit=True, save_count=50)

plt.show()

# Задание 4
x = np.linspace(0, 2 * np.pi, 1000)
y1 = np.sin(x)
y2 = np.sin(2 * x)

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
l1, = plt.plot(x, y1, label='Волна 1')
l2, = plt.plot(x, y2, label='Волна 2')
l3, = plt.plot(x, y1 + y2, label='Сумма волн', color='g')
plt.legend(loc='upper right')

axcolor = 'white'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

sfreq = Slider(axfreq, 'Частота', 0.1, 30.0, valinit=1)
samp = Slider(axamp, 'Амплитуда', 0.1, 10.0, valinit=1)


def update(val):
    amp = samp.val
    freq = sfreq.val
    l1.set_ydata(amp * np.sin(freq * x))
    l2.set_ydata(amp * np.sin(2 * freq * x))
    l3.set_ydata(amp * np.sin(freq * x) + amp * np.sin(2 * freq * x))
    fig.canvas.draw_idle()


sfreq.on_changed(update)
samp.on_changed(update)

plt.show()

# Задание 5
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
x, y = np.meshgrid(x, y)
z = (1 / 2) * (x ** 2 + y ** 2)

fig = plt.figure(figsize=(12, 6))

ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(x, y, z, cmap='gnuplot')
ax1.set_title('Обычная ось Z')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(x, y, np.log(z), cmap='gnuplot')
ax2.set_title('Логарифмическая ось Z')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('log(Z)')

plt.show()