import re
import csv
from datetime import datetime

messages = csv.reader(open("chat.csv", "r"))
next(messages)

# Sort by datetime
sortedmessages = sorted(messages, key = lambda message: datetime.strptime(message[0] + message[1], "%d.%m.%y%H:%M"))

for message in sortedmessages:
    # Change text to lowercase
    message[4] = message[4].lower()
    # Remove special characters
    message[4] = re.sub(".*http.*","link", message[4])
    # Remove img links
    message[4] = re.sub("img\salt.*"," ", message[4])
    message[4] = re.sub("width.*"," ", message[4])
    message[4] = re.sub(","," ", message[4])
    message[4] = re.sub("\."," ", message[4])
    message[4] = re.sub("\?"," ", message[4])
    message[4] = re.sub("\<"," ", message[4])
    message[4] = re.sub("\>"," ", message[4])
    message[4] = re.sub(".quot."," ", message[4])
    # Remove double and trailing whitespace
    message[4] = " ".join(message[4].split())
    # Remove empty text
    if message[4] == "":
        sortedmessages.remove(message)

with open("chat.csv", "w", newline = "") as file_out:
    wr = csv.writer(file_out)
    wr.writerows(sortedmessages)
