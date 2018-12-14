import serial
import time
import feedparser
import re

numOfTitles = 5

NewsFeed = feedparser.parse("https://www.tomshardware.com/feeds/rss2/articles.xml")
ser = serial.Serial('/dev/cu.wchusbserial14210', 9600)

time.sleep(3)

#getting titles from feed, saving them in array "titles" and cutting them into 78 char segments
titles = [0] * numOfTitles
for i in range(0,numOfTitles):
    curTitle = NewsFeed.entries[i].title
    titles[i] = re.findall('.{1,78}', curTitle)
print(titles)

#write out each title to the serial port, by way of each 78 char segment of each title
while(True):
    for i in range(len(titles)):
        for j in range(len(titles[i])):
            print(titles[i][j])
            encoded = (titles[i][j] + "\n").encode('utf-8')
            ser.write(encoded)
            print(len(titles[i][j]))
            sleepVal = ((24 + (len(titles[i][j]) * 6)) * 0.05)
            print(sleepVal)
            time.sleep(sleepVal)






#sending bespoke strings to the arduino to scroll

#while True:
#    inputted = (input("text:") + "\n").encode('utf-8')
#    ser.write(inputted)

