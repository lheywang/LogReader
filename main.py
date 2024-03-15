import tomllib
from multiprocessing import Pool

from reader import reader
from sorter import sorter
from files import FilesCopy, FilesExtraction
from markdown import Exporter
from time import time

if __name__ == "__main__":
    # Copying and extracting files
    start = time()
    print("Start Copying and Extracting files")

    # Openning the TOML File and parsing it
    with open("keywords.toml", "rb") as t:
        config = tomllib.load(t)

    FilesCopy(config["source"], config["workzone"])
    FilesExtraction(config["workzone"])

    # Creating a pool on all cores available
    pool = Pool()

    # Creating an args tab to be passed to te pool. Each worker will seek one (or multiples) word(s)
    args = []
    for keywords in config["Keywords"]:
        args.append((config["workzone"], keywords))

    # Launching the reading process on all cores, with for each one a specific argument set
    results = pool.starmap(reader, args)

    # Re-using the args tab, with new args;
    args = []
    for result in results:
        args.append((result, config["Output"]))
    # Launching the sorting process on all cores, with each one a specific argument set
    print("Start Sorting all of the logs, per Keyword")
    logs = pool.starmap(sorter, args)

    print("Starting Final Export of logs")
    Exporter(logs, config["Output"], config["Keywords"], config["export"])

    end = time()
    print("END !")
    print("Executed in : ", (end - start) / 60, " mn")
