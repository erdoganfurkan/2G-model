import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/furkan/Bureau/Stage/class_public-2.9.3-master/output/test00_cl.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['test00_cl']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = ['TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
ax.plot(curve[:, 0], curve[:, 1])

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('$\ell$', fontsize=16)
plt.show()