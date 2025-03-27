# Python program to draw random cards from a deck

import itertools
import random

def create_deck() -> list:
    """Create a standard deck of 52 playing cards."""
    ranks = {
        1: "Ace", 11: "Jack", 12: "Queen", 13: "King"
    }
    suits = ['Spade', 'Heart', 'Diamond', 'Club']
    return [(ranks.get(rank, rank), suit) for rank, suit in itertools.product(range(1, 14), suits)]

def draw_cards(deck: list, num_cards: int) -> list:
    """Draw a specified number of cards from the deck."""
    if num_cards > len(deck):
        raise ValueError("Cannot draw more cards than are available in the deck.")
    random.shuffle(deck)
    return deck[:num_cards]

def main() -> None:
    """Main function to execute the card drawing program."""
    try:
        deck = create_deck()
        num_cards_to_draw = 5  # You can make this configurable if needed
        drawn_cards = draw_cards(deck, num_cards_to_draw)
        print("You got:")
        for rank, suit in drawn_cards:
            print(f"{rank} of {suit}")
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
