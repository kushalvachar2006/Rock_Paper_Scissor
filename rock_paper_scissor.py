import random

print("\t\t\t\t\tWelcome to ROCK_PAPER_SCISSOR Game")

def game():
    count=0
    count1=0
    n=int(input("Enter the number of matches you wish to play\n"))
    print("Enter....\n 1.Rock 🪨\n 2.Paper  📄 \n 3.Scissors ✂️\n")
    for i in range(0,n):
        choice=input()
        comp_choice=random.choice("123")
        while choice not in ["1","2","3"]:
            choice=input("Please enter the choice 1,2,3\n1.Rock\n2.Paper\n3.Scissors\n")
        if choice=="1" and comp_choice=="3" or choice=="2" and comp_choice=="1" or choice=="3" and comp_choice=="2":
            print(comp_choice)
            print("You win!!😊")
            count+=1
        if comp_choice=="1" and choice=="3" or comp_choice=="2" and choice=="1" or comp_choice=="3" and choice=="2":
            print(comp_choice)
            print("Python wins💻")
            count1+=1
        if choice==comp_choice:
            print(comp_choice)
            print("Tie game🙌")
    print("You have won",count," times out of",n," matches\n")
    print("Python has won",count1," times out of",n," matches\n")
    if(count>count1):
        print("YOU WIN THE MATCH\n")
    elif count==count1:
        print("DRAW MATCH")
    else:
        print("PYTHON WON THE MATCH\n")
    global yn
    yn=input("Enter 'Y' to continue the game or\nEnter 'N' to end the game\n")
game()

while yn=="y" or yn=='Y':
    game()
if(yn=="N" or yn=="n"):
    print("Thank you for playing with us🙏")

