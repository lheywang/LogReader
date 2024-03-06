import tomllib
from multiprocessing import Queue, Process

from reader import reader
from files import FilesCopy, FilesExtraction
from classes import LogEntry


if __name__ == "__main__":
    # Copying and extracting files
    FilesCopy("full_logs", "temp")
    FilesExtraction("C:\\Dev\\logs\\reader\\LogReader\\temp")

    # Openning the TOML File
    with open("keywords.toml", "rb") as t:
        words = tomllib.load(t)

    # Iterating trough the keywords and start an approppriate word
    processes = []
    for keywords, attributes in words.items():
        print(keywords, attributes)
        processes.append(
            Process(
                target=reader,
                args=(
                    "C:\\Dev\\logs\\reader\\LogReader\\temp",
                    keywords,
                ),
            )
        )

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print("END !")

"""



reader("C:\\Dev\\logs\\reader\\LogReader\\temp", "dionysos")
"""
