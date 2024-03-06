import os
from socket import MsgFlag
from classes import LogEntry


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
                        date = buf.pop(0) + buf.pop(0) + subbuf.pop(0)
                        src = subbuf.pop(1)
                        message = " ".join(buf)

                        # Checking if a similar message already exists
                        to_add = 1
                        for log in logs:
                            if message == log.msg:
                                to_add = 0

                        # If no messages are found, append them to the log collection
                        if to_add == 1:
                            log = LogEntry(date, src, message)
                            logs.append(log)

                    except:
                        pass
    for log in logs:
        print(log)
    return
