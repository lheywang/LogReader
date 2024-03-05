import os
import shutil
import gzip
import time

#
# Copying files to a temp directory
#
start_copy = time.time()
src = "full_logs"
dst = "temp"

try :
    shutil.rmtree(dst)
except :
    print("Cannot remove the folder")

files = os.listdir(src)
shutil.copytree(src, dst)
print("Files copied")
end_copy = time.time()

#
# Extracting .gz files to their ascii versions
#
for path, subdirs, files in os.walk("C:\\Dev\\logs\\reader\\LogReader\\temp"):
    for name in files:
        file = os.path.join(path, name)
        if file.endswith(".gz"):
            with gzip.open(file) as fi:
                fo = open(file[:-3]+ ".txt", "wb")
                fo.write(fi.read())
                fo.close()
            os.remove(file)

end_gz = time.time()
print("Files extracted")

#
# Printing execution time
# 
print(end_copy - start_copy)
print(end_gz - end_copy)

#
# Launching readers 
#