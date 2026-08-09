import random 

num = random.randint(1,25)
print(num)
print("\n1. Start The Game .. ")
print("2. Quit ...")
choice = int(input("\nEnter Your Choice : "))

while True :
    if choice == 1 :

        g = int(input("Enter Your Guess Number : "))
        
        if g == num :
            print("Congratulation ....")
            print("You Won the Game ...")
            print("------Game Over-----")
            break       
        elif g > num :
            print("Your Guess Number Is larger than the Correct Number please chose smaller Number...  ")       
        else :
            print("Your Guess Number Is smaller than the Correct Number please chose larger Number...  ")

    elif choice == 2 :
        print("\nThank You for Playing....\n") 
        break
    
    
    else :
        print("\nInvalid Choice... ")
        print("Please Select  Correct Choice... \n")