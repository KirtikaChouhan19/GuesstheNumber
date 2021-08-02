n = 18
number_of_guesses=1
print("\nNumber of guesses is limited")
print("You have only 9 chance\n")

while (number_of_guesses<=9):

    guess_number = int(input("Guess the number :\n"))
    
    if guess_number<18:
        print("You enter less number please input greater number")

    elif guess_number>18:    
        print("You enter greater number please input small number")

    else:
        print("You won\n")
        print(number_of_guesses,"no. of guesse you took to finish the game.\n")
        break    

    print(9-number_of_guesses,"no. of guesses left\n")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9) :
    print("Game over\n")
    