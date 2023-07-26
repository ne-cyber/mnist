import numpy as np

idx = 333

txt_file = ".\\mnist_train_1000.txt"

all_data = np.loadtxt(txt_file, delimiter="\t", usecols=range(0,785), dtype=np.int64)

x_data = all_data[:,0:784]  # all rows, 784 cols
y_data = all_data[:,784]    # all rows, last col

label = y_data[idx]

print("digit = ", str(label), "\n")

pixels = x_data[idx]
pixels = pixels.reshape((28,28))

for i in range(28):
    for j in range(28):
      # print("%.2X" % pixels[i,j], end="")
      print("%3d" % pixels[i,j], end="")
      print(" ", end="")
    print("")

