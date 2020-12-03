import random

def display_board(board):

	print('\n'*100)
	print('                                   ''TIC TAC TOE')
	print()
	print('                                       |'' |')
	print('                                      '+board[1]+'|'+board[2]+'|'+board[3])
	print('                                       |'' |')
	print('                              ----------------------')
	print('                                       |'' |')
	print('                                      '+board[4]+'|'+board[5]+'|'+board[6])
	print('                                       |'' |')
	print('                              ----------------------')
	print('                                       |'' |')
	print('                                      '+board[7]+'|'+board[8]+'|'+board[9])
	print('                                       |'' |')
	
	print('\n'*4)
	

def player_input():

	marker = ''

	while marker != 'X' and marker != 'O':

		marker = (input('PLAYER 1 CAN SELECT X OR O: ')).upper()

		if marker != 'X' and marker != 'O':

			print("!!!PLEASE CHOOSE 'X' OR 'O'")


	if marker == 'X':

		return ('X','O')

	else:

		return ('O','X')


def place_marker(board, marker, position):
    
    board[position] = marker


def win_check(board, mark):
    
    return ((board[1]==board[2]==board[3]==mark) or
    (board[4]==board[5]==board[6]==mark) or
    (board[7]==board[8]==board[9]==mark) or
    (board[1]==board[4]==board[7]==mark) or
    (board[2]==board[5]==board[8]==mark) or
    (board[3]==board[6]==board[9]==mark) or
    (board[3]==board[5]==board[7]==mark) or
    (board[1]==board[5]==board[9]==mark))


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    
    return board[position] == ' '

    
def full_board_check(board):

	for i in range(1,10):

		if space_check(board,i):

			return False

	return True

def player_choice(board):

	position = 0

	while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):

		position = int(input('CHOOSE YOUR NEXT POSITION FROM (1-9): '))


	return position


def replay():


	if input("Do you want to play again? Enter 'YES' or 'NO': ").lower()[0] == 'y':

		return True

	else:

		return False



# LOGIC

print('\n'*100)

print('                              Welcome to Tic Tac Toe!')

print('\n'*10)

while True:

	theboard = [' '] * 10

	player1_marker,player2_marker = player_input()

	turn = choose_first()

	print(turn + ' WILL GO FIRST')

	play_game = input("ARE YOU READY TO PLAY ENTER 'YES' OR 'NO': ")

	if play_game.lower()[0] == 'y':

		game_on = True

	else:

		game_on = False


	while game_on:

		if turn == 'Player 1':

			display_board(theboard)

			print('Player 1 : ')

			position = player_choice(theboard)

			place_marker(theboard,player1_marker,position)

			if win_check(theboard,player1_marker):

				display_board(theboard)

				print('                CONGRATULATION player_1 YOU HAVE WON THE GAME!!!')
				print()

				game_on = False

			else:

				if full_board_check(theboard):

					display_board(theboard)

					print('                                THE GAME IS DRAW!!!')
					print()

					break
				else:

					turn = 'Player 2'


		else:

			display_board(theboard)

			print('Player 2 : ')

			position = player_choice(theboard)

			place_marker(theboard,player2_marker,position)


			if win_check(theboard,player2_marker):

				display_board(theboard)

				print('                CONGRATULATION player_2 YOU HAVE WON THE GAME!!!')
				print()

				game_on = False


			else:

				if full_board_check(theboard):

					display_board(theboard)

					print('                                THE GAME IS DRAW!')
					print()

					break

				else:

					turn = 'Player 1'
					


	if not replay():
		break
