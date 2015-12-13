import sqlite3
import random

from app.controllers.menu_manager import MenuManager
from app.controllers.db_manager import DatabaseManager
from app.controllers.twtr_manager import twtrManager

from app.models.boss import Boss
from app.models.character import Character
from app.models.dungeon import Dungeon

#
#   GameManager
#
#   Handles all game logic for the app, and makes calls to MenuManager and DBManager as needed.
#
class GameManager:
    #
    #   Init
    #
    def __init__(self):
        self.menu_manager = MenuManager(self)
        self.db_manager = DatabaseManager(self)
        self.twtr_manager = twtrManager()
        self.menu_manager.title_screen()



    #
    #   New Game
    #
    def new_game(self):
        self.menu_manager.title('New Game')
        # self.menu_manager.write("This is where the new game functionality will go.\nRight now there's nothing here.")

        self.dungeon_pick(self.char_creation())
        self.menu_manager.continue_prompt()
        self.menu_manager.title_screen()



    #
    #   Continue
    #
    def char_creation(self):
        firstHalf = "Ger Sym Hugh Ger Byssh Riff Vin Heg Gile Gau Ewl Gyl" \
                  "Rar Helm Thu Coel Erf Cane folke Knet Lenth Dene Hav Tun Thun".split() #24

        seconHalf = "y ey te nah ney ley walt wort man der dar dor da ness ke fin son kin".split() #18

        nickName1 = "Silent Horse Iron Grim Shadow Warrior Cold Queen King Prince Princess" \
                    " Mumble Quick  Flame".split() #14

        nickName2 = "Tongue Preserver Mouth Phantom Wonder Guardian Watcher Fist " \
                    "Slayer Hammer Sword Arrow".split() #12

        nickName3 = "Big Small Flamming Last First Great Final Burning Smug".split()

        nickName = ""

        # Total of 456 first name combinations
        if (random.randint(0,1) == 0): #Flips coin, determins if name will have one or two syllables
            firstName = firstHalf[random.randint(0,23)] + seconHalf[random.randint(0,17)]
        else:
            firstName = firstHalf[random.randint(0,23)]

        if (random.randint(0,1) == 0):#Flips coin, determins if name will have one or two syllables
            secondName = firstHalf[random.randint(0,23)] + seconHalf[random.randint(0,17)]
        else:
            secondName = firstHalf[random.randint(0,23)]
        while(firstName == secondName): #If first and last name are both the same, remakes last name.
            if (random.randint(0,1) == 0):
                secondName = firstHalf[random.randint(0,24)] + seconHalf[random.randint(0,17)]
            else:
                secondName = firstHalf[random.randint(0,24)]
        name = firstName + " " + secondName

        if (random.randint(0,1) == 0):

            if (random.randint(0,1) == 0):
                nickName += nickName1[random.randint(0,13)] + " " + nickName2[random.randint(0,11)]
            else:
                nickName += nickName2[random.randint(0,11)] + " " + nickName1[random.randint(0,13)]
        else: #Big Small Flamming Last First Great Final Burning
            if (random.randint(0,1) == 0):
                nickName = nickName1[random.randint(0,13)]
            else:
                nickName = nickName2[random.randint(0,11)]
            if (random.randint(0,1) == 0): #If Nickname appears as only one word then there is another flip to add another word
                nickName = nickName3[random.randint(0,6)] + " " + nickName

        if (random.randint(0,1) == 0 or nickName == "Tongue" or nickName == "Silent"or nickName == "Big"or nickName == "Small"
          or nickName == "Princess"):
            nickName = "the " + nickName
        else:
            nickName = "of the " + nickName + "s"
        fullName = name + " " + nickName
        gold = random.randint(1,5)
        job = ["Warrior", "Thief","Barbarian","Warrior Priest","Knight","Paladin"]
        youJob =  job[random.randint(1,5)]
        health = random.randint(80,400)
        #The longest sentence possible is a max of 122 characters to avoid going over twitters char limit
        if gold > 1:
            print "You are " + fullName + ". You are a " + youJob + ". You begin your adventure with only " + str(gold) + " coins."
        else:
            print "You're " + fullName + ". You are a " + youJob + ". You begin your adventure with only a single coin."

        conn = sqlite3.connect('DunSuciRun.sqlite')
        c = conn.cursor()
        p = conn.cursor()
        ch= conn.cursor()
        p.execute("SELECT USERNAME FROM PLAYERS")
        getUser = p.fetchall()
        userName = getUser[0][0]
        ch.execute("SELECT PLAYER FROM CHARACTERS WHERE PLAYER = ?",(userName,))
        check = ch.fetchall()
        if len(check) > 1:
            c.execute('INSERT INTO CHARACTERS VALUES (?,?,?,?,?)', (userName, fullName, youJob, health, gold))
        else:
            c.execute('UPDATE CHARACTERS SET NAME = ?, JOB = ?, HEALTH = ?,  GOLD = ? WHERE PLAYER = ?', (fullName, youJob, health, gold, userName))

        conn.commit()
        conn.close()

        new_char = Character(fullName, youJob, health)
        return new_char

    def continue_game(self):
        self.printTweet(self.menu_manager.title('Continue Game'))
        player = self.player_game()
        self.dungeon_pick(player)
        self.menu_manager.continue_prompt()
        self.menu_manager.title_screen()

    #
    #   Graveyard
    #
    def scoreboard(self):
        self.twtr_manager.printTweet(self.menu_manager.title('Scoreboard'))
        self.twtr_manager.printTweet(self.menu_manager.menu('scoreboard_menu'))
        self.menu_manager.title_screen()

    def get_report_list(self):
        chars = []
        conn = sqlite3.connect('DunSuciRun.sqlite')
        c = conn.cursor()
        c.execute('SELECT * FROM CHARACTERS')
        characters = c.fetchall()
        for character in characters:
            char = Character(character[0], character[1], character[2])
            chars.append(char)
        conn.close()
        return chars

    # def reporting(self):
    #     chars = self.get_report_list()
    #     self.menu_manager.title('View Scoreboard')
    #     for i in range(len(chars)):
    #         self.menu_manager.write(chars[i].numbered_stats(i+1))
    #
    #
    #     self.menu_manager.continue_prompt()


    # def reporting_save(self):
    #     chars = self.get_report_list()
    #     self.menu_manager.title('Download Scoreboard')
    #
    #     try:
    #         filename = input('Please enter a filename to save to (e.g. "reporting.txt"): ')
    #         f = open(filename, 'w')
    #
    #         f.write('----- Dungeon Suicide Run ------\n\n')
    #
    #         for i in range(len(chars)):
    #             f.write(chars[i].numbered_stats(i+1))
    #             f.write('\n')
    #
    #         f.close()
    #         self.menu_manager.write('Report has been written to: ' + str(filename))
    #         self.menu_manager.continue_prompt()
    #
    #     except:
    #         self.reporting_save()

    #
    #   Instructions
    #
    def instructions(self):
        # self.menu_manager.title('Instructions')
        # self.menu_manager.write("This game is about running through as many dungeons as you can before dying.\nTo start a new character Press"+
        #     " 1 and then decide what level of dungeon to run. Level is 1 is easy, 2 is medium, and 3 is hard.\nIf you wish to use an"+
        #     " existing character, press two. Then select which character you want to play with.\nReminder: each time you encounter a monster"+
        #     " you will take damage. When you select a character they will have some health already depleated.\nChoose your character and"+
        #     " dungeon level wisely!\nTo see current characters and their stats press 3.")
        self.twtr_manager.printTweet('You are an adventurer tasked with rid the world of evil. There is no rest. Every battle brings you closer to death.')

        self.menu_manager.continue_prompt()
        self.menu_manager.title_screen()

    #
    #   Quit
    #
    #   Exits the program (i.e. doesn't call another menu).
    #
    def quit(self):
        self.menu_manager.write("\nSee you soon!\n")

    #
    #   Dungeon Pick
    #
    def dungeon_pick(self, name):

            try:
                self.menu_manager.title(name.name)
                # level = raw_input("What level of dungeon would you like? (Easy, Medium or Hard)\n").lower()
                self.twtr_manager.printTweet("What level of dungeon would you like? (Easy, Medium or Hard)")
                level = self.twtr_manager.main()
                level = level.lower()
                print "You selected: " + level
                self.printTweet("You selected: " + level)
                if "easy" in level:
                    level = 1
                elif "medium" in level:
                    level = 2
                elif "hard" in level:
                    level = 3
                else:
                    # self.menu_manager.write('Level not recognized. Please choose Easy, Medium or Hard.')
                    self.printTweet('Level not recognized. Please choose Easy, Medium or Hard.')
                    self.dungeon_pick(name)
                useName = self.selectCurrentUser()
                if 1 <= level <= 3:
                    conn = sqlite3.connect('DunSuciRun.sqlite')
                    c = conn.cursor()
                    m = conn.cursor()
                    n = conn.cursor()
                    p = conn.cursor()
                    c.execute('SELECT * FROM DUNGEONS WHERE DIFFICULTY =' + str(level))
                    dungeons = c.fetchall()


                    randomNum= random.randint(0, len(dungeons)-1)
                    newTuple = dungeons[randomNum]
                    dun = Dungeon(newTuple[0],newTuple[1],newTuple[2]) #
                    dun.sign()
                    m.execute('SELECT * FROM BIGSCARIES WHERE THEME =?',(dun.theme,))
                    monsters = m.fetchall()
                    # print (monsters)
                    randoMon = random.randint(0, len(monsters)-1)
                    monsterTuple = monsters[randoMon]
                    mob = Boss(monsterTuple[0], monsterTuple[1], int(monsterTuple[2]))
                    horde = random.randint(0,(level*dun.difficulty))
                    # n.execute('UPDATE CHARACTERS SET HEALTH = ' + str((name.health - (mob.damage*dun.difficulty)))+ ', GOLD = ' + str(horde)+ ' WHERE NAME ="' + name.name + '"')
                    n.execute('UPDATE CHARACTERS SET HEALTH = ?, GOLD = ? WHERE NAME = ?',(str((name.health - (mob.damage*dun.difficulty))), horde, useName))
                    conn.commit()
                    conn.close()
                    # self.menu_manager.write("You slay a " + mob.name + " and collect " + str(horde) + " gold! " "It hurt you for " + str((mob.damage*dun.difficulty)) + " damage.")
                    self.twtr_manager.printTweet("You slay a " + mob.name + " and collect " + str(horde) + " gold! " "It hurt you for " + str((mob.damage*dun.difficulty)) + " damage.")
                else:
                    # self.menu_manager.write('Level not recognized. Please choose 1, 2, or 3.')
                    self.twtr_manager.printTweet('Level not recognized. Please choose 1, 2, or 3.')
                    self.dungeon_pick(name)

            except:
                self.twtr_manager.printTweet('Level not recognized. Please choose Easy, Medium or Hard.')
                # self.menu_manager.write('Level not recognized. Please choose Easy, Medium or Hard.')
                self.dungeon_pick(name)


    def player_game(self):
        chars = self.get_report_list()

        for i in range(len(chars)):
            self.menu_manager.write(chars[i].numbered_stats(i + 1))

        try:

            # player_number = input("\nType the number of the character you would like to play: ")
            self.twtr_manager.printTweet("Type the number of the character you would like to play")
            player_number = self.twtr_manager.main()
            player_number = int(player_number) - 1

            if 0 <= player_number <= (len(chars) - 1):
                return chars[player_number]
            else:
                # self.menu_manager.write(str(player_number))
                # self.menu_manager.write('\nCharacter not recognized. Please try again.\n')
                self.twtr_manager.printTweet(str(player_number))
                self.twtr_manager.printTweet('Character not recognized. Please try again.')
                self.player_game()

        except:
            # self.menu_manager.write(str(player_number))
            # self.menu_manager.write('\nCharacter not recognized. Please try again.\n')
            self.twtr_manager.printTweet(str(player_number))
            self.twtr_manager.printTweet('Character not recognized. Please try again.')
            self.player_game()

    def selectCurrentUser(self):
        conn = sqlite3.connect('DunSuciRun.sqlite')
        p = conn.cursor()
        p.execute("SELECT USERNAME FROM PLAYERS")
        getUser = p.fetchall()
        userName = getUser[0][0]
        conn.close()
        return userName