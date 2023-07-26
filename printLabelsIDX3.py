import random

labels = open('./UnzippedBinary/t10k-labels.idx1-ubyte', 'rb')

print('must be 2049', int.from_bytes(labels.read(4)))
lab_count = int.from_bytes(labels.read(4))
print(lab_count)

print()

images = open('./UnzippedBinary/t10k-images.idx3-ubyte', 'rb')

print('must be 2051', int.from_bytes(images.read(4)))
img_count = int.from_bytes(images.read(4))
print(img_count)

print(int.from_bytes(images.read(4)))
print(int.from_bytes(images.read(4)))



exit()







for i in range(img_count):
    lb = labels.read(1)
    lb = ord(lb)

    
    

    if i == 0:
        print(i, lb)
        for j2 in range(28):
            for i2 in range(28):
                pixel = images.read(1)

                print("%4s" % pixel[0], end = '')


                
                
            
            print('\n\n')