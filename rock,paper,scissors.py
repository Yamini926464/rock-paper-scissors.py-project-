import random
print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      "Rock vs Paper -> Paper Wins\n"
      "Rock vs Scissors -> Rock Wins\n"
      "Paper vs Scissors -> Scissors Win\n")

while True:
    print("Enter your ee \n 1 - Rock\n 2 - Paper\n 3 - Scissors\n")
    choice=int(input("Enter your choice:\n"))
    while choice > 3 or choice < 1:
        choice = int(input("Enter a valid choice please"))
    if choice == 1:
        choice_name='Rock'
    elif choice == 2:
        choice_name='Paper'
    else:
        choice_name='Scissors'
    print('User choice is \n' ,choice_name)
    print('Now its Computers Turn ......')
    comp_choice=random.randint(1,3)
    while comp_choice == choice:
        comp_choice=random.randint(1,3)
    if comp_choice ==1:
        comp_choice_name='Rock'
    elif comp_choice==2:
        comp_choice_name='Paper'
    else:
        comp_choice_name='Scissors'
    print("computer choice is \n",comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)
    if choice ==comp_choice:
        print('Its a Draw',end="")
        result="DRAW"
    if (choice==1 and comp_choice==2):
        print('Paper wins =>',end="")
        result='Paper'
    elif(choice==2 and comp_choice==1):
        print('paper wins =>', end="")
        result='Paper'
    if (choice==1 and comp_choice==3):
        print('Rock wins =>',end="")
        result='Rock'
    elif (choice==3 and comp_choice==1):
        print('Rock wins =>',end="")
        result='Rock'
    if (choice ==2 and comp_choice==3):
        print('Scissors wins =>',end="")
        result='Scissors'
    elif (choice==3 and comp_choice==2):
        print('Scissors wins =>',end="")
        result='Rock'
    if result=='DRAW':
        print("<== Its a tie ==>")
    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== computer wins ==>")
    print("Do you want to play again?(Y/N)")
    ans=input().lower()
    if ans=='n':
        break
print("Thanks for playing")
