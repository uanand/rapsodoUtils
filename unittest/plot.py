import numpy
import matplotlib.pyplot as plt

plt.style.use("uanand")

data = numpy.loadtxt("input.txt", skiprows = 1, delimiter = "\t")

fig = plt.figure(figsize = (4, 3))
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(data[:, 0], data[:, 1], label = "Old kernel")
ax.plot(data[:, 0], data[:, 2], label = "New kernel")
ax.plot(data[:, 0], data[:, 3], label = "Default kernel")
ax.set_xlabel("Exposure key")
ax.set_ylabel("Average Intensity (a.u.)")
ax.set_xlim(0, 622)
ax.set_ylim(0, 2**16 - 1)
ax.legend()
plt.savefig("plot.png", format = "png")
plt.close()