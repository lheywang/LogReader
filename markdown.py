from unicodedata import category
import mdutils
from classes import LogEntry
from datetime import datetime


def LevelCounter(Logs):
    LogLevelCounter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for keylog in Logs:
        LevelIndex = 0
        for level in keylog:
            LogLevelCounter[LevelIndex] += len(level)
            LevelIndex += 1
    return LogLevelCounter


def Exporter(SortedLogs, Levels: dict, Keywords: list):
    LogCount = LevelCounter(SortedLogs)
    now = datetime.now()

    # Force the file creation
    with open("report.md", "w+") as f:
        f.close()

    # Creating the "file" ==> The lib create it at the end
    mdfile = mdutils.MdUtils(
        file_name="report.md",
        title="",
    )

    mdfile.write("# Report on %04d/%02d/%02d\n" % (now.year, now.month, now.day))

    # Disclaimers
    # mdfile.new_header(level=2, title="Disclaimers", style="setext")
    mdfile.write(
        "This report was generated automatically to recap the logs.\n"
        "Please leave in mind that\n\n"
        "- They depend on YOUR configuration (keywords.toml)\n"
        "- Thus, this report may not include every log that you want / you need to see.\n"
        "- The script ELIMINATE logs that are older than 50 days.\n\n"
    )

    # Logs statistics
    mdfile.write("## Logs\n")

    # Log Count Tab
    mdfile.write("### Logs Counts\n")
    mdfile.write(
        "You will find here a tab that recap the number of logs that occured within the last 50 days, counted by category\n"
    )
    TabText = ["Category :", "Level :", "Number of logs :"]
    for x in range(len(LogCount)):
        if x == 0:
            category = "High Importance"
        elif x == 3:
            category = "Median Importance"
        elif x == 6:
            category = "Low Importance"
        elif x == 9:
            category = "Reported log"
        else:
            category = ""
        Level = "Level " + str(x)
        Count = str(LogCount[x])
        TabText.extend([category, Level, Count])
    mdfile.new_table(
        columns=3,
        rows=11,
        text=TabText,
    )

    # Log settings useds
    mdfile.write("### Output parameters\n")
    mdfile.write(
        "Here are listed the parameters used when creating this report. Check if everything is correct.\n"
        "Otherwise, your report may be incomplete\n"
    )

    # Keywords that were used to class the logs :
    TabText = ["Level :", "Keywords :"]
    for keys, values in Levels.items():
        t_values = ""
        for value in values:
            if t_values == "":
                t_values = value
            else:
                t_values += " | " + value
        TabText.extend([keys, t_values])
    mdfile.new_table(
        columns=2,
        rows=11,
        text=TabText,
    )

    # Keywords that were used to generate log in the script :
    mdfile.write("### Keywords that were seeked\n")
    col = 8
    TabText = ["Keywords :"]

    for _ in range(col - 1):
        TabText.append("")

    for word in Keywords:
        TabText.append(word)

    # +1 to go upper, and + 1 to add the "header" rows
    row = round(len(Keywords) / col) + 2
    target = row * col
    diff = target - len(Keywords)
    for _ in range(diff):
        TabText.append("")  # Fill the tab to match the required size
    mdfile.new_table(
        columns=col,
        rows=row + 1,
        text=TabText,
    )

    mdfile.write("## Logs messages\n")

    LogsPerLevel = []
    for _ in range(10):
        LogsPerLevel.append([])

    for keylog in SortedLogs:
        index = 0
        for level in keylog:
            LogsPerLevel[index].extend(level)
            index += 1

    mdfile.write("\n### Level 0")
    for log in LogsPerLevel[0]:
        TabText = ["Date :", "Source :", "Message : "]
        TabText.extend([log.date, log.src, log.msg])
        mdfile.new_table(
            columns=3,
            rows=2,
            text=TabText,
        )

    mdfile.write("\n### Level 1")
    for log in LogsPerLevel[1]:
        TabText = ["Date :", "Source :", "Message : "]
        TabText.extend([log.date, log.src, log.msg])
        mdfile.new_table(
            columns=3,
            rows=2,
            text=TabText,
        )

    mdfile.write("\n### Level 2")
    for log in LogsPerLevel[2]:
        TabText = ["Date :", "Source :", "Message : "]
        TabText.extend([log.date, log.src, log.msg])
        mdfile.new_table(
            columns=3,
            rows=2,
            text=TabText,
        )

    mdfile.write("\n### Level 3")
    for log in LogsPerLevel[3]:
        TabText = ["Date :", "Source :", "Message : "]
        TabText.extend([log.date, log.src, log.msg])
        mdfile.new_table(
            columns=3,
            rows=2,
            text=TabText,
        )

    mdfile.write("\n### Level 4")
    for log in LogsPerLevel[4]:
        TabText = ["Date :", "Source :", "Message : "]
        TabText.extend([log.date, log.src, log.msg])
        mdfile.new_table(
            columns=3,
            rows=2,
            text=TabText,
        )

    mdfile.write("\n### Level 5")
    for log in LogsPerLevel[5]:
        TabText = ["Date :", "Source :", "Message : "]
        TabText.extend([log.date, log.src, log.msg])
        mdfile.new_table(
            columns=3,
            rows=2,
            text=TabText,
        )

    mdfile.write("\n### Level 6")
    for log in LogsPerLevel[6]:
        TabText = ["Date :", "Source :", "Message : "]
        TabText.extend([log.date, log.src, log.msg])
        mdfile.new_table(
            columns=3,
            rows=2,
            text=TabText,
        )

    mdfile.write("\n### Level 7")
    for log in LogsPerLevel[7]:
        TabText = ["Date :", "Source :", "Message : "]
        TabText.extend([log.date, log.src, log.msg])
        mdfile.new_table(
            columns=3,
            rows=2,
            text=TabText,
        )

    mdfile.write("\n### Level 8")
    for log in LogsPerLevel[8]:
        TabText = ["Date :", "Source :", "Message : "]
        TabText.extend([log.date, log.src, log.msg])
        mdfile.new_table(
            columns=3,
            rows=2,
            text=TabText,
        )

    mdfile.write("\n### Level 9")
    for log in LogsPerLevel[9]:
        TabText = ["Date :", "Source :", "Message : "]
        TabText.extend([log.date, log.src, log.msg])
        mdfile.new_table(
            columns=3,
            rows=2,
            text=TabText,
        )

    mdfile.write("\nEnd of the logs report.\n")
    mdfile.create_md_file()
    return 0
