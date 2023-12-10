import random as rnd
#list of words for computer to pick at random
word_list = ["mango", "pineapple", "apple", "pear", "kiwi"]
#word is a string with a randomly chosen word from word_list
word = rnd.choice(word_list)
guess = input("input a letter: ")
#function to convert the input into lower case, and check whether it is in the alphabet with length of 1. 
# if not, the input loop will repeat.
def ask_for_input(guess):   
  guess = guess.lower()
  while True:
    if guess.isalpha() == True and len(guess) == 1:
      break
    else:
      print("Invalid letter. Please, enter a single alphabetical character.") 
      guess = input("New letter: ")
      guess = guess.lower() 
  check_guess(guess)    
#if loop to check whether the letter guessed is in the word.
def check_guess(guess):
  if guess in word: 
    print(f"Good guess! {guess} is in the word.")
  else: 
    print(f"Sorry, {guess} is not in the word. Please try again.")
  
        
ask_for_input(guess)


