import random #import random function

choices = ["banana","orange","grapes","apple","watermelon","mango"] 
guessLimit = 0
guesses = 0


def choose_word(fruits): # function to randomly choose a fruit
    word = random.choice(fruits)
    print (fruits)
    
'''
while guessLimit >= guesses:
    for letter in word:
        letterGuess = input ("Guess one letter: ")
        print (letter)

        if letterGuess == letter:
            print (letterGuess)
            print("correct")
            guesses += 1
            
        elif letterGuess != letter:
            print("Wrong letter, try again!")
            guesses += 1

        print ("guess counter:", guesses)
'''
