#RPS.py
#Name:Riley Mayfield
#Date:2/3
#Assignment:Lab 2
#Purpose: Make a rock paper scissors game
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  play = "yes"
  hands = ["R","P","S"]
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.

  play = input("shall we play a game?(yes/no): ")
  while play != "yes" and play != "no":
    print("I don't understand")
    play = input("shall we play a game?(yes/no): ")


  while play == "yes":
    compPlay = random.choice(hands)
    #print(compPlay)
    mePlay = input("I made my choice, what's yours?(R/P/S): ")
    print("I chose: ",compPlay,"\nYou chose: ",mePlay)

    if compPlay == "R":
      if mePlay == "R":
        ties = ties + 1
        print("tie")
      elif mePlay == "P":
        wins = wins + 1
        print("you win")
      elif mePlay == "S":
        losses = losses + 1
        print("you lose")
      else:
        print("Not a valid hand")

    if compPlay == "P":
      if mePlay == "P":
        ties = ties + 1
        print("tie")
      elif mePlay == "S":
        wins = wins + 1
        print("you win")
      elif mePlay == "R":
        losses = losses + 1
        print("you lose")
      else:
        print("Not a valid hand")

    if compPlay == "S":
      if mePlay == "S":
        ties = ties + 1
        print("tie")
      elif mePlay == "R":
        wins = wins + 1
        print("you win")
      elif mePlay == "P":
        losses = losses + 1
        print("you lose")
      else:
        print("Not a valid hand")
    
    play = input("shall we play a game?(yes/no): ")
    while play != "yes" and play != "no":
      print("I don't understand")
      play = input("shall we play a game?(yes/no): ")
    

  
  #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.

  #In the end, print the stats
  print("Goodbye")
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
