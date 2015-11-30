1#
#   MenuManager
#
#   Handles all writing and display functionality for the app.
#
#   - MenuManager.menus corresponds to GameManager.actions
#   - Use menu_manager.write() to display long lines of text, as it will automatically wrap and optionally center the message.
#
import tweepy, time, sys, json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
ckey = 'rlee33vXmHIlmR5tQljIX0ucD'
csecret = 'cUiIFESIXSSin9YJHYwLnVwnHpS64Ytj7csY9yFqshvAlkcaPg'
atoken = '2836017980-DxYDsgHqGMyRIq1yH3Uf3Ar63eYCFhqawJAWGOw'
asecret = 'SruNXYjh0BpY4GQhiflXaxbB2XUhrCMslBrmrH2ViULnu'
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)
auth = OAuthHandler(ckey, csecret)
class MenuManager:
    #
    #   Initializes the MenuManager with a reference to its parent GameManager.
    #
    #   To make a new menu, add it to self.menus. Choices will be displayed in the order they're listed here.
    #   The first part of the tuple is the display name. The 2nd part is the name of the function to be called in GameManager.
    #   
    #   e.g.
    #   'menu_name': [('Choice 1', 'choice_1_action'), ('Choice 2', 'choice_2_action')]
    #   This example expects GameManager.choice_1_action() and GameManager.choice_2_action() to be valid functions.
    #
    def __init__(self, game_manager):
        self.game_manager = game_manager

        self.menus = {
            'main_menu': [
                ('New Game',        'new_game'), 
                ('Continue',        'continue_game'), 
                ('Scoreboard',       'scoreboard'),
                ('Instructions',    'instructions'), 
                ('Quit',            'quit')],
            'scoreboard_menu': [
                ('View Scoreboard', 'reporting'),
                ('Download Scoreboard', 'reporting_save')
            ]
        }

    #
    #   Prints a pretty title screen graphic followed by the main menu.
    #
    def title_screen(self):
        # print """
        #      __               __             __
        #     /  )    _ _      (    '_ '_/_   /__)
        #    /(_/(//)(/(-()/) __)(//( /(/(-  / ( (//)
        #           _/                                """

        print """Thank you for playing Dungeon Sucide Run"""
        self.divider()
        self.menu('main_menu', True)

    #
    #   Prints a centered title and divider.
    #
    def title(self, title):
        print "\n" + title.center(60, ' ')
        self.divider()

    #
    #   Prints a divider line.
    #
    def divider(self):
        print "______________________________________________".center(60, ' ') + '\n'

    #
    #   Prints a line of text, wrapped to 60 columns and optionally centered.
    #
    def write(self, message, centered=False):
        message = self.wrap(message, 60)
        if centered:
            print message.center(60, ' ')
        else:
            print message

    #
    #   Wraps text for display.
    #   Source: http://code.activestate.com/recipes/148061-one-liner-word-wrap-function/
    #
    def wrap(self, text, width):
        return reduce(lambda line, word, width=width: '%s%s%s' %
              (line,
               ' \n'[(len(line)-line.rfind('\n')-1
                     + len(word.split('\n',1)[0]
                          ) >= width)],
               word),
              text.split(' ')
             )

    #
    #   Prints out a numbered list and a prompt from a named menu.
    #   Menu must be defined in MenuManager's menus property.
    #
    def menu(self, menu, centered=False):
        m = self.menus[menu]
        menu_items = []
        for item in m:
            menu_items.append(item[0])
        self.list(menu_items, centered)
        self.prompt(menu)

    #
    #   Prints out a numbered list.
    #
    def list(self, list, centered=False):
        for i in range(len(list)):
            s = str(i + 1) + '. ' + list[i]
            if centered:
                print s.center(60, ' ')
            else:
                print s

    #
    #   Prompts the user to enter a number. If the input is invalid, the prompt happens again.
    #
    def prompt(self, menu):
        while True:        
            self.write("\nEnter the number that corresponds with your choice.")
            choice = raw_input()
            try:
                int(choice)
                self.menus[menu][int(choice) - 1]
                break
            except:
                pass

        choice = int(choice) - 1
        self.handle_choice(menu, choice)

    #
    #   Prompts the user to press enter to continue. Call this when you have text the user needs to read.
    #
    def continue_prompt(self):
        self.write("\nPress enter to continue ...\n")
        raw_input()

    #
    #   Takes user input from a prompt() and calls the appropriate action in the GameManager.
    #   The action is taken from the actions[menu][choice_name] string of the game manager.
    #   e.g. "main_menu" -> "Instructions" will call GameManager.show_instructions() 
    #
    def handle_choice(self, menu, choice):
        action_name = self.menus[menu][choice][1]
        action = getattr(self.game_manager, action_name)
        action()