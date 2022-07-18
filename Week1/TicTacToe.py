def print_board(gameboard):
    for row in gameboard:
        print(row)


def win_game(gameboard, icon1, icon2):
    x = 0
    while x < 3:
        if ((icon2 == gameboard[x][0] or icon1 == gameboard[x][0]) and gameboard[x][0] == gameboard[x][1] and
                gameboard[x][2] == gameboard[x][1]):
            return True
        elif ((icon2 == gameboard[0][x] or icon1 == gameboard[0][x]) and gameboard[0][x] == gameboard[1][x] and
              gameboard[2][x] == gameboard[1][x]):
            return True
        x += 1
    if ((icon2 == gameboard[0][0] or icon1 == gameboard[0][0]) and gameboard[0][0] == gameboard[1][1] and gameboard[2][
        2] == gameboard[1][1]):
        return True
    elif ((icon2 == gameboard[0][2] or icon1 == gameboard[0][2]) and gameboard[0][2] == gameboard[1][1] and
          gameboard[2][0] == gameboard[1][1]):
        return True
    else:
        return False


def play_game():
    game_over = False
    player1 = input('Player 1 enter your name: ')
    icon1 = input(player1 + ' choose your icon (enter "x" or "o"): ')
    player2 = input('Player 2 enter your name: ')
    icon2 = ''
    if icon1 == 'x':
        icon2 = 'o'
    else:
        icon2 = 'x'
    print(player1 + " you are " + icon1)
    print(player2 + " you are " + icon2)
    player1_choice = ''
    player2_choice = ''
    player1_x = ''
    player1_y = ''
    player2_x = ''
    player2_y = ''
    gameboard = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print_board(gameboard)
    while not game_over:
        same_square = True
        while same_square and not game_over:
            coor = input(player1 + ", select your square: (enter 'x,y'): ")
            player1_choice = coor.split(',')
            player1_x = int(player1_choice[0])
            player1_y = int(player1_choice[1])
            if int(player1_x) > 2:
                print('The x-coordinate is not within limit, choose again.')
                continue
            if int(player1_y) > 2:
                print('The y-coordinate is not within limit, choose again.')
                continue
            if gameboard[player1_x][player1_y] == 'x' or gameboard[player1_x][player1_y] == 'o':
                print('This square is already chosen, choose again.')
                same_square = True
                continue
            else:
                same_square = False
                gameboard[player1_x][player1_y] = icon1
                bool_win = win_game(gameboard, icon1, icon2)
                print_board(gameboard)
                if bool_win:
                    print("Good job " + player1 + ", you won!")
                    game_over = True
        same_square = True
        while same_square and not game_over:
            coor = input(player2 + ", select your square: (enter 'x,y'): ")
            player2_choice = coor.split(',')
            player2_x = int(player2_choice[0])
            player2_y = int(player2_choice[1])
            if int(player2_x) > 2:
                print('The x-coordinate is not within limit, choose again.')
                continue
            if int(player2_y) > 2:
                print('The y-coordinate is not within limit, choose again.')
                continue
            if gameboard[player2_x][player2_y] == 'x' or gameboard[player2_x][player2_y] == 'o':
                print('This square is already chosen, choose again.')
                same_square = True
                continue
            else:
                same_square = False
                gameboard[player2_x][player2_y] = icon2
                bool_win = win_game(gameboard, icon1, icon2)
                print_board(gameboard)
                if bool_win:
                    print("Good job " + player2 + ", you won!")
                    game_over = True


play_game()
