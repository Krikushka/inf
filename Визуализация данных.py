from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

'''n = int(input('введи количество точек >> '))
tochki = np.random.rand(n, 2)
print(tochki)

sum_x = sum(tochki[i][0] for i in range(n))
sum_y = sum(tochki[i][1] for i in range(n))
print(sum_x, sum_y)

sum_xy = sum([tochki[i][0] * tochki[i][1] for i in range(n)])
sum_x2 = sum([tochki[i][0] ** 2 for i in range(n)])
print(sum_xy, sum_x2)

a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
b = (sum_x2 * sum_y - sum_x * sum_xy) / (n * sum_x2 - sum_x ** 2)



x = np.linspace(0, 10, 100)
y = a * x + b

plt.title('МНК')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.plot(x, y)
plt.show()'''

n = int(input('введи количество значений >> '))
chisla = np.random.rand(n)
k = len(chisla)
ver = Counter(chisla)
mat_o = sum(i * (ver[i] / k) for i in ver)
mat_o2 = sum((i * (ver[i] / k)) ** 2 for i in ver)

disp = mat_o2 - mat_o ** 2
sr_otkl = disp ** 0.5
print(sr_otkl)








