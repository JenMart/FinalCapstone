__author__ = 'Jen Mart'

import random

class Game:
    # randomWords = "blueberry homewards zero banana gravel hairless avenging highway circuitry agency".split()
    # word = randomWords[random.randint(0,9)]
    #RandomWords consists of the same words in the tryFile.txt
    #I left this bit of code incase of troubles using the file attachment
    def __init__(self, fileOpen, foString ):
        self.fileOpen = fileOpen
        self.foString = foString


    # fileOpen = open("tryFile.txt", "r")
    # foString = fileOpen.read().split()
    # word = foString[random.randint(0,9)]
    # print word



    # def makeStars(theWord):
    #     wordCount = len(theWord)
    #     starCounter = 0
    #     winState = ""
    #     while wordCount > starCounter: ##Determines the number of letters in the word and makes an * version
    #         winState += "*"
    #         starCounter += 1


    def HangMan(self):
        fileOpen = open("tryFile.txt", "r")
        foString = fileOpen.read().split()
        word = foString[random.randint(0,9)]
        print word
        wordCount = len(word)
        starCounter = 0
        winState = ""
        while wordCount > starCounter: ##Determines the number of letters in the word and makes an * version
            winState += "*"
            starCounter += 1
        turns = 0
        wrongLetters = ""
        rightLetters = ""
        hangManWord = "H A N G M A N ".split()
        failState = ""
        wordCount = len(word)
        starCounter = 0
        while turns != 7:
            print failState
            print winState
            print "Guess a letter"
            playerInput = raw_input()
            if len(playerInput) != 1: #Confirms only a single character has been used.
                print("please enter only a single character")
            else:
                playerInput.lower() #lowers the case of the character to avoid confusion
                counterThing = 0
                #If player enters a character already used, the system informs them.

                if playerInput in rightLetters or playerInput in wrongLetters:
                    print "You've already guessed that"
                    print "\n"
                else:
                    if playerInput in word:
                        print "correct!"
                        print "\n"
                        rightLetters += playerInput
                        currentLetter = playerInput
                        #If a player guesses correctly, the system adds the correct letter
                        # were it's corresponding astrisk is located
                        while wordCount != counterThing:
                            if currentLetter in word[counterThing]:
                                winState = winState[:counterThing] + currentLetter + winState[counterThing + 1:]
                                counterThing += 1
                            else:
                                counterThing += 1
                    else:
                        print "incorrect!"
                        print "\n"
                        wrongLetters += playerInput + " "
                        failState += hangManWord[turns]
                        turns += 1
                    if turns == 7:
                        print failState
                        print "you lose! The answer was " + word
                        break
                    if winState == word:
                        print "you win! The answer was " + winState
                        break
                if len(wrongLetters) > 0:
                    print "Incorrect letters used: " +  wrongLetters
    # makeStars(word)
