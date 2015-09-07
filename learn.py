
"""
Objective:
The game should keep asking for the input.
The game should tell the user to Guess higher or Guess lower depending on the input.
The game should tell the user the number of tries he did to get the correct answer
The code should be able to catch errors. 
"""
"""
Hints :
You need to define a variable as a counter 
You should have a while loop which should run infinitely . It should break only when the correct input is recieved.
The counter's value should increase by one , everytime an input is recieved.
use while True: to run a loop infinitely
To stop a while loop , there is a special keyword called "break"
"""

"""
Comments:
What is the difference between [from random import randint] and [import randint]
Why are you printing the hidden random number?
because after guessing the user should know that what was the number inside

"""

from random import randint

counter = 0
random_number = randint(0,20)


while counter < 100:
    counter +=1
    
    user_input = int(raw_input("Enter yout number here from 0-20: "))
    print random_number
    if  user_input== random_number:
        print "You guessed it right"
        break
    

    elif user_input > random_number:
        print "Your input is higher than the number generated"
    elif user_input < random_number:
        print "Your input is lower than the number generated"
        
    else:
        print "you did not enter a number"
print "The times you tried to guess is", counter