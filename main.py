# main file that runs program

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

def player_name():
    # returns player 1 and 2 names in a tuple
    # from input
    
    p1 = input('Player 1 Name: ')
    p2 = input('Player 2 Name: ')
    
    return p1, p2

def game():
    #plays game
    pass

def change_range():
    # changes the range of numbers
    pass

if __name__ == '__main__':
    main()
