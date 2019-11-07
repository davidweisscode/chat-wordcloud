import re
import csv
import time
from tqdm import tqdm

def isUserLine(string):
    if string == "User name1" or string == "User name2":
        return True
    else:
        return False

def isTextLine(string):
    if re.findall("^\d\d[.]\d\d[.]\d\d\d\d[,]\s\d\d[:]\d\d", string):
        return False
    elif string == "User name1" or string == "User name2":
        return False
    else:
        return True

def isDateTimeLine(string):
    if re.findall("^\d\d[.]\d\d[.]\d\d\d\d[,]\s\d\d[:]\d\d", string):
        return True
    else:
        return False

def getDate(string):
    return re.search("\d\d[.]\d\d[.]\d\d\d\d", string).group()

def getTime(string):
    return re.search("\d\d[:]\d\d", string).group()

encounteredTextLine = False
messages = []
file = open("fb-messages.txt", "r")

for line in tqdm(range(0, 53107)):
    line = file.readline().rstrip()
    if isUserLine(line):
        user = line

    if isTextLine(line) and not encounteredTextLine:
        text = line
        encounteredTextLine = True
    elif isTextLine(line) and encounteredTextLine:
        text = text + " " + line

    if isDateTimeLine(line):
        date = getDate(line)
        time = getTime(line)
        encounteredTextLine = False
        messages.append((date, time, "fb", user, text))

file.close()

for message in tqdm(range(0, len(messages))):
    tempTuple = messages[message]
    if tempTuple[3] == "User name1":
        messages[message] = (tempTuple[0], tempTuple[1], tempTuple[2], "User name3", tempTuple[4])
    # Reformat date to double digit
    newDate = tempTuple[0][:6] + tempTuple[0][8:]
    messages[message] = (newDate, tempTuple[1], tempTuple[2], tempTuple[3], tempTuple[4])

with open("fb-chat.csv", "w") as out:
    csv_out = csv.writer(out)
    csv_out.writerow(["date", "time", "plat", "user", "text"])
    for message in messages:
        csv_out.writerow(message)
