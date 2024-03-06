import os
import shutil
import gzip


def FilesCopy(src, dst):
    try:
        shutil.rmtree(dst)
    except:
        print("Cannot remove the folder")

    files = os.listdir(src)
    shutil.copytree(src, dst)
    return


def FilesExtraction(FilesPath):
    for path, subdirs, files in os.walk(FilesPath):
        for name in files:
            file = os.path.join(path, name)
            if file.endswith(".gz"):
                with gzip.open(file) as fi:
                    fo = open(file[:-3] + ".txt", "wb")
                    fo.write(fi.read())
                    fo.close()
                os.remove(file)
    return
