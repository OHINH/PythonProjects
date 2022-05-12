############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_random_card():
    return random.choice(cards)

print("Welcome to the Blackjack game!")
Mycards = (card1 = draw_random_card(), card2 = draw_random_card())
DealerCards = [cardDealer1 = draw_random_card(), cardDealer2 = draw_random_card()]

print(f"Your starting deck is {card1} and {card2}; the Dealer's first card is {cardDealer1}")

MyPoints = card1 + card2
DealerPoints = cardDealer1 + cardDealer2
Draw_More_Card = input("Do you want to draw another card? 'y' for Yes and 'n' for No")

if Draw_More_Card == "y":
    print(f"Your 3rd card is {card3}")
    card3 = draw_random_card()
    Mycards.append(card3)
    MyPoints += card3

if DealerPoints < 17:
    cardDealer3 = draw_random_card()
    DealerCards.append(cardDealer3)
    DealerPoints += cardDealer3


if MyPoints > 21 and card1 != 11 and card2 != 11 and card3 != 11:
    print("You have more than 21, You Lose...")
elif MyPoints > 21 and (card1 != 11 or card2 != 11 or card3 != 11):
    MyPoints -= 10 * (11 in Mycards)
else:
    print("The Dealer's cards are {cardDealer1}, {cardDealer2} and {cardDealer3}, which is {DealerPoints}... You Lose...")




if card1 + card2 + card3 < cardDealer1 + cardDealer2 + cardDealer3:
    
else:
    if card1 == 11:

