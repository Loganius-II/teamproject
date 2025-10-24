# main file that runs program
import random

num1_range = 1
num2_range = 1000

def main():
    # loops the menu
    running = True
    while running:
        running = menu()

def menu():
    # menu
    print("Menu:")
    print("1. New game")
    print("2. Change range")
    print("3. Exit game")
    
    option = int(input('Choose an option: '))
    
    if option == 1:
        game()
        return True
    elif option == 2:
        Min = int(input("Please enter the minimum: "))
        Max = int(input("Please enter the maximum: "))
        while Min >= Max:
            print("The minimum must be less than the maximum")
            Min = int(input("Please enter the minimum: "))
            Max = int(input("Please enter the maximum: "))
        while Min < 1:
            print("The minimum most be greater than 0")
            Min = int(input("Please enter the minimum: ")) 
            while Min >= Max:
                print("The minimum must be less than the maximum")
                Min = int(input("Please enter the minimum: "))
                Max = int(input("Please enter the maximum: "))
        change_range(Min, Max)
        return True
    elif option == 3:
        return False

def player_name():
    # returns player 1 and 2 names in a tuple
    # from input
    
    p1 = input('Player 1 Name: ')
    p2 = input('Player 2 Name: ')
    
    return p1, p2

def random_num(num1, num2):
    # num1 and num2 integers
    # just returns a random number between the range
    return random.randint(num1, num2)

def game():
    #runs the game
    player1, player2 = player_name()
    number = random_num(num1_range, num2_range)
    range1 = num1_range
    range2 = num2_range
    guess = 0
    win = 0
    while not win: 
        while guess not in range(range1, range2):
            guess = int(input(f"{player1} guess a number between {range1}-{range2}: "))
        if guess == number:
            print(player1, "you win!!!")
            win = 1
        else:
            if guess < number:
                range1 = guess
            else:
                range2 = guess
        guess = 0
        if not win:
            while guess not in range(range1, range2):
                guess = int(input(f"{player2} guess a number between {range1}-{range2}: "))
            if guess == number:
                print(player2, "you win!!!")
                win = 1
            else:
                if guess < number:
                    range1 = guess
                else:
                    range2 = guess
        guess = 0
    

def change_range(num1, num2):
    # num1 and num2 must be integers fo the range
    # changes the range of numbers
    # of global variables
    # returns nothing
        global num1_range, num2_range
        num1_range = num1
        num2_range = num2

if __name__ == '__main__':
    main()
    
