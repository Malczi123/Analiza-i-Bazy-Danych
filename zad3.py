import matplotlib.pyplot as plt
import numpy as np

def func(x: float)->float:
    return x**2+5

t1 = np.linspace(-1,1)
t2 = np.linspace(-6,6)
t3 = np.linspace(0,5)

fig,axs = plt.subplots(1,3)
axs[0].plot(t1,func(t1))
axs[0].set_title('Wykres pierwszy')
axs[0].set_xlabel('Wartosc x')
axs[0].set_ylabel('Wartosc funkcji')
axs[0].legend('X',loc='upper right')

axs[1].plot(t2,func(t2))
axs[1].set_title('Wykres drugi')
axs[1].set_xlabel('Wartosc x')
axs[1].set_ylabel('Wartosc funkcji')
axs[1].legend('Y',loc='upper right')

axs[2].plot(t3,func(t3))
axs[2].set_title('Wykres trzeci')
axs[2].set_xlabel('Wartosc x')
axs[2].set_ylabel('Wartosc funkcji')
axs[2].legend('Z',loc='upper right')

plt.show()