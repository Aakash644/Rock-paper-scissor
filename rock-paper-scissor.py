import random
rock = """ 
    Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = '''
     Paper
    ________
---'    ____)____
           ______)
          _______)
         _______)
---.__________) '''
scissor = ''' 
     Scissor
    _______
---'  ____)____
          ______)
       __________)
      (____)
---.__(___)
 '''
while (1):
    choice = int(
        input('''***-----------------***\nWhat is your choice?\n1.Rock\n2.Paper\n3.Scissor\n4.Exit\n'''))

    def getimg(input):
        if (input == 1):
            print(rock)

        elif (input == 2):
            print(paper)

        elif (input == 3):
            print(scissor)

    getimg(choice)
    print("Computer chooses:")
    rand = random.randint(1, 3)
    getimg(rand)
    if (choice == 1):
        if (rand == 3):
            print("You win")
        elif (rand == 2):
            print("You lose")
        else:
            print("Tie")
    elif (choice == 2):
        if (rand == 3):
            print("You lose")
        elif (rand == 2):
            print("Tie")
        else:
            print("You win")
    elif (choice == 3):
        if (rand == 3):
            print("Tie")
        elif (rand == 2):
            print("You win")
        else:
            print("You lose")
    elif (choice == 4):
        exit(0)
    else:
        print("Invalid input")
