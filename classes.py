class LogEntry:
    def __init__(self, date, src, message):
        self.date = date
        self.src = src
        self.msg = message

    def __str__(self):
        return "LOG ON %s FROM %s : %s" % (self.date, self.src, self.msg)
