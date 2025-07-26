import random

class suit:
	def __innit__(self,sym):
		self.type = sym
	
	def getSym(self):
		if (self.sym == 0):
			return "♠"
		if (self.sym == 1):
			return "♥"
		if (self.sym == 2):
			return "♣"
		return "♦"
 
	def __str__(self):
		title = ""
		if (self.sym == 0):
			title = "Spades"
		if (self.sym == 1):
			title = "Hearts "
		if (self.sym == 2):
			title = "Clubs "
		if (self.sym == 3):
			title= "Diamonds "
		return title + self.getSym()

class card:
	def __init__(self, val, suit):
		self.val = val
		self.suit = suit
		return

	def getVal(self):
		return self.val
 
	def __str__(self):
		return ""+self.val+" of "+self.suit

	def setVal(self,val):
		self.val = val

class deckOcards:
	def __init__(self):
		self.deck = []
		self.fill()

	def fill(self):
		self.deck = []
  
		for j in range(4):
			for i in range(13):
				self.deck.append(card(j,i))
    
	def print(self):
		for i in self.deck:
			print(i)
   
	def shuffle(self):
		random.shuffle(self.deck)
	
	def dealCard(self):
		card = self.deck(0)
		self.deck.pop(0);
		return card