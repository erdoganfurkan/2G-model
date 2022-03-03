import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/furkan/Bureau/Stage/class_public-2.9.3-master/output/test05_cl.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['test05_cl']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = ['TT', 'EE', 'BB', 'TE', 'dd', 'dT', 'dE']
tex_names = ['TT', 'EE', 'BB', 'TE', 'dd', 'dT', 'dE']
x_axis = 'l'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 1]))
ax.loglog(curve[:, 0], abs(curve[:, 2]))
ax.loglog(curve[:, 0], abs(curve[:, 3]))
ax.loglog(curve[:, 0], abs(curve[:, 4]))
ax.loglog(curve[:, 0], abs(curve[:, 5]))
ax.loglog(curve[:, 0], abs(curve[:, 6]))
ax.loglog(curve[:, 0], abs(curve[:, 7]))

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('$\ell$', fontsize=16)
plt.show()