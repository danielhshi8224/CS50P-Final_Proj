 # LEITNER SYSTEM FLASHCARDS
    #### Video Demo: https://youtu.be/so6tRTY0au8
    #### Description: This is a flashcard program based on the Leitner system for spaced repetition. Every time you answer a question correctly, it will move up into the next deck, and vice versa if you answer a question incorrectly. It's up to you how often you study each deck, and it also depends on how far away your test date is. For example, you might study deck 1 every day, deck 2 every other day, and deck 3 once a week if you have a test coming up in a month. However, the Leitner system is most effective over long periods of time, so that your pool of knowledge can grow methodically.This program allows you to add, remove, and move cards in existing decks, create new decks, view their contents, and of course study your flashcards. Once you're done studying, 'sq' will save your cards so they can be loaded next time you open the program--just make sure to keep the program file and the deck files in the same folder. Saving can also be done without closing the program, using the ‘s’ command. You can even edit the text files directly to add or remove cards, and reload the program to study your edited decks.
    The main project file, project.py, contains all of the functions involved in the program. Project.py contains a class with three methods, nine regular functions, and a main function. The class “Deck” was what started the program off for me, as I really wanted to make a project that would allow me to implement object-oriented programming in some way. The methods inside the Deck class deal with the majority of the program’s interactions with file I/O, a choice I made mainly to make my main() function less bulky. Regarding the use of file I/O, my program was originally going to go without it, and initialize new empty decks of cards every time it ran, but I changed my mind, realizing that such a program would be effectively useless, as the point of any flashcard app is to be able to come back to the same decks time after time to study them. Therefore, I had to find a way to allow the user to save their decks as text files, and be able to load them again. I was easily able to implement functions using the with open and basic file reading and writing, but I began running into many errors–the deck files would save to the wrong directory, and I still didn’t know how to get my program to search the program’s directory for text files to import as decks. This led me to learn more about the built-in python module os, which allowed me to ensure that the program would read from and write to the same directory as project.py every time, without creating redundant files. After a suggestion from a friend, I also implemented a function that would check if the user was a new user or not, and either create new decks or search for saved decks accordingly. Near the end of development, I decided to change my main function to use match/case instead of if/else, as I wanted users to be able to type commands as letters or full words, and match/case better served such a purpose.

