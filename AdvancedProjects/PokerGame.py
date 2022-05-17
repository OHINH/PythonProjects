import numpy as np

colors = ["Spade", "Heart", "Diamond", "Club"]
heads = ["Ace", "King", "Queen", "Jack"]
cards_array = []
for i in list(colors):
    for j in range(2, 11):
        cards_array.append(str(j) + " of " + i)
    for k in list(heads):
        cards_array.append(k + " of " + i)

print("Welcome to the Python Poker Texas Hold'em Game!")
# N = int(input("How Many players are there?" + "\n" + "--> "))
N = 8
while N <= 2 or N > 10:
    N = int(input("Poker is for 3-9 players optimally! How Many players are there?" + "\n" +
                  "--> "))
print(str(N) + " players it is! Let's Begin!")

# setting up # of chips

# tenChips = int(input("How many Chips of 10$? \n --> "))
# twentyChips = int(input("How many Chips of 20$? \n --> "))
# fiftyChips = int(input("How many Chips of 50$? \n --> "))
# hundredChips = int(input("How many Chips of 100$? \n --> "))
# chips = tenChips * 10 + twentyChips * 20 + fiftyChips * 50 + hundredChips * 100
chips = 1000


# setting up the player class

class Player:
    def __init__(self, name, numbofchips, role, holdingcards):
        self.name = name
        self.numbofchips = numbofchips
        self.role = role
        self.holdingcards = holdingcards

    def getname(self):
        print("The name is " + self.name + ".")

    def getnumchips(self):
        print("You currently have " + self.numbofchips + " chips.")

    def getrole(self):
        print("your current role is " + self.role)


p = []

for i in range(1, N + 1):
    p.append(Player(input("What is the " + str(i) + "-th player's name? "), chips, role=None, holdingcards=None))


print("\n recap: \n ")
for i in range(0, N):
    print(p[i].name + " has " + str(p[i].numbofchips) + "$")

print("\n" + p[0].name + " will be the initial dealer \n" + p[1].name + " is the small blind \n" + p[2].name + " is "
                                                                                                               "the "
                                                                                                               "big "
                                                                                                               "blind")
p[0].role = "dealer"
p[1].role = "small blind"
p[1].numbofchips -= 10
p[2].role = "big blind"
p[2].numbofchips -= 20

print("The dealer will now deal the cards!")

for i in range(0, N):
    a = np.random.choice(cards_array)
    b = np.random.choice(cards_array)
    if a == b:
        continue
    else:
        p[i].holdingcards = [np.random.choice(cards_array), np.random.choice(cards_array)]
    print(p[i].name + " receives " + p[i].holdingcards[0] + " and " + p[i].holdingcards[1])


"""
2nd step: set the dealer
3rd step: set the small and big blinds
4th step: distribute the cards
5th step: small blind plays: call, raise or fold
6th step: big blind plays
...
7th step: the dealer burns one card (discard one card, face down)
8th step: the flop: 3 face up cards
2nd betting round: small blind plays, check, call, raise or fold
...
9th step: burning, +1 card to the board (the turn)
3rd round = 2nd round...
10th step = 9th step (the river)
4th round = 3rd round
11th step: showdown
12th: winners?

test
"""
