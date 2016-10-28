import twitter, datetime
import urllib2
import time
browsingHistory = open("/Users/csmaycock/Library/Application Support/Google/Chrome/Default/Current Session")

#CHROME CODE

while True:
    with open('/Users/csmaycock/Library/Application Support/Google/Chrome/Default/Current Session', 'r') as myfile:
        lines = myfile.read().split('http')
        lastLine = lines[-1]
        print (lastLine)

        #position = lastLine.find(chr(0))
        #print("The zero is at position " + str(position))

        bits = lastLine.split(chr(0))
        url = "http" +bits[0]
        #print (url)
        html = urllib2.urlopen(url).read()
        start = html.find('<title>') + 7
        end = html.find('</title>', start)
        title = html[start:end]

        #TWITTER CODE
        file = open("accesskeys.txt")
        creds = file.read().split('\n')
        api = twitter.Api(creds[0],creds[1],creds[2],creds[3])
        response = api.PostUpdate("I have been browsing " + str(title))
        time.sleep(60)






