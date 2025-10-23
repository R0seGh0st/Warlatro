from random import shuffle
from tkinter import *

#classes
class Card:
    suit = ["Hearts", "Dimonds", "Spades", "Clubs"]
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, s, r):
        self.suit = s
        self.rank = r

    def __repr__(self):
        return f"{self.rank} of {self.suit}"
    
    def __eq__(self, card):
        if (self.rank == card.rank):
            return True
        else:
            return False
        
    def __lt__ (self, card):
        if (self.rank < card.rank) :
            return True
        else:
            return False
        
    def __gt__ (self, card):
        if (self.rank > card.rank) :
            return True
        else:
            return False
        
class Deck:
    def __init__(self):
        self.cards = []
        for i in range (0, 4):
            for j in range (0, 13):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rmCard (self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        #active card
        self.card = None
        #what cards are in the collection
        self.collection = []
        #how many 'bosses' have been defeated
        self.wins = 0
        
class Game:
    def __init__ (self):
        #creates a player object, and a computer object, as well as the deck
        name = input("what is your name?")
        self.deck = Deck()
        self.player = Player(name)
        self.computer = Player("Computer")
    
    def win (self):
        self.player.wins += 1
        self.computer = Player ("Computer {}").format(self.player.wins + 1)
    
    def draw (self, c1, c2):
        p = "You drew {} and {} drew {}".format(c1, self.computer.name, c2)
        print (p)

    def playGame (self):
        # the way to do this is split the deck like in irl war, then collections would be 26
        # and loop from there until someone loses all there cards
        # just make a deal function to do the 26 split in a loop with the created deck, then deck is ignored during play
        cards = self.deck.cards
        print("Begin War")
        self.player.card = self.deck.rmCard()
        self.player.collection.append(self.player.card)
        self.computer.card = self.deck.rmCard()
        self.computer.collection.append(self.computer.card)            
        
        while (len(self.player.collection) >= 1 and len(self.computer.collection) >= 1):
            m = "Press 'q' to quit. Any other key to play: "
            response = input(m)
            if response == 'q':
                break
            self.draw(self.player.card, self.computer.card)
            if self.player.card > self.computer.card:
                self.player.collection.append(self.computer.card)
                self.computer.collection.remove(self.computer.card)
            elif self.player.card < self.computer.card:
                self.computer.collection.append(self.player.card)
                self.player.collection.remove(self.player.card)
