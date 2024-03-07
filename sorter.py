import os
from classes import LogEntry


def SeekOnList(msg: str, words: list):
    for word in words:
        if word in msg:
            return True
    return False


def sorter(logs: list, Levels: dict):
    # Creating the output container
    LevelsID = []
    for Level in Levels.keys():
        LevelsID.append(int(Level[5:]))
    LevelNumber = max(LevelsID)
    LogLevel = []
    for index in range(LevelNumber):
        LogLevel.append([])

    for log in logs:
        for Level, WordList in Levels.items():
            # Now create multiples levels of logs...
            result = SeekOnList(log.msg, WordList)
            if result == True:
                LogLevel[int(Level[5:])].append(log)
    return LogLevel
