import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/omar/EDE/class_ede/output/expexp_background.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['expexp_background']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = ['Omega_scf']
tex_names = ['Omega_scf']
x_axis = 'z'
ylim = []
xlim = []
ax.semilogx(curve[:, 0], curve[:, 24])

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('z', fontsize=16)
plt.show()