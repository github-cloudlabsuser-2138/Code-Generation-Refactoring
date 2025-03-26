# Python program to draw five random cards from a deck

import itertools
import random

# Create a deck of cards
deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))

# Shuffle the cards
random.shuffle(deck)

# Draw five cards
print("You got:")
for i in range(5):
    print(f"{deck[i][0]} of {deck[i][1]}")
