import sys #Used to quit the program after saving decks to text files


class Deck:
    def __init__(self, name, cards=None):
        self.name = name
        self.cards =cards if cards is not None else {}
    def save_to_file(self):
         
            with open(f"{self.name}.txt", "w") as deck_file:
                 for key, value in self.cards.items():
                    deck_file.write(f"{key}:{value}\n")
                 print(f"Deck '{self.name}' saved to file.")
    def initialize_deck_from_file(self):
        
            with open(f"{self.name}.txt", "r") as file:
                lines=file.readlines()
                for line in lines:
                    key, value=line.strip().split(":")
                    self.cards[key]=value



decks = [Deck("deck1"), Deck("deck2"), Deck("deck3")]# 3 decks by default
'''
def add_deck(name):#Add a deck to the default 3 decks. Use this if you want to add another time interval
    decks.append(Deck(name))
    print(f"Current decks: {len(decks)}")
'''

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
def move_card(decks_list, giver, receiver, front):
    giver_deck = None
    receiver_deck = None
    
    for deck in decks_list:
        if deck.name == giver:
            giver_deck = deck
        if deck.name == receiver:
            receiver_deck = deck
        if giver_deck and receiver_deck:
            break
    
    if not giver_deck:
        print(f"Deck {giver} not found")
    elif not receiver_deck:
        print(f"Deck {receiver} not found")
    else:
        card = giver_deck.cards.pop(front, None)
        if card is None:
            print(f"Card '{front}' not found in deck '{giver}'")
        else:
            receiver_deck.cards[front] = card
            print(f"Card '{front}' moved from '{giver}' to '{receiver}'")




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
    instructions="\nThis is a flashcard program based on the Leitner system for spaced repetition.\nEvery time you answer a question correctly, it will move up into the next deck, and vice versa if you answer a question incorrectly.\nIt's up to you how often you study each deck, and it also depends on how far away your test date is.\nFor example, you might study deck 1 every day, deck 2 every other day, and deck 3 once a week if you have a test coming up in a month.\nHowever, the Leitner system is most effective over long periods of time, so that your pool of knowledge can grow methodically.\n\nThis program allows you to add, remove, and move cards in existing decks, create new decks, view their contents, and of course study your flashcards.\nOnce you're done studying, 'sq' will save your cards so they can be loaded next time you open the program--just make sure to keep the program file and the deck files in the same folder.\nYou can even edit the text files directly to add or remove cards, and reload the program to study your edited decks."
    print(instructions)
    for deck in decks:
        deck.initialize_deck_from_file()
    while True:
        choice = input(
            "\ns: Study\na: Add to a deck\nd: Delete card from a deck\nv: View the contents of a deck\nm: Move a card to a different deck\nsq: Save decks to your computer and quit the program\nq: Quit without saving\nWhat would you like to do? "
        ).lower().strip()
        if choice=="a":
            deck_name=input("Which deck are you adding to? ").strip()
            front=input("Front of card: ").strip()
            back=input("Back of card: ").strip()
            if front=="":
                print("Card must have a front!")
            elif back=="":
                print("Card must have a back!")
            else:
                add_flashcard(decks,deck_name, front, back)
        elif choice=="d":
            deck_name=input("Which deck are you removing from? ").strip()
            front=input("Front of card: ")
            delete_flashcard(decks, deck_name, front)
        
        #elif choice=="c":
           # new_deck_name=input("Name your new deck: ").strip()
            #add_deck(new_deck_name)
        
        elif choice=="v":
            deck_name=input("Which deck would you like to view? ").strip()
            view_deck_contents(decks, deck_name)
        elif choice=="s":
            deck_name=input("Which deck would you like to study? ").strip()
            study_deck(decks, deck_name)
        elif choice=="m":
            giver_deck=input("Move a card from which deck? ").strip()
            receiver_deck=input("Move to which deck? ").strip()
            front=input("Front of card: ").strip()
            move_card(decks, giver_deck, receiver_deck, front)
        elif choice=="q":
            while True:
                    quit=input("Are you sure you want to quit without saving your decks?(y/n) ").strip().lower()
                    if quit=="y":
                        sys.exit("Decks not saved. See you next time!")
                    elif quit=="n":
                        break
            
        elif choice=="sq":
             for deck in decks:
                  deck.save_to_file()
             
             sys.exit("All decks saved. See you next time!")

        


if __name__ == "__main__":
    main()
