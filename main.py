import os

print("Hello World !")

f = []
layer = 1
w = os.walk("/")
for (dirpath, dirnames, filenames) in w:
    if layer == 2:
        f.extend(dirnames)
        break
    layer += 1

print(f)