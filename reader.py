import os
from classes import LogEntry
from datetime import datetime


def RemoveUselessSpaces(str):
    for index in range(len(str) - 1):
        if str[index] == " ":
            while (str[index + 1]) == " ":
                str = str[:index] + str[index + 1 :]
                if index + 1 == len(str):
                    break
        if str[index] == " " and index == 0:
            str = str[1:]
        if index + 1 == len(str):
            break
    return str


def IsMessageSimilar(str1, str2):

    str1 = RemoveUselessSpaces(str1)
    str2 = RemoveUselessSpaces(str2)

    len1 = len(str1)
    len2 = len(str2)

    LenToCompare = min(len1, len2)

    CommonChar = 0
    for index in range(LenToCompare):
        if str1[index] == str2[index]:
            CommonChar += 1

    # 88% Of the chars are similar : Let's consider them equal
    if CommonChar > LenToCompare * 0.88:
        return True
    return False


def reader(logpath: str, keyword: str):
    print("Start seeking for %s" % keyword)
    logs = []

    for path, subdirs, files in os.walk(logpath):
        for name in files:
            file = os.path.join(path, name)
            f = open(file, "rb")
            for line in f:
                sline = str(line)
                if keyword in sline:
                    try:
                        # Extracting the data from the log line
                        buf = sline.split(":")
                        subbuf = buf.pop(2).split(" ")
                        date = buf.pop(0) + ":" + buf.pop(0) + ":" + subbuf.pop(0)
                        src = subbuf.pop(1)
                        message = " ".join(buf)

                        # Checking if a similar message already exists
                        to_add = 1
                        for log in logs:
                            if IsMessageSimilar(message, log.msg) == True:
                                to_add = 0
                                message = RemoveUselessSpaces(message)
                        # If no messages are found, append them to the log collection
                        if to_add == 1:
                            log = LogEntry(date, src, message)
                            logs.append(log)
                            to_add = 0
                    except:
                        # If fail, do nothing and jump on the next
                        pass
    print("\tEnded seeking for %s" % keyword)
    return logs
