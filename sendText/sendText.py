import serial
import time
import feedparser
import re

numOfTitles = 20
titleCounter = 0

NewsFeed = feedparser.parse("https://www.tomshardware.com/feeds/rss2/articles.xml")
ser = serial.Serial('/dev/cu.wchusbserial14210', 9600)

time.sleep(3)

#getting titles from feed, saving them in array "titles" and cutting them into 78 char segments
titles = [0] * numOfTitles
for i in range(0,numOfTitles):
    curTitle = NewsFeed.entries[i].title
    titles[i] = re.findall('.{1,128}', curTitle)
print(titles)

def printTitle():
    for j in range(len(titles[titleCounter])):
        print(titles[titleCounter][j])
        encoded = (titles[titleCounter][j] + "\n").encode('utf-8')
        ser.write(encoded)
        print(len(titles[titleCounter][j]))
        sleepVal = ((24 + (len(titles[titleCounter][j]) * 6)) * 0.05) + 1
        print(sleepVal)
        time.sleep(sleepVal)

def animation():
    encoded = ("<>\n").encode('utf-8')
    ser.write(encoded)

#write out each title to the serial port, by way of each 78 char segment of each title
while(True):
    printTitle()
    if titleCounter == numOfTitles - 1:
        titleCounter = 0
    else:
        titleCounter = titleCounter + 1
    




#sending bespoke strings to the arduino to scroll

#while True:
#    inputted = (input("text:") + "\n").encode('utf-8')
#    ser.write(inputted)

