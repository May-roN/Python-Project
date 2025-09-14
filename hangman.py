import random

choices = ["banana","orange","grapes","apple","watermelon","mango"]
word = random.choice(choices)
word = list(word)
print (word)
guessLimit = 0
guesses = 0
guessLimit = len(word) + 2
print (guessLimit)
    
for x in range(guessLimit):
	letterGuess = input("Guess one letter: ")
	print(letterGuess)
	print("guess counter: ", guesses)
	guesses += 1
        #print(letterGuess)        
	#print("guess counter:", guesses)
	#guesses += 1
	
'''
while guessLimit >= guesses:
    for letter in word:
        guesses += 1
        letterGuess = input ("Guess one letter: ")
        print (letter)

        if letterGuess == letter:
            print (letterGuess)
            print("correct")
            
            
        elif letterGuess != letter:
            print("Wrong letter, try again!")
          
        print ("guess counter:", guesses)
'''
