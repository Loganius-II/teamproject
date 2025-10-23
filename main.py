# main file that runs program

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
        change_range()
        return True
    elif option == 3:
        return False

def game():
    #runs the game
    player1, player2 = player_name()
    number = random_num(num1_range, num2_range)
    guess = 0
    win = 0
    while win 
        while guess not in range(num1_range, num2_range):
            guess1 = int(input(f"{player1} enter your guess for a number between {num1_range}-{num2_range}"))
            if guess1 = number:
                print(player1, "you win!!!")
    pass

def change_range():
    # changes the range of numbers
    pass

if __name__ == '__main__':
    main()
    