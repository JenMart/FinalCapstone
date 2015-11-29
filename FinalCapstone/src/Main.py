__author__ = 'jensinamart'
import tweepy, time, sys, json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import string
import Tkinter
import json
from Tkinter import *

SCREEN_NAME = 'Jen_B_Mart'
ckey = 'rlee33vXmHIlmR5tQljIX0ucD'
csecret = 'cUiIFESIXSSin9YJHYwLnVwnHpS64Ytj7csY9yFqshvAlkcaPg'
atoken = '2836017980-DxYDsgHqGMyRIq1yH3Uf3Ar63eYCFhqawJAWGOw'
asecret = 'SruNXYjh0BpY4GQhiflXaxbB2XUhrCMslBrmrH2ViULnu'

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)
auth = OAuthHandler(ckey, csecret)



test = raw_input("Type Stream, tweet or search. ")
if test == "stream":
    thing = raw_input("Enter a subject: ")
    class listener(StreamListener):

        def on_data(self, data):
            try:
                tweetText = data.split(',"text":"')[1].split('","source')[0]
                print tweetText

                saveTime = str(time.time())+':::'+tweetText
                timeStamp = str(time.localtime().tm_hour) + str(time.localtime().tm_mday) + str(time.localtime().tm_mon) + str(time.localtime().tm_year)
                fileName = 'TweepyTestSave ' + timeStamp + '.doc'
                print timeStamp
                saveFile = open(fileName, 'a') #'a' means append
                saveFile.write(saveTime)
                saveFile.write('\n') # \n means write to new line
                saveFile.close()
                return True
            except BaseException, e: #If can't this line (e) write to file...
                print 'failed ondata, ',str(e) #Leave this message
                time.sleep(10) #Try again in 10 seconds

        def on_error(self, status):
            print status

        auth.set_access_token(atoken, asecret)

    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=[thing])