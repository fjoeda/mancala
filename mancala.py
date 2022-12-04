"""Mancala, by Al Sweigart al@inventwithpython.com
The ancient seed-sowing game.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, board game, game, two-player"""

import sys
from helper import MancalaGame, GameAI
import random 

random.seed(1)

def main():
    print('''Mancala, by Al Sweigart al@inventwithpython.com

The ancient two-player, seed-sowing game. Grab the seeds from a pit on
your side and place one in each following pit, going counterclockwise
and skipping your opponent's store. If your last seed lands in an empty
pit of yours, move the opposite pit's seeds into your store. The
goal is to get the most seeds in your store on the side of the board.
If the last placed seed is in your store, you get a free turn.

The game ends when all of one player's pits are empty. The other player
claims the remaining seeds for their store, and the winner is the one
with the most seeds.

More info at https://en.wikipedia.org/wiki/Mancala
''')
    input('Press Enter to begin...')

    win_dict = {
        '1':0,
        '2':0
    }
    play_first_dict = {
        '1':0,
        '2':0
    }
    for i in range(1000):
        gameBoard = MancalaGame.get_new_board()
        playerTurn = str(random.randint(1,2))
        play_first_dict[playerTurn] += 1
        print("simulation : ", i)
        print("main duluan :", playerTurn)
        while True:  # Run a player's turn.
            # "Clear" the screen by printing many newlines, so the old
            # board isn't visible anymore.
            # print('\n' * 60)
            # Display board and get the player's move:
            # MancalaGame.display_board(gameBoard, playerTurn)
            
            playerMove = GameAI.greedy_cvc(playerTurn, gameBoard)
            

            # Carry out the player's move:
            playerTurn = MancalaGame.make_move_simulate(gameBoard, playerTurn, playerMove)
            
            # Check if the game ended and a player has won:
            winner = MancalaGame.check_for_winner(gameBoard)
            #input("Press to play next move")
            if winner == '1' or winner == '2':
                MancalaGame.display_board(gameBoard, playerTurn)  # Display the board one last time.
                #print('Player ' + winner + ' has won!')
                win_dict[winner] += 1
                break
            elif winner == 'tie':
                MancalaGame.display_board(gameBoard, playerTurn)  # Display the board one last time.
                #print('There is a tie!')
                break

        #break

    print("Play first :")
    print(play_first_dict)
    print("Win :")
    print(win_dict)


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
