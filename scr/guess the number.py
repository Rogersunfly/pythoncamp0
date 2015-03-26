import simplegui
import math
import random

secert_the_number = 100
guess_the_number = 0

def new_game():
    if guess < secert_the_number:
      print "lower!"
    elif guess > secert_the_number:
      print "higer!"
    elif guess == secert_the_number:
      print " correct,you are a gooooooood booy!"
    else:
      print " you are out of control, MYM!"
    
def range100():
    global secert_the_number
    secert_the_number = random.randint(0, 100)
    number_of_choice = 100
    input_guess()
    
def range1000():
    global secert_the_number
    secert_the_number = random.randint(0, 1000)
    number_of_choice = 1000
    input_guess()
     
def input_guess():
    global guess
    global guess_the_number
    number = math.ceil(math.log(2, number_of_choice)
    guess_the_number = guess_the_number + 1
    if guess_the_number <= number:
      print " Guess is " guess
      new_game()
    else:
      print "you are lose!"
       
f = simplegui.create_frame("guess the number", 200, 200)
                      
frame.add_button("range=[0, 100)", range100, 200)
frame.add_button("range=[0, 1000)", range1000, 200)
frame.add_input("guess the number", input_guess, 200)

new_game()
