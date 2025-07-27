from deckOCards import deck, card

class pokerGame():
    def __init__(self, machineModel):
        self.cardDeck = deck() #Deck of cards, will call the deal function for each player and board
        #---> as well as 2 burns, Total of 9 dealt cards
        self.board = [] #An array of 5 "card"s (will be populated as we go)
        self.playerHoleCards = [[],[]] #0: Machine, 1: Player, each arr is len 2
        self.actions = [[],[],[],[]] #Actions: Preflop, flop, turn, river
        self.curBettingRound = 0 #0: preflop, 1:flop, 2:turn, 3:river
        self.smallBlind = 0 #Again 0: machine, 1: player. Infer BB position with the SB pos
        self.stacks = [200, 200] #BB is 2, SB is 1, so it's a 1/2 game 200 dollar buy in
        #--> Each players starts with 100 BB behind
        self.machine = machineModel

    def dealHoleCards(self):
        for player in range(2): #bc heads up
            for num_card in range(2): #bc it's holdem not omaha
                self.playerHoleCards[player][num_card] = self.cardDeck.dealCard()

    def playHand(self):
        self.dealHoleCards()