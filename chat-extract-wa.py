import re
import csv
import time
from tqdm import tqdm

def isNewMessage(string):
    if re.findall("^\d\d[.]\d\d[.]\d\d[,]\s\d\d[:]\d\d\s[-]\s", str(string)):
        return True
    else:
        return False

messages = []
file = open("wa-messages.txt", "r")

for line in range(0, 1901):
    line = file.readline().rstrip()
    if isNewMessage(line):
        date, rest = line.split(", ", 1)
        time, rest = rest.split(" - ", 1)
        name, text = rest.split(": ", 1)
        messages.append((date, time, "wa", name, text))
    elif len(line) > 0: # Bundle lines with linebreaks into one single message
        date, time, platform, name, text = messages.pop()
        messages.append((date, time, platform, name, text + " " + line))

file.close()

with open("wa-chat.csv", "w") as out:
    csv_out = csv.writer(out)
    csv_out.writerow(["date", "time", "plat", "user", "text"])
    for message in messages:
        csv_out.writerow(message)
