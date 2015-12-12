import sqlite3
import datetime
from app.controllers import db_manager
from app.controllers.db_manager import DatabaseManager

__author__ = 'Jen Mart'
import tweepy, time, sys, json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import string
import Tkinter
import json
from Tkinter import *



class twtrManager:
    def __init__(self):
        self.db_manager = DatabaseManager(self)
        self.main()

    def main(self):
        SCREEN_NAME = 'Jen_B_Mart'
        ckey = 'rlee33vXmHIlmR5tQljIX0ucD'
        csecret = 'cUiIFESIXSSin9YJHYwLnVwnHpS64Ytj7csY9yFqshvAlkcaPg'
        atoken = '2836017980-DxYDsgHqGMyRIq1yH3Uf3Ar63eYCFhqawJAWGOw'
        asecret = 'SruNXYjh0BpY4GQhiflXaxbB2XUhrCMslBrmrH2ViULnu'

        auth = tweepy.OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        api = tweepy.API(auth)
        auth = OAuthHandler(ckey, csecret)

        self.homeTimeline(ckey,csecret,atoken,asecret,auth,api)
    # def mainMenu(ckey,csecret,atoken,asecret,auth,api, self):
    #     name = raw_input("Enter name \n")
    #     text = raw_input("Enter text \n")
    #     date = datetime.datetime.now().time()
    #     db_manager.storeTweets(name, text, date)
    #     # thing = input("Type anything to continue")
    #     # if thing != "j2hde":
    #     #     homeTimeline(ckey,csecret,atoken,asecret,auth,api)
    def homeTimeline(self, ckey,csecret,atoken,asecret,auth,api):
        # timeline=api.home_timeline(OUNT=0)
        # try:
        #     for tweet in timeline:
        #         user=tweet.user
        #         name=tweet.user.name.encode('utf-8')
        #         text=tweet.text.encode('utf-8')
        #         # print(name +"\n"+ text)
        #         # print("\n")
        #         if "@DunSuciRun" in text: #checks if special text in field
        #             check = self.db_manager.checkUser(name) #checks if user exists
        #             if (check): #if yes
        #                 check = self.db_manager.checkTweets() #sends out to another method to check if in db
        #                 if (check): #If not, add to DB
        #                     date = date();
        #                     text = text[11:]
        #                     self.db_manager.storeTweets(name, text, 1)
        #                 else: #If exists in DB then waits for a minute
        #                     self.executeMinute()
        #         else: #if nothing changes, waits.
        #             self.executeMinute()
        #
        # except Exception, e:
        #     pass

        # self.mainMenu(ckey,csecret,atoken,asecret,auth,api)
        date = datetime;
        print date
        self.db_manager.storeTweets("name", "1", date)

    def printTweet(self,text): #Works perfectly!
        ckey = 'rlee33vXmHIlmR5tQljIX0ucD'
        csecret = 'cUiIFESIXSSin9YJHYwLnVwnHpS64Ytj7csY9yFqshvAlkcaPg'
        atoken = '2836017980-DxYDsgHqGMyRIq1yH3Uf3Ar63eYCFhqawJAWGOw'
        asecret = 'SruNXYjh0BpY4GQhiflXaxbB2XUhrCMslBrmrH2ViULnu'
        auth = tweepy.OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        api = tweepy.API(auth)
        auth = OAuthHandler(ckey, csecret)

        # api.update_status(text)
        print "demo!"
        print text
        return

    def executeSomething(self):
        time.sleep(60) #set up to check for tweets every minute.

        while True:
            self.main()

    # def homeTimeline(ckey,csecret,atoken,asecret,auth,api):
    #     timeline=api.home_timeline(COUNT=0)
    #     try:
    #         for tweet in timeline:
    #             user=tweet.user
    #             name=tweet.user.name.encode('utf-8')
    #             text=tweet.text.encode('utf-8')
    #             # print(name +"\n"+ text)
    #             # print("\n")
    #             if "@DunSuciRun" in text:
    #                 print(name +"\n"+ text)
    #                 print("\n")
    #                 date = date();
    #                 self.db_manager.storeTweets(name, text, date)
    #                 # storeTweets(name, text, date)
    #                 # postTweet(ckey,csecret,atoken,asecret,auth,api, name, text)
    #     except Exception, e:
    #         pass
    #
    #     self.mainMenu(ckey,csecret,atoken,asecret,auth,api)
    # def directMessages(ckey,csecret,atoken,asecret,auth,api):
    #     message = api.direct_messages()
    #
    # def postTweet(ckey,csecret,atoken,asecret,auth,api,name, text):
    #     auth = tweepy.OAuthHandler(ckey, csecret)
    #     auth.set_access_token(atoken, asecret)
    #     status= "@" + name + " Returned!"
    #     api.update_status(status)
    #     print("\n")
    #     print("Tweet posted!")
    #     print("\n")
    #     self.mainMenu(ckey,csecret,atoken,asecret,auth,api)

    # def setup(self):
    #     conn = sqlite3.connect('DunSuciRun.sqlite')
    #     c = conn.cursor()
    #     players = """ CREATE TABLE PLAYERS (
    #                 USERNAME VARCHAR(255) NOT NULL,
    #                 MESSAGE VARCHAR(255) NOT NULL,
    #                 STEP INT NOT NULL )"""
    #     c.execute(players)
    #     conn.commit()
    #     conn.close()
    #             # for i in range(len(monsters)):
    #             # print ("Add " + monsters[i] + " to database")
    #             # c.execute("INSERT INTO BIGSCARIES VALUES (?, ?, ?)", (monsters[i], types[i], health[i]))

    # def storeTweets(name, text, date):
    #     conn = sqlite3.connect('DunSuciRun.sqlite')
    #     c = conn.cursor()
    #
    #     print("Adding user data to Database")







