from random import shuffle
from tkinter import *

#classes
class card:
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
        

#GUI
root = Tk()
root.title = "Warlatro"
