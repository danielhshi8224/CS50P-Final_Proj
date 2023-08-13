import sys


class Deck:
    def __init__(self, name, cards=None):
        self.name = name
        self.cards =cards if cards is not None else {}

decks = [Deck("Deck 1"), Deck("Deck 2"), Deck("Deck 3")]# 3 decks by default
def add_deck(name):#Add a deck to the default 3 decks. Use this if you want to add another time interval
    decks.append(Deck(name))
    print(f"Current decks: {len(decks)}")


def add_flashcard(decks_list, deck_name, front, back):# Add a flashcard to any deck
    deck_exists=False
    for deck in decks_list:
        if deck.name==deck_name:
            deck_exists=True
            deck.cards[front]=back
            print(f"New card {front}: {back} added to {deck_name}")
            print(f"{deck_name} Contents:")
            for card in deck.cards:

                    print(f"{card} : {deck.cards[card]}")
            break
    if not deck_exists:
        print(f"Deck '{deck_name} not found")


def delete_flashcard(decks_list, deck_name, front):#Remove a flashcard from any deck
    deck_exists=False
    for deck in decks_list:
        if deck.name==deck_name:
             deck_exists=True
             if front in deck.cards:
                del deck.cards[front]
                print("Card removed.")
                for card in deck.cards:
                    print(f"{card} : {deck.cards[card]}")
                break
             else:
                 print(f'Card "{front}" not found in {deck_name}.')
    if not deck_exists:
        print(f"Deck '{deck_name} not found")
def view_deck_contents(decks_list, deck_name): #View the contents of any deck
    deck_exists=False
    for deck in decks_list:
        if deck.name==deck_name:
            deck_exists=True
            for card in deck.cards:
                print(f"{card} : {deck.cards[card]}")
            break
    if not deck_exists:
        print(f"Deck '{deck_name}' not found")

'''
def study_deck(decks_list, deck_name):
    for deck in decks_list:
        if deck.name==deck_name:
            for card in deck.cards:
                ans=input(f"{card}:").strip()
                if ans==deck.cards[card]:
                    if decks_list.index(deck)<len(decks_list):
                        next_deck=decks_list[decks_list.index(deck)+1].cards
                        next_deck.update({card:deck.cards.pop(card)})
                        print(f"Correct! Card moved up to {decks_list[decks_list.index(deck)+1].name}!")
                    else:
                        print("Correct! You are in the highest deck.")
                else:
                    if decks_list.index(deck)> 0:
                        prev_deck=decks_list[decks_list.index(deck)-1]
                        prev_deck.update({card:deck.cards.pop(card)})
                        print(f"Incorrect... Card moved down to {decks_list[decks_list.index(deck)+1].name}")
                    else:
                        print("Incorrect...")


        else:
            print(f"Deck '{deck_name} not found")

'''
def move_card(decks_list,giver, receiver, front):
    deck_exists=False
    for recer in decks_list:
        if recer ==deck.name:
        
            for deck in decks_list:
                    if giver==deck.name:
                        deck_exists=True
                        recer.cards.update(front, deck.cards.pop(front))
        if not deck_exists:
                             print(f"Deck {receiver} not found")        
                    if not deck_exists:
                        print(f"Deck {giver} not found")




'''
def study_deck(decks_list, deck_name):#Study a deck
    for deck in decks_list:
        if deck.name == deck_name:
            cards_to_remove = []  # Collect cards to be removed from the deck
            cards_to_add = {}     # Collect cards to be added to another deck

            for card in deck.cards:
                ans = input(f"{card}: ").strip()
                if ans == deck.cards[card]:
                    if decks_list.index(deck) < len(decks_list) - 1:
                        next_deck = decks_list[decks_list.index(deck) + 1]
                        cards_to_add[card] = deck.cards[card]
                        print(f"Correct! Card moved up to {next_deck.name}!")
                    else:
                        print("Correct! You are in the highest deck.")
                else:
                    if decks_list.index(deck) > 0:
                        prev_deck = decks_list[decks_list.index(deck) - 1]
                        cards_to_add[card] = deck.cards[card]
                        print(f"Incorrect... Card moved down to {prev_deck.name}")
                    else:
                        print("Incorrect...")
                    cards_to_remove.append(card)

            for card in cards_to_remove:
                deck.cards.pop(card)

            for card, value in cards_to_add.items():
                if decks_list.index(deck) < len(decks_list) - 1:
                    next_deck = decks_list[decks_list.index(deck) + 1]
                    next_deck.cards[card] = value
                else:
                    print("Warning: Card couldn't be moved up further.")
            break
        else:
            print(f"Deck '{deck_name}' not found")
'''
def study_deck(decks_list, deck_name):  # Study a deck
    current_deck_index = None

    for index, deck in enumerate(decks_list):
        if deck.name == deck_name:
            current_deck_index = index
            break

    if current_deck_index is None:
        print(f"Deck '{deck_name}' not found")
        return

    current_deck = decks_list[current_deck_index]
    next_deck_index = current_deck_index + 1 if current_deck_index < len(decks_list) - 1 else None
    prev_deck_index = current_deck_index - 1 if current_deck_index > 0 else None

    cards_to_remove = []
    cards_to_add = {}

    for card in current_deck.cards:
        ans = input(f"{card}: ").strip()
        if ans == current_deck.cards[card]:
            if next_deck_index is not None:
                next_deck = decks_list[next_deck_index]
                cards_to_add[card] = current_deck.cards[card]
                cards_to_remove.append(card)
                print(f"Correct! Card moved up to {next_deck.name}!")
            else:
                print("Correct! You are in the highest deck.")
        else:
            if prev_deck_index is not None:
                prev_deck = decks_list[prev_deck_index]
                cards_to_add[card] = current_deck.cards[card]
                cards_to_remove.append(card)
                print(f"Incorrect... Card moved down to {prev_deck.name}")
            else:
                print("Incorrect...")

    for card in cards_to_remove:
        del current_deck.cards[card]

    for card, value in cards_to_add.items():
        if next_deck_index is not None:
            next_deck = decks_list[next_deck_index]
            next_deck.cards[card] = value
        else:
            print("Warning: Card couldn't be moved up further.")


def main():
    while True:
        choice = input(
            "\ns: Study\na: Add to a deck\nd: Delete card from a deck\nc: Create a new deck\nv: View the contents of a deck\nm: Move a card to a different deck\nWhat would you like to do?"
        ).lower().strip()
        if choice=="a":
            deck_name=input("Which deck are you adding to? ")
            front=input("Front of card: ")
            back=input("Back of card: ")
            add_flashcard(decks,deck_name, front, back)
        elif choice=="d":
            deck_name=input("Which deck are you removing from? ")
            front=input("Front of card: ")
            delete_flashcard(decks, deck_name, front)

        elif choice=="c":
            new_deck_name=input("Name your new deck: ")
            add_deck(new_deck_name)
        elif choice=="v":
            deck_name=input("Which deck would you like to view? ")
            view_deck_contents(decks, deck_name)
        elif choice=="s":
            deck_name=input("Which deck would you like to study? ")
            study_deck(decks, deck_name)
        elif choice=="m":
            giver_deck=input("Move a card from which deck? ")
            receiver_deck=input("Move to which deck? ")
            front=input("Front of card: ")
            move_card(decks, giver_deck, receiver_deck, front)
        


if __name__ == "__main__":
    main()
