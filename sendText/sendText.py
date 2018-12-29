#Written by Stephen Hawes December 2018 for Tom's Hardware
#stephenhawes.com

import serial
import time
import feedparser
import re


###################
# MAKE EDITS HERE #
###################
numOfTitles = 20
rssLink = "https://www.tomshardware.com/feeds/rss2/articles.xml"
serialPort = "/dev/ttyUSB0"
###################
# STOP EDITS HERE #
###################

NewsFeed = feedparser.parse(rssLink)
ser = serial.Serial(serialPort, 9600)
time.sleep(3)

titleCounter = 0

try:
    print(NewsFeed.entries[0].title)
except:
    while(True):
        encoded = ("Toms Hardware\n").encode('utf-8')
        ser.write(encoded)
        time.sleep(7)


#getting titles from feed, saving them in array "titles" and cutting them into 128 char segments in case the titles are too long
titles = [0] * numOfTitles
for i in range(0,numOfTitles):
    curTitle = NewsFeed.entries[i].title
    titles[i] = re.findall('.{1,128}', curTitle)

#printing out all titles as a sanity check
print(titles)

#printTitle() method: scrolls the title in titles[] array at index titleCounter
def printTitle():
    for j in range(len(titles[titleCounter])):
        print(titles[titleCounter][j])
        encoded = (titles[titleCounter][j] + "\n").encode('utf-8')
        ser.write(encoded)
        print("Title character length:")
        print(len(titles[titleCounter][j]))
        sleepVal = ((24 + (len(titles[titleCounter][j]) * 6)) * 0.05) + 1
        print("Delay time to allow for scrolling:")
        print(sleepVal)
        time.sleep(sleepVal)
        print("---")

#loop through all titles in "titles" using the printTitle() method. handle changing titleCounter variable to cycle through titles
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
