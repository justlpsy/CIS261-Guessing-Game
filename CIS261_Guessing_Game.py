import random

def display_title ():
    print("Guessing the number game!")
    print()
    
def play_game(limit):
    NUMBER = random.randint(1, limit)
    print(f"I am thinking of a number from 1 to {limit}\n")
    count = 1
    guess = int(input("Your guess?:  "))
                
    while(guess != NUMBER):
        if guess < NUMBER:
            print("Too low")
            count += 1
        elif guess > NUMBER:
            print("Too high")
            count += 1
        guess = int(input("Your guess?:  "))
    print(f"You guess it in {count} tries. \n")

def new_func(limit):
    NUMBER = random.randint(1, limit)
    return NUMBER
    
def main():
    display_title()
    again = "yes"
    while again.lower() == "yes":
        limit = int(input("Enter the limit:  "))
        play_game(limit)
        again = input("Would you like to play again? Enter (yes/no)")
        print()
    print("Bye")
    
if __name__ == "__main__":
    main()