import random

VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

class WOFPlayer:
    def __init__(self,name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
    def addMoney(self,amt):
        self.prizeMoney += amt
    def goBankrupt(self):
        self.prizeMoney = 0
    def addPrize(self,prize):
        self.prizes.append(prize)
    def __str__(self):
        return '{} (${})'.format(self.name,self.prizeMoney)

class WOFHumanPlayer(WOFPlayer):
    def getMove(self,category, obscuredPhrase, guessed):
        print('{} has ${}'.format(self.name,self.prizeMoney)+'\n')
        print(showBoard(category,obscuredPhrase,guessed)+'\n')
        return input("Guess a letter, phrase, or type 'exit' or 'pass':")

class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    def __init__(self,name,difficulty):
        WOFPlayer.__init__(self,name)
        self.difficulty = difficulty
    def smartCoinFlip(self):
        return random.randint(1,10)>self.difficulty
    def guessPossibleLetters(self,guessed):
        possibleLetters = self.SORTED_FREQUENCIES
        if self.prizeMoney < VOWEL_COST:
            possibleLetters = [letter for letter in possibleLetters if letter not in VOWELS]
        return [letter for letter in possibleLetters if letter not in guessed]
    def getMove(self,category, obscuredPhrase, guessed):
        possibleLetters = self.guessPossibleLetters(guessed)
        if possibleLetters == []:
            return 'pass'
        elif self.smartCoinFlip():
            return possibleLetters[-1]
        else:
            return random.choice(possibleLetters)

# Returns a string representing the current state of the game
def showBoard(category, obscuredPhrase, guessed):
    return """
Category: {}
Phrase:   {}
Guessed:  {}""".format(category, obscuredPhrase, ', '.join(sorted(guessed)))