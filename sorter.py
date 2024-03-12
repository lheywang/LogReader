import os
from classes import LogEntry
from datetime import date, datetime


def SeekOnList(msg: str, words: list):
    for word in words:
        if word in msg:
            return True
    return False


def RemoveUselessCharacters(msg):
    output = ""
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
    s_msg = str(msg)
    for strc in s_msg.split("\\x"):
        if strc != "":
            if len(strc) > 6:
                for letter in strc:
                    out = strc
                    if letter in letters:
                        out = out + letter

                if out.isascii():
                    output = output + out
    output = output[:-1]
    for ch in output:
        if ch.isnumeric():
            output = output[1:]
        else:
            break
    return output


def ClearLogEntry(Log: LogEntry):
    Log.msg = RemoveUselessCharacters(Log.msg)
    Log.src = RemoveUselessCharacters(Log.src)
    Log.date = RemoveUselessCharacters(Log.date)
    return Log


def DateFormatter(Log: LogEntry):
    for month in (
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ):
        pos = Log.date.find(month)
        if pos > -1:
            Log.date = Log.date[pos:]
            Log.date = Log.date[0:15]
            return Log
    Log.date = ""
    return Log


def IsLogOld(Log: LogEntry, threshold: int):
    try:
        now = datetime.now()
        LogDate = datetime.strptime(Log.date, "%b %d %H:%M:%S")
        LogDate = LogDate.replace(year=now.year)
        diff = now - LogDate
        if diff.days < threshold:
            return False
        else:
            return True
    except:
        # In case of error, let just use the log as it is
        return False


def sorter(logs: list, Levels: dict):
    # Creating the output container
    LevelsID = []
    for Level in Levels.keys():
        LevelsID.append(int(Level[5:]))
    LevelNumber = max(LevelsID)

    LogLevel = []
    for index in range(LevelNumber + 1):
        LogLevel.append([])

    for log in logs:
        # Remove usuless data (Non ascii characters from the string)
        log = ClearLogEntry(log)

        # Format the date
        log = DateFormatter(log)

        # If the log is older than 50 days, just forget it and remove it
        if IsLogOld(log, 31):
            continue
        for Level, WordList in Levels.items():
            # Now create multiples levels of logs...
            result = SeekOnList(log.msg, WordList)
            if result == True:
                LogLevel[int(Level[5:])].append(log)
    return LogLevel
