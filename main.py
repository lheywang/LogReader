import tomllib
from multiprocessing import Pool, Queue, Process
import time

from reader import reader
from sorter import sorter, ClearLogEntry
from files import FilesCopy, FilesExtraction
from classes import LogEntry


if __name__ == "__main__":
    # Copying and extracting files
    FilesCopy("full_logs", "temp")
    FilesExtraction("C:\\Dev\\logs\\reader\\LogReader\\temp")

    # Openning the TOML File and parsing it
    with open("keywords.toml", "rb") as t:
        config = tomllib.load(t)

    # Creating a pool on all cores available
    pool = Pool()

    # Creating an args tab to be passed to te pool. Each worker will seek one (or multiples) word(s)
    args = []
    for keywords in config["Keywords"]:
        args.append(("C:\\Dev\\logs\\reader\\LogReader\\temp", keywords))

    # Launching the reading process on all cores, with for each one a specific argument set
    results = pool.starmap(reader, args)

    # Re-using the args tab, with new args;
    args = []
    for result in results:
        args.append((result, config["Output"]["Output"]))

    # Launching the sorting process on all cores, with each one a specific argument set
    logs = pool.starmap(sorter, args)

    # DEBUG OUTPUT
    for keylog in logs:
        for level in keylog:
            for log in level:
                print(log)

    #
    # TO DO : Exporter in PDF
    #

    print("END !")
