import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
plt.plot(x)
plt.grid()
plt.savefig('plot.png')