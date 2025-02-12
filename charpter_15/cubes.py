import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title('Cubes', fontsize=24)
ax.set_xlabel('Values', fontsize=14)
ax.set_ylabel('Cubes opf Values', fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)
ax.axis([0, 5100, 0, 100000000000])

plt.savefig('Cubes_plot.png')