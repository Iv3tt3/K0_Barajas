#Use dotenv library to import env variables and import os
from dotenv import load_dotenv
import os
import random

#Load env varibales from file .env
load_dotenv()


class Deck():
    def __init__(self):
        #Set suits and numbers form .env
        self.suits = os.getenv('SUITS').split(',')
        self.numbers = os.getenv('NUMBERS').split(',')
        #Create an empty list to store all deck cards
        self.playing_cards = [] 
        #Call the method to fill the list 
        self.get_playing_cards()

    def get_playing_cards(self):
        #Generate playing cards by addinng all suits of each numbers
        for suit in self.suits:
            for number in self.numbers:
                card = number + suit
                self.playing_cards.append(card)

    def shuffle(self):
        #Shuffle the playing cards using random library and an index to swap the cards 
        for i in range(len(self.playing_cards)):
            p = random.randrange(0,len(self.playing_cards),1)
            self.playing_cards[i], self.playing_cards[p] = self.playing_cards[p], self.playing_cards[i] 