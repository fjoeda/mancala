import sys
import time

# A tuple of the player's pits:
PLAYER_1_PITS = ('A', 'B', 'C', 'D', 'E', 'F')
PLAYER_2_PITS = ('G', 'H', 'I', 'J', 'K', 'L')
PIT_LABELS = 'ABCDEF1LKJIHG2'
STARTING_NUMBER_OF_SEEDS = 4 

class MancalaGame:
    @staticmethod
    def opposite_pit(pit):
        OPPOSITE_PIT = {'A': 'G', 'B': 'H', 'C': 'I', 'D': 'J', 'E': 'K',
                        'F': 'L', 'G': 'A', 'H': 'B', 'I': 'C', 'J': 'D',
                        'K': 'E', 'L': 'F'}
        return OPPOSITE_PIT[pit]

    @staticmethod
    def next_pit(pit):
        NEXT_PIT = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': '1',
                    '1': 'L', 'L': 'K', 'K': 'J', 'J': 'I', 'I': 'H', 'H': 'G',
                    'G': '2', '2': 'A'}
        return NEXT_PIT[pit]

    @staticmethod
    def get_new_board(s = STARTING_NUMBER_OF_SEEDS):
        return {'1': 0, '2': 0, 'A': s, 'B': s, 'C': s, 'D': s, 'E': s,
                'F': s, 'G': s, 'H': s, 'I': s, 'J': s, 'K': s, 'L': s}


    def display_board(board, playerTurn):
        """Displays the game board as ASCII-art based on the board
        dictionary."""

        seedAmounts = []
        # This 'GHIJKL21ABCDEF' string is the order of the pits left to
        # right and top to bottom:
        
        for pit in 'GHIJKL21ABCDEF':
            numSeedsInThisPit = str(board[pit]).rjust(2)
            seedAmounts.append(numSeedsInThisPit)
        if playerTurn == '1':
            print("""
    +------+------+--<<<<<-Player 2----+------+------+------+
    2      |G     |H     |I     |J     |K     |L     |      1
           |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |
    S      |      |      |      |      |      |      |      S
    T  {}  +------+------+------+------+------+------+  {}  T
    O      |A     |B     |C     |D     |E     |F     |      O
    R      |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |      R
    E      |      |      |      |      |      |      |      E
    +------+------+------+"Player 1">>>>>-----+------+------+

    """.format(*seedAmounts))
        else:
            print("""
    +------+------+--<<<<<"Player 2"---+------+------+------+
    2      |G     |H     |I     |J     |K     |L     |      1
           |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |
    S      |      |      |      |      |      |      |      S
    T  {}  +------+------+------+------+------+------+  {}  T
    O      |A     |B     |C     |D     |E     |F     |      O
    R      |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |      R
    E      |      |      |      |      |      |      |      E
    +------+------+------+-Player 1->>>>>-----+------+------+

    """.format(*seedAmounts))


    @staticmethod
    def ask_for_player_move_console(playerTurn, board):
        """Asks the player which pit on their side of the board they
        select to sow seeds from. Returns the uppercase letter label of the
        selected pit as a string."""
        if playerTurn == '1':
            while True:  # Keep asking the player until they enter a valid move.
                # Ask the player to select a pit on their side:
                if playerTurn == '1':
                    print('Player 1, choose move: A-F (or QUIT)')
                elif playerTurn == '2':
                    print('Player 2, choose move: G-L (or QUIT)')
                response = input('> ').upper().strip()

                # Check if the player wants to quit:
                if response == 'QUIT':
                    print('Thanks for playing!')
                    sys.exit()

                # Make sure it is a valid pit to select:
                if (playerTurn == '1' and response not in PLAYER_1_PITS) or (
                    playerTurn == '2' and response not in PLAYER_2_PITS
                ):
                    print('Please pick a letter on your side of the board.')
                    continue  # Ask player again for their move.
                if board.get(response) == 0:
                    print('Please pick a non-empty pit.')
                    continue  # Ask player again for their move.
                return response
        else:
            while True:  # Keep asking the player until they enter a valid move.
                # Ask the player to select a pit on their side:
                if playerTurn == '2':
                    print('Player 2, choose move: G-L (or QUIT)')
                response = input('> ').upper().strip()

                # Check if the player wants to quit:
                if response == 'QUIT':
                    print('Thanks for playing!')
                    sys.exit()

                # Make sure it is a valid pit to select:
                if (playerTurn == '1' and response not in PLAYER_1_PITS) or (
                    playerTurn == '2' and response not in PLAYER_2_PITS
                ):
                    print('Please pick a letter on your side of the board.')
                    continue  # Ask player again for their move.
                if board.get(response) == 0:
                    print('Please pick a non-empty pit.')
                    continue  # Ask player again for their move.
                return response

    @staticmethod
    def make_move(board, playerTurn, pit):
        seedsToSow = board[pit]  # Get number of seeds from selected pit.
        board[pit] = 0  # Empty out the selected pit.

        while seedsToSow > 0:
            print('\n' * 60)# Continue sowing until we have no more seeds.
            MancalaGame.display_board(board, playerTurn)
            time.sleep(1.3)
            pit = MancalaGame.next_pit(pit)  # Move on to the next pit.
            if (playerTurn == '1' and pit == '2') or (
                playerTurn == '2' and pit == '1'
            ):
                continue  # Skip opponent's store.
            board[pit] += 1
            seedsToSow -= 1

        # If the last seed went into the player's store, they go again.
        if (pit == playerTurn == '1') or (pit == playerTurn == '2'):
            # The last seed landed in the player's store; take another turn.
            return playerTurn

        # Check if last seed was in an empty pit; take opposite pit's seeds.
        if playerTurn == '1' and pit in PLAYER_1_PITS and board[pit] == 1:
            oppositePit = MancalaGame.opposite_pit(pit)
            if board[oppositePit] != 0:
                board['1'] += board[oppositePit]
                board[oppositePit] = 0
                board['1'] += board[pit]
                board[pit] = 0
        elif playerTurn == '2' and pit in PLAYER_2_PITS and board[pit] == 1:
            oppositePit = MancalaGame.opposite_pit(pit)
            if board[oppositePit] != 0:
                board['2'] += board[oppositePit]
                board[oppositePit] = 0
                board['2'] += board[pit]
                board[pit] = 0

        # Return the other player as the next player:
        if playerTurn == '1':
            return '2'
        elif playerTurn == '2':
            return '1'

    @staticmethod
    def make_move_simulate(board, playerTurn, pit):
        seedsToSow = board[pit]  # Get number of seeds from selected pit.
        board[pit] = 0  # Empty out the selected pit.

        while seedsToSow > 0:
            pit = MancalaGame.next_pit(pit)  # Move on to the next pit.
            if (playerTurn == '1' and pit == '2') or (
                playerTurn == '2' and pit == '1'
            ):
                continue  # Skip opponent's store.
            board[pit] += 1
            seedsToSow -= 1

        # If the last seed went into the player's store, they go again.
        if (pit == playerTurn == '1') or (pit == playerTurn == '2'):
            # The last seed landed in the player's store; take another turn.
            return playerTurn

        # Check if last seed was in an empty pit; take opposite pit's seeds.
        if playerTurn == '1' and pit in PLAYER_1_PITS and board[pit] == 1:
            oppositePit = MancalaGame.opposite_pit(pit)
            if board[oppositePit] != 0:
                board['1'] += board[oppositePit]
                board[oppositePit] = 0
                board['1'] += board[pit]
                board[pit] = 0
        elif playerTurn == '2' and pit in PLAYER_2_PITS and board[pit] == 1:
            oppositePit = MancalaGame.opposite_pit(pit)
            if board[oppositePit] != 0:
                board['2'] += board[oppositePit]
                board[oppositePit] = 0
                board['2'] += board[pit]
                board[pit] = 0

        # Return the other player as the next player:
        if playerTurn == '1':
            return '2'
        elif playerTurn == '2':
            return '1'

    @staticmethod
    def check_for_winner(board):

        player1Total = board['A'] + board['B'] + board['C']
        player1Total += board['D'] + board['E'] + board['F']
        player2Total = board['G'] + board['H'] + board['I']
        player2Total += board['J'] + board['K'] + board['L']

        if player1Total == 0:
            board['2'] += player2Total
            for pit in PLAYER_2_PITS:
                board[pit] = 0  
        elif player2Total == 0:
            board['1'] += player1Total
            for pit in PLAYER_1_PITS:
                board[pit] = 0  
        else:
            return 'no winner'  

        if board['1'] > board['2']:
            return '1'
        elif board['2'] > board['1']:
            return '2'
        else:
            return 'tie'


