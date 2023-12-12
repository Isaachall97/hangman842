#importing random module to generate random word from list
import random as rnd
#Defining class 'Hangman' which will take in a letter and check whether it is within a random word selected from a predetermined list. 
class Hangman:
    #__init__ class- defining the random word choice from list, num_lives is set to 5. 
    def __init__(self, num_lives = 5, word_list= []):
        #The word to be guessed, picked randomly from word_list
        self.word = rnd.choice(word_list)
        #The number of lives the player has at the start of the game
        self.num_lives = num_lives
        #list - A list of the letters of the word, with _ for each letter not yet guessed.
        # For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_'].
        # If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
        self.word_guessed = ['_'] * len(self.word)
        #int - The number of UNIQUE letters in the word that have not been guessed yet
        self.num_letters = len(set(self.word))
        #list - A list of the guesses that have already been tried. Set this to an empty list initially
        self.list_of_guesses = []
#if loop to check whether the letter guessed is in the word. If it is, it adds the letter to the list of correct letters at the index of the word. 
#if it isn't, the user's lives go down by 1. 
    def check_guess(self, guess):
        if guess in self.word: 
             print(f"Good guess! {guess} is in the word.")
             list_word = list(self.word)
             for letter in list_word: 
                 if guess == letter:
                    self.word_guessed[list_word.index(letter)] = guess
                 else:
                     continue
             self.num_letters = self.num_letters - 1
        else:
             self.num_lives = self.num_lives - 1
             print(f"Sorry, {guess} is not in the word. Please try again. you have {self.num_lives} lives left.")
    #function defining whether the user input is valid, and checking if they have already guessed the character in question. 
    def ask_for_input(self):
        self.list_of_guesses = []
        while True:
            self.guess = input("New letter: ")
            guess = self.guess.lower()
            if  guess.isalpha() == False or len(guess) > 1:
                print("Invalid letter. Please, enter a single alphabetical character.")   
            elif self.guess in self.list_of_guesses:
                print("You already guessed that! Please input a new letter.")   
                print(f"letters already guessed: {self.list_of_guesses}")
            else:
               self.check_guess(guess)
               self.list_of_guesses.append(guess)
            print(self.word_guessed)
            
            
               
               
   
joue = Hangman(word_list = ["apple", "banana", "orange", "pineapple"])
joue.ask_for_input()



            

   
        


    


        
