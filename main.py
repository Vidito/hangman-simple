import random
print("Let's play hangman!")
print()
print("So what's your first guess?")

words = ['water', 'white', 'happy']
random_word = random.choice(words)
guesses = ''

lives = len(random_word)

while lives > 0:         
    guess = input("guess a character:")                    
    if guess not in random_word:  
        lives -= 1
        print()        
        print("Wrong Guess")    
 
        print("You have", + lives, 'more guesses')  
        if lives == 0:              
            print ("You Lose")

    guesses += guess 
    failed = 0                
    for char in random_word:      

        if char in guesses:    
          print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1    
    if failed == 0:        
        print("\nYou won")
        break              

    print()
    print()

