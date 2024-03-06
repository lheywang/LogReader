from math import log
import os
import shutil

import time


def reader(logpath: str, keyword: str):
    print("Start seeking for %s" % keyword)

    for path, subdirs, files in os.walk(logpath):
        for name in files:
            file = os.path.join(path, name)
            f = open(file, "rb")
            for line in f:
                if keyword in str(line):
                    print("KEYWORD FOUND : %s" % keyword)
    print("End !")
    return
