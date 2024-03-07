import tomllib
from multiprocessing import Pool, Queue, Process
import time

from reader import reader
from sorter import sorter
from files import FilesCopy, FilesExtraction
from classes import LogEntry


if __name__ == "__main__":
    # Copying and extracting files
    FilesCopy("full_logs", "temp")
    FilesExtraction("C:\\Dev\\logs\\reader\\LogReader\\temp")

    # Openning the TOML File
    with open("keywords.toml", "rb") as t:
        config = tomllib.load(t)

    # Iterating trough the keywords and start an approppriate word
    args = []
    for keywords in config["Keywords"]:
        args.append(("C:\\Dev\\logs\\reader\\LogReader\\temp", keywords))

    pool = Pool()
    results = pool.starmap(reader, args)

    """
    TO DO : Start a worker pool task to sort all of the outputed logs
    Then, PDF Creation.
    """
    print(sorter(results[20], config["Output"]["Output"]))

    print("END !")

"""



reader("C:\\Dev\\logs\\reader\\LogReader\\temp", "dionysos")
"""
