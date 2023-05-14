import random, sys

wins, losses, ties = 0,0,0

#  0->rock   1->paper   2->scissor

#approach 1
choice = {'s': 0,
            'p': 1,
            'r': 2} 

while True: #user's input
    print ("Choose: (r)ock, (p)aper, (s)cissor or (q)uit")
    user_choice = input()
    if user_choice=='q':
        break
    elif user_choice=='r' or user_choice=='p' or user_choice=='s':
        computer_choice = random.choice(['r', 'p', 's'])
        print ('Computer\'s choice', computer_choice )
        if user_choice==computer_choice:
            print("It's a tie")
            ties += 1
        elif choice[user_choice]>choice[computer_choice]:
            print("You lose")
            losses += 1
        elif choice[user_choice]<choice[computer_choice]:
            print("You win!")
            wins +=1
    else:
        print ("please enter either of the following: r  p  s  q  ") 
print("Game over", "%s Wins, %s Losses %s Ties" %(wins, losses, ties))


#approach 2
#function to generate computer's choice
def computer_choice():
        computer=''
        number = random.randint(1,3)
        if number==1:
            computer = 'r'
            
        elif number==2:
            computer = 'p'
        else:
            computer = 's'
        return computer

def game():    
    while True: #user's input
        print ("Choose: (r)ock, (p)aper, (s)cissor or (q)uit")
        user_choice = input()
        if user_choice=='q':
            break
        elif user_choice=='r' or user_choice=='p' or user_choice=='s':
            computer =  computer_choice()
            print ("Computer's choice", computer)
            
            if user_choice==computer:
                print("It's a tie")
                ties += 1
            elif user_choice=='r' and computer=='s':
                print("You win!")
                wins += 1
            elif user_choice=='p' and computer=='r':
                print("You win!")
                wins +=1
            elif user_choice=='s' and computer=='p':
                print("You win!")
                wins += 1
            elif user_choice=='r' and computer=='p':
                print("You lose")
                losses += 1 
            elif user_choice=='p' and computer=='s':
                print("You lose")
                losses += 1        
            elif user_choice=='s' and computer=='r':
                print("You lose")
                losses += 1    
        else:
            print ("please enter either of the following: r  p  s  q  ") 

    print("Game over", "%s Wins, %s Losses %s Ties" %(wins, losses, ties))



