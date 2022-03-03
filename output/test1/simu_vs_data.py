import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/furkan/Bureau/Stage/class_public-2.9.3-master/output/test01_cl.dat','/home/furkan/Bureau/Stage/class_public-2.9.3-master/output/test05_cl.dat','/home/furkan/Bureau/Stage/class_public-2.9.3-master/output/test03_cl.dat','/home/furkan/Bureau/Stage/class_public-2.9.3-master/output/dataEE.txt']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['Fit Planc18 TT ','Fit Planck18 EE','Fit Planck18 TT+TE+EE','Data']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = ['EE']
tex_names = ['EE']
x_axis = 'l'
ylim = []
xlim = []
ax.plot(curve[:, 0], curve[:, 2])

index, curve = 1, data[1]
y_axis = ['EE']
tex_names = ['EE']
x_axis = 'l'
ylim = []
xlim = []
ax.plot(curve[:, 0], curve[:, 2])

index, curve = 2, data[2]
y_axis = ['EE']
tex_names = ['EE']
x_axis = 'l'
ylim = []
xlim = []
ax.plot(curve[:, 0], curve[:, 2])


index, curve = 3, data[3]
y_axis = ['EE']
tex_names = ['EE']
x_axis = 'l'
ylim = []
xlim = []
#ax.plot(curve[:, 0], curve[:, 1])
ax.errorbar(curve[:, 0], curve[:, 1], yerr=curve[:, 3], fmt=".", linestyle="solid")




ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('$\ell$', fontsize=16)
ax.set_ylabel('$\ell (\ell +1)/(2 \pi )C_{\ell}$ ($(\mu K)^2$)', fontsize=14)

plt.show()