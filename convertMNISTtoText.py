# converter_mnist.py

import numpy as np
import matplotlib.pyplot as plt

# convert MNIST binary to text file; combine pixels and labels
# target format:
# pixel_1 (tab) pixel_2 (tab) . . pixel_784 (tab) digit

# 1. manually download four zipped-binary files from
#    yann.lecun.com/exdb/mnist/ 
# 2. use 7-Zip to unzip files, add ".bin" extension
# 3. determine format you want and modify script

def convert(img_file, label_file, txt_file, n_images):
  print("\nOpening binary pixels and labels files ")
  lbl_f = open(label_file, "rb")   # labels (digits)
  img_f = open(img_file, "rb")     # pixel values
  print("Opening destination text file ")
  txt_f = open(txt_file, "w")      # output to write to

  print("Discarding binary pixel and label headers ")
  img_f.read(16)   # discard header info
  lbl_f.read(8)    # discard header info

  print("\nReading binary files, writing to text file ")
  print("Format: 784 pixels then labels, tab delimited ")
  for i in range(n_images):   # number requested 
    lbl = ord(lbl_f.read(1))  # Unicode, one byte
    for j in range(784):  # get 784 pixel vals
      val = ord(img_f.read(1))
      txt_f.write(str(val) + "\t") 
    txt_f.write(str(lbl) + "\n")
  img_f.close(); txt_f.close(); lbl_f.close()
  print("\nDone ")

def display_from_file(txt_file, idx):
  all_data = np.loadtxt(txt_file, delimiter="\t",
    usecols=range(0,785), dtype=np.int64)

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

  plt.tight_layout()
  plt.imshow(pixels, cmap=plt.get_cmap('gray_r'))
  plt.show()  

def main():
  n_images = 1000
  print("\nCreating %d MNIST train images from binary files " % n_images)
  convert(".\\UnzippedBinary\\train-images.idx3-ubyte",
          ".\\UnzippedBinary\\train-labels.idx1-ubyte",
          "mnist_train_1000.txt", 1000)

  # n_images = 100
  # print("\nCreating %d MNIST test images from binary files " % n_images)
  # convert(".\\UnzippedBinary\\t10k-images.idx3-ubyte.bin",
  #         ".\\UnzippedBinary\\t10k-labels.idx1-ubyte.bin",
  #         "mnist_test_100.txt", 100)

  print("\nShowing train image [0]: ")
  img_file = ".\\mnist_train_1000.txt"
  display_from_file(img_file, idx=0)  # first image

if __name__ == "__main__":
  main()