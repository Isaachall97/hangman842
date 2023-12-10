import random as rnd
#initialising variables
word_list = ["mango", "pineapple", "apple", "pear", "kiwi"]
word = []
#user guesses letter
guess = input("please input a letter: ")
# if statement to check whether the number of letters entered is correct, and whether the input is alphabetical or incorrect
if guess.isalpha() == True and len(guess) == 1: 
    print('Good guess!')
else:
    print("Oops! That's not a valid input")
#function to get a random fruit from the list of fruits
def random_choice(word_list):
    word = rnd.choice(word_list)
    return word
print(type(word_list))
print(word_list)
print(random_choice(word_list))