class GameAI:
    @staticmethod
    def make_temp_move(board, playerTurn, pit):
        seedsToSow = board[pit]  
        board[pit] = 0 

        while seedsToSow > 0:
            pit = MancalaGame.next_pit(pit)  # Move on to the next pit.
            if (playerTurn == '1' and pit == '2') or (
                playerTurn == '2' and pit == '1'
            ):
                continue  # Skip opponent's store.
            board[pit] += 1
            seedsToSow -= 1

        if playerTurn == '1' and pit in PLAYER_1_PITS and board[pit] == 1:
            oppositePit = MancalaGame.opposite_pit(pit)
            if board[oppositePit] > 0:
                board['1'] += board[oppositePit]
                board[oppositePit] = 0
                board['1'] += board[pit]
                board[pit] = 0
        elif playerTurn == '2' and pit in PLAYER_2_PITS and board[pit] == 1:
            oppositePit = MancalaGame.opposite_pit(pit)
            if board[oppositePit] > 0:
                board['2'] += board[oppositePit]
                board[oppositePit] = 0
                board['2'] += board[pit]
                board[pit] = 0

        if pit == playerTurn:
            is_continue = True
        else:
            is_continue = False

        return board, is_continue

    @staticmethod
    def greedy_Move(playerTurn, board:dict):
        if playerTurn == '1':
            eval_score = []
            temp_board_list = []
            for pit in PLAYER_1_PITS:
                temp_board, _ = GameAI.make_temp_move(board.copy(),playerTurn, pit)
                score = temp_board["1"] - temp_board["2"]
                eval_score.append(score)
                temp_board_list.append(temp_board)
            min_eval = -999
            selected_idx = 0
            
            for i, score in enumerate(eval_score):
                if score > min_eval and board[PLAYER_1_PITS[i]] != 0:
                    selected_idx = i
                    min_eval = score

            return PLAYER_1_PITS[selected_idx]
        else:
            eval_score = []
            temp_board_list = []
            for i, pit in enumerate(PLAYER_2_PITS):
                temp_board, _ = GameAI.make_temp_move(board.copy(),playerTurn, pit)
                score = temp_board["2"] - temp_board["1"]
                dist = abs(board[pit]-(i+1))
                eval_score.append(score-dist)
                temp_board_list.append(temp_board)
            min_eval = -999
            selected_idx = 0
            
            for i, score in enumerate(eval_score):
                if score > min_eval and board[PLAYER_2_PITS[i]] != 0:
                    selected_idx = i
                    min_eval = score

            return PLAYER_2_PITS[selected_idx]

    @staticmethod
    def vs_greedy_move(playerTurn, board:dict):
        """Asks the player which pit on their side of the board they
        select to sow seeds from. Returns the uppercase letter label of the
        selected pit as a string."""
        PLAYER_2_PITS_REVERSE  = [PLAYER_2_PITS[i] for i in range(len(PLAYER_2_PITS)-1,-1,-1)]
        if playerTurn == '1':
            while True:  # Keep asking the player until they enter a valid move.
                # Ask the player to select a pit on their side:
                if playerTurn == '1':
                    print('Player 1, choose move: A-F (or QUIT)')
                elif playerTurn == '2':
                    print('Player 2, choose move: G-L (or QUIT)')
                response = input('> ').upper().strip()

                # Check if the player wants to quit:
                if response == 'QUIT':
                    print('Thanks for playing!')
                    sys.exit()

                # Make sure it is a valid pit to select:
                if (playerTurn == '1' and response not in PLAYER_1_PITS) or (
                    playerTurn == '2' and response not in PLAYER_2_PITS
                ):
                    print('Please pick a letter on your side of the board.')
                    continue  # Ask player again for their move.
                if board.get(response) == 0:
                    print('Please pick a non-empty pit.')
                    continue  # Ask player again for their move.
                return response

            
        else:
            eval_score = []
            temp_board_list = []
            for pit in PLAYER_2_PITS:
                temp_board, _ = GameAI.make_temp_move(board.copy(),playerTurn, pit)
                score = temp_board["2"] - temp_board["1"]
                eval_score.append(score)
                temp_board_list.append(temp_board)
            
            min_eval = -999
            selected_idx = 0
            
            for i, score in enumerate(eval_score):
                if score > min_eval and board[PLAYER_2_PITS[i]] != 0:
                    selected_idx = i
                    min_eval = score

            return PLAYER_2_PITS[selected_idx]

    @staticmethod
    def vs_greedy_move_2(playerTurn, board:dict):
        """Asks the player which pit on their side of the board they
        select to sow seeds from. Returns the uppercase letter label of the
        selected pit as a string."""
        PLAYER_2_PITS_REVERSE  = [PLAYER_2_PITS[i] for i in range(len(PLAYER_2_PITS)-1,-1,-1)]
        if playerTurn == '1':
            while True:  # Keep asking the player until they enter a valid move.
                # Ask the player to select a pit on their side:
                if playerTurn == '1':
                    print('Player 1, choose move: A-F (or QUIT)')
                elif playerTurn == '2':
                    print('Player 2, choose move: G-L (or QUIT)')
                response = input('> ').upper().strip()

                # Check if the player wants to quit:
                if response == 'QUIT':
                    print('Thanks for playing!')
                    sys.exit()

                # Make sure it is a valid pit to select:
                if (playerTurn == '1' and response not in PLAYER_1_PITS) or (
                    playerTurn == '2' and response not in PLAYER_2_PITS
                ):
                    print('Please pick a letter on your side of the board.')
                    continue  # Ask player again for their move.
                if board.get(response) == 0:
                    print('Please pick a non-empty pit.')
                    continue  # Ask player again for their move.
                return response

            
        else:
            eval_score = []
            temp_board_list = []
            for i, pit in enumerate(PLAYER_2_PITS):
                temp_board, _ = GameAI.make_temp_move(board.copy(),playerTurn, pit)
                score = temp_board["2"] - temp_board["1"]
                dist = abs(board[pit]-(i+1))
                eval_score.append(score-dist)
                temp_board_list.append(temp_board)
            min_eval = -999
            selected_idx = 0
            
            for i, score in enumerate(eval_score):
                if score > min_eval and board[PLAYER_2_PITS[i]] != 0:
                    selected_idx = i
                    min_eval = score

            return PLAYER_2_PITS[selected_idx]

    @staticmethod
    def evaluate_move(board, playerTurn, pit):
        PLAYER_2_PITS_REVERSE  = [PLAYER_2_PITS[i] for i in range(len(PLAYER_2_PITS)-1,-1,-1)]
        if playerTurn == '1':
            eval_score = []
            temp_board_list = []

            root_board, is_continue = GameAI.make_temp_move(board.copy(),playerTurn, pit)
            final_score = root_board["1"] - root_board["2"]
            
            if is_continue:
                for pit in PLAYER_1_PITS:
                    temp_board, is_continue = GameAI.make_temp_move(root_board.copy(),playerTurn, pit)
                    score = temp_board["1"] - temp_board["2"]
                    eval_score.append(score)
                    temp_board_list.append(temp_board)
                min_eval = -999
                selected_idx = 0

                for i, score in enumerate(eval_score):
                    if score > min_eval and board[PLAYER_1_PITS[i]] != 0:
                        selected_idx = i
                        min_eval = score

                return GameAI.evaluate_move(root_board.copy(), playerTurn, PLAYER_1_PITS[selected_idx])

            
        else:
            eval_score = []
            temp_board_list = []
            
            root_board, is_continue = GameAI.make_temp_move(board.copy(),playerTurn, pit)
            final_score = root_board["2"] - root_board["1"]
            
            if is_continue:
                for i, pit in enumerate(PLAYER_2_PITS_REVERSE):
                    temp_board, is_continue = GameAI.make_temp_move(root_board.copy(),playerTurn, pit)
                    score = temp_board["2"] - temp_board["1"]
                    eval_score.append(score)
                    temp_board_list.append(temp_board)
                min_eval = -999
                selected_idx = 0

                for i, score in enumerate(eval_score):
                    if score > min_eval and board[PLAYER_2_PITS_REVERSE[i]] != 0:
                        selected_idx = i
                        min_eval = score

            
                return GameAI.evaluate_move(root_board.copy(), playerTurn, PLAYER_2_PITS_REVERSE[selected_idx])

        
        return final_score

    @staticmethod
    def get_best_move(board, playerTurn):
        PLAYER_2_PITS_REVERSE  = [PLAYER_2_PITS[i] for i in range(len(PLAYER_2_PITS)-1,-1,-1)]
        eval_score = []
        if playerTurn == '1':
            for pit in PLAYER_1_PITS:
                temp_board, is_continue = GameAI.make_temp_move(board.copy(),playerTurn, pit)
                score = temp_board["1"] - temp_board["2"]
                eval_score.append(score)
                
            min_eval = -999
            selected_idx = 0

            for i, score in enumerate(eval_score):
                if score > min_eval and board[PLAYER_1_PITS[i]] != 0:
                    selected_idx = i
                    min_eval = score

            return PLAYER_1_PITS[selected_idx]
        else:
            for i, pit in enumerate(PLAYER_2_PITS_REVERSE):
                temp_board, is_continue = GameAI.make_temp_move(board.copy(),playerTurn, pit)
                score = temp_board["2"] - temp_board["1"]
                eval_score.append(score)
                
            min_eval = -999
            selected_idx = 0

            for i, score in enumerate(eval_score):
                if score > min_eval and board[PLAYER_2_PITS_REVERSE[i]] != 0:
                    selected_idx = i
                    min_eval = score

            return PLAYER_2_PITS_REVERSE[selected_idx]

    @staticmethod
    def evaluate_move_minimax(board, playerTurn, pit):
        PLAYER_2_PITS_REVERSE  = [PLAYER_2_PITS[i] for i in range(len(PLAYER_2_PITS)-1,-1,-1)]
        if playerTurn == '1':
            eval_score = []
            temp_board_list = []

            root_board, is_continue = GameAI.make_temp_move(board.copy(),playerTurn, pit)
            final_score = root_board["1"] - root_board["2"]
            
            if is_continue:
                for pit in PLAYER_1_PITS:
                    temp_board, is_continue = GameAI.make_temp_move(root_board.copy(),playerTurn, pit)
                    score = temp_board["1"] - temp_board["2"]
                    eval_score.append(score)
                    temp_board_list.append(temp_board)
                min_eval = -999
                selected_idx = 0

                for i, score in enumerate(eval_score):
                    if score > min_eval and board[PLAYER_1_PITS[i]] != 0:
                        selected_idx = i
                        min_eval = score

                return GameAI.evaluate_move(root_board.copy(), '1', PLAYER_1_PITS[selected_idx])
            
        else:
            eval_score = []
            temp_board_list = []
            
            root_board, is_continue = GameAI.make_temp_move(board.copy(),playerTurn, pit)
            final_score = root_board["2"] - root_board["1"]
            
            if is_continue:
                for i, pit in enumerate(PLAYER_2_PITS_REVERSE):
                    temp_board, is_continue = GameAI.make_temp_move(root_board.copy(),playerTurn, pit)
                    score = temp_board["2"] - temp_board["1"]
                    eval_score.append(score)
                    temp_board_list.append(temp_board)
                min_eval = -999
                selected_idx = 0

                for i, score in enumerate(eval_score):
                    if score > min_eval and board[PLAYER_2_PITS_REVERSE[i]] != 0:
                        selected_idx = i
                        min_eval = score

            
                return GameAI.evaluate_move(root_board.copy(), playerTurn, PLAYER_2_PITS_REVERSE[selected_idx])

        
        return final_score
        

    @staticmethod
    def evaluate_move_hoarder_vs_attacker(board, playerTurn, pit):
        PLAYER_2_PITS_REVERSE  = [PLAYER_2_PITS[i] for i in range(len(PLAYER_2_PITS)-1,-1,-1)]
        if playerTurn == '1':
            eval_score = []
            temp_board_list = []

            root_board, is_continue = GameAI.make_temp_move(board.copy(),playerTurn, pit)
            total_board = [board['D'], board['F']]
            final_score = (root_board["1"] - root_board["2"]) + sum(total_board)
            
            if is_continue:
                for pit in PLAYER_1_PITS:
                    temp_board, is_continue = GameAI.make_temp_move(root_board.copy(),playerTurn, pit)
                    total_board = [temp_board['D'], temp_board['F']]
                    score =(root_board["1"] - root_board["2"]) + sum(total_board)
                    eval_score.append(score)
                    temp_board_list.append(temp_board)
                min_eval = -999
                selected_idx = 0

                for i, score in enumerate(eval_score):
                    if score > min_eval and board[PLAYER_1_PITS[i]] != 0:
                        selected_idx = i
                        min_eval = score

                return GameAI.evaluate_move_hoarder_vs_attacker(root_board.copy(), playerTurn, PLAYER_1_PITS[selected_idx])

            
        else:
            eval_score = []
            temp_board_list = []
            
            root_board, is_continue = GameAI.make_temp_move(board.copy(),playerTurn, pit)
            final_score = root_board["2"] - root_board["1"]
            
            if is_continue:
                for i, pit in enumerate(PLAYER_2_PITS_REVERSE):
                    temp_board, is_continue = GameAI.make_temp_move(root_board.copy(),playerTurn, pit)
                    score = temp_board["2"] - temp_board["1"]
                    eval_score.append(score)
                    temp_board_list.append(temp_board)
                min_eval = -999
                selected_idx = 0

                for i, score in enumerate(eval_score):
                    if score > min_eval and board[PLAYER_2_PITS_REVERSE[i]] != 0:
                        selected_idx = i
                        min_eval = score

            
                return GameAI.evaluate_move_hoarder_vs_attacker(root_board.copy(), playerTurn, PLAYER_2_PITS_REVERSE[selected_idx])

        
        return final_score

    @staticmethod
    def evaluate_move_hoarder_vs_hoarder(board, playerTurn, pit):
        PLAYER_2_PITS_REVERSE  = [PLAYER_2_PITS[i] for i in range(len(PLAYER_2_PITS)-1,-1,-1)]
        if playerTurn == '1':
            eval_score = []
            temp_board_list = []

            root_board, is_continue = GameAI.make_temp_move(board.copy(),playerTurn, pit)
            total_board = [board['D'], board['F']]
            final_score = (root_board["1"] - root_board["2"]) + sum(total_board)
            
            if is_continue:
                for pit in PLAYER_1_PITS:
                    temp_board, is_continue = GameAI.make_temp_move(root_board.copy(),playerTurn, pit)
                    total_board = [temp_board['D'], temp_board['F']]
                    score =(root_board["1"] - root_board["2"]) + sum(total_board)
                    eval_score.append(score)
                    temp_board_list.append(temp_board)
                min_eval = -999
                selected_idx = 0

                for i, score in enumerate(eval_score):
                    if score > min_eval and board[PLAYER_1_PITS[i]] != 0:
                        selected_idx = i
                        min_eval = score

                return GameAI.evaluate_move_hoarder_vs_hoarder(root_board.copy(), playerTurn, PLAYER_1_PITS[selected_idx])

            
        else:
            eval_score = []
            temp_board_list = []
            
            root_board, is_continue = GameAI.make_temp_move(board.copy(),playerTurn, pit)
            total_board = [board['I'], board['H']]
            final_score = (root_board["2"] - root_board["1"]) + sum(total_board)
            
            if is_continue:
                for i, pit in enumerate(PLAYER_2_PITS_REVERSE):
                    temp_board, is_continue = GameAI.make_temp_move(root_board.copy(),playerTurn, pit)
                    total_board = [temp_board['I'], temp_board['H']]
                    score = (root_board["2"] - root_board["1"]) + sum(total_board)
                    eval_score.append(score)
                    temp_board_list.append(temp_board)
                min_eval = -999
                selected_idx = 0

                for i, score in enumerate(eval_score):
                    if score > min_eval and board[PLAYER_2_PITS_REVERSE[i]] != 0:
                        selected_idx = i
                        min_eval = score

            
                return GameAI.evaluate_move_hoarder_vs_hoarder(root_board.copy(), playerTurn, PLAYER_2_PITS_REVERSE[selected_idx])

        
        return final_score


    @staticmethod
    def vs_greedy_move3(playerTurn, board:dict):
        """Asks the player which pit on their side of the board they
        select to sow seeds from. Returns the uppercase letter label of the
        selected pit as a string."""
        PLAYER_2_PITS_REVERSE  = [PLAYER_2_PITS[i] for i in range(len(PLAYER_2_PITS)-1,-1,-1)]
        if playerTurn == '1':
            while True:  # Keep asking the player until they enter a valid move.
                # Ask the player to select a pit on their side:
                if playerTurn == '1':
                    print('Player 1, choose move: A-F (or QUIT)')
                elif playerTurn == '2':
                    print('Player 2, choose move: G-L (or QUIT)')
                response = input('> ').upper().strip()

                # Check if the player wants to quit:
                if response == 'QUIT':
                    print('Thanks for playing!')
                    sys.exit()

                # Make sure it is a valid pit to select:
                if (playerTurn == '1' and response not in PLAYER_1_PITS) or (
                    playerTurn == '2' and response not in PLAYER_2_PITS
                ):
                    print('Please pick a letter on your side of the board.')
                    continue  # Ask player again for their move.
                if board.get(response) == 0:
                    print('Please pick a non-empty pit.')
                    continue  # Ask player again for their move.
                return response

            
        else:
            eval_score = []
            for pit in PLAYER_2_PITS_REVERSE:
                score = GameAI.evaluate_move_hoarder_vs_hoarder(board.copy(),playerTurn,pit)
                eval_score.append(score)
                #temp_board_list.append(temp_board)
            min_eval = -999
            selected_idx = 0
            #temp_board_num = 0
            for i, score in enumerate(eval_score):
                if score > min_eval and board[PLAYER_2_PITS_REVERSE[i]] != 0:
                    selected_idx = i
                    min_eval = score

            return PLAYER_2_PITS_REVERSE[selected_idx]

    @staticmethod
    def greedy_cvc(playerTurn, board:dict):
        """Asks the player which pit on their side of the board they
        select to sow seeds from. Returns the uppercase letter label of the
        selected pit as a string."""
        PLAYER_2_PITS_REVERSE  = [PLAYER_2_PITS[i] for i in range(len(PLAYER_2_PITS)-1,-1,-1)]
        if playerTurn == '1':
            eval_score = []
            temp_board_list = []
            for pit in PLAYER_1_PITS:
                score = GameAI.evaluate_move_hoarder_vs_hoarder(board.copy(),playerTurn,pit)
                eval_score.append(score)
                #temp_board_list.append(temp_board)
            min_eval = -999
            selected_idx = 0
            #temp_board_num = 0
            for i, score in enumerate(eval_score):
                if score >= min_eval and board[PLAYER_1_PITS[i]] != 0:
                    selected_idx = i
                    min_eval = score

            return PLAYER_1_PITS[selected_idx]
            
        else:
            eval_score = []
            temp_board_list = []
            for pit in PLAYER_2_PITS_REVERSE:
                score = GameAI.evaluate_move_hoarder_vs_hoarder(board.copy(),playerTurn,pit)
                eval_score.append(score)
                #temp_board_list.append(temp_board)
            min_eval = -999
            selected_idx = 0
            #temp_board_num = 0
            for i, score in enumerate(eval_score):
                if score >= min_eval and board[PLAYER_2_PITS_REVERSE[i]] != 0:
                    selected_idx = i
                    min_eval = score

            return PLAYER_2_PITS_REVERSE[selected_idx]


    @staticmethod
    def move_computer(board:dict):
        PLAYER_2_PITS_REVERSE  = [PLAYER_2_PITS[i] for i in range(len(PLAYER_2_PITS)-1,-1,-1)]
        eval_score = []
        temp_board_list = []
        for pit in PLAYER_2_PITS_REVERSE:
            score = GameAI.evaluate_move_hoarder_vs_hoarder(board.copy(),'2',pit)
            eval_score.append(score)
            #temp_board_list.append(temp_board)
        min_eval = -999
        selected_idx = 0
        #temp_board_num = 0
        for i, score in enumerate(eval_score):
            if score >= min_eval and board[PLAYER_2_PITS_REVERSE[i]] != 0:
                selected_idx = i
                min_eval = score

        return PLAYER_2_PITS_REVERSE[selected_idx]