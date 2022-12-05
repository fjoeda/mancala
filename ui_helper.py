import streamlit as st
import time

ph = st.empty()
# A tuple of the player's pits:
PLAYER_1_PITS = ('A', 'B', 'C', 'D', 'E', 'F')
PLAYER_2_PITS = ('G', 'H', 'I', 'J', 'K', 'L')
PIT_LABELS = 'ABCDEF1LKJIHG2'
STARTING_NUMBER_OF_SEEDS = 4 

btn_list = []

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

    def __init__(self, ph) -> None:
        self.ph = ph
        if 'board' not in st.session_state:
            self.initiate_state(MancalaGame.get_new_board())
            #self.render()
    
    def initiate_state(self, board, is_beginning = True):
        st.session_state['player_move'] = 1
        if is_beginning:
            st.session_state['game_state'] = 'start'
        st.session_state['board'] = board

    def start(self, agent):
        self.initiate_state(MancalaGame.get_new_board(), False)
        st.session_state['game_state'] = 'playing'
        st.session_state['agent'] = agent
        #self.render()

    def restart(self):
        st.session_state['game_state'] = 'start'
    
    def make_move_player(self, pit):
        if st.session_state['board'][pit] != 0:
            next_move = self.make_move('1', pit)
            while next_move == '2':
                player_2_pit = GameAI.move_computer(st.session_state['board'])
                print(player_2_pit)
                next_move = self.make_move('2', player_2_pit)

            winner = self.check_for_winner()
            is_end = False
            if winner == '1' or winner == '2':
                is_end = True
                if winner == '1':
                    st.balloons()
                    st.info("Anda menang")
                else:
                    st.info("Anda kalah")
                # TODO: tampilkan pemenang
            elif winner == 'tie':
                #print('There is a tie!')
                st.info("Permainan berakhir seri")
                is_end = True
                # TODO: tampilkan seri

            if is_end:
                self.render()
                st.session_state['game_state'] = 'end'
                

    def render(self):
        
        col1, col2, col3, col4, col5, col6, col7, col8 = self.ph.columns(8)
        g1, g2, g3, g4, g5, g6, g7, g8 = self.ph.columns(8)
        col9, col10, col11, col12, col13, col14, col15, col16 = self.ph.columns(8)
            

        with col2:
            st.write("<h6 style='text-align: center; color: red'>G</h6>", unsafe_allow_html=True)
            st.write(f"<h3 style='text-align: center; color: black;'>{st.session_state['board']['G']}</h3>", unsafe_allow_html=True)

        with col3:
            st.write("<h6 style='text-align: center; color: red;'>H</h6>", unsafe_allow_html=True)
            st.write(f"<h3 style='text-align: center; color: black;'>{st.session_state['board']['H']}</h3>", unsafe_allow_html=True)

        with col4:
            st.write("<h6 style='text-align: center; color: red;'>I</h6>", unsafe_allow_html=True)
            st.write(f"<h3 style='text-align: center; color: black;'>{st.session_state['board']['I']}</h3>", unsafe_allow_html=True)

        with col5:
            st.write("<h6 style='text-align: center; color: red;'>J</h6>", unsafe_allow_html=True)
            st.write(f"<h3 style='text-align: center; color: black;'>{st.session_state['board']['J']}</h3>", unsafe_allow_html=True)
            
        with col6:
            st.write("<h6 style='text-align: center; color: red;'>K</h6>", unsafe_allow_html=True)
            st.write(f"<h3 style='text-align: center; color: black;'>{st.session_state['board']['K']}</h3>", unsafe_allow_html=True)

        with col7:
            st.write("<h6 style='text-align: center; color: red;'>L</h6>", unsafe_allow_html=True)
            st.write(f"<h3 style='text-align: center; color: black;'>{st.session_state['board']['L']}</h3>", unsafe_allow_html=True)

        #with col8:

            
        with g1:
            st.metric("Score A", st.session_state['board']['2'])

        with g2:
            st.write("""---""")

        with g3:
            st.write("""---""")
            
        with g4:
            st.write("""---""")
            
        with g5:
            st.write("""---""")
            
        with g6:
            st.write("""---""")
            
        with g7:
            st.write("""---""")

        with g8:
            st.metric("Score B", st.session_state['board']['1'])
            
        #with col9:
            
        with col10:
            st.write(f"<h3 style='text-align: center; color: black;'>{st.session_state['board']['A']}</h3>", unsafe_allow_html=True)
            #st.write("<h6 style='text-align: center; color: blue;'>A</h6>", unsafe_allow_html=True)
            

        with col11:
            st.write(f"<h3 style='text-align: center; color: black;'>{st.session_state['board']['B']}</h3>", unsafe_allow_html=True)
            #st.write("<h6 style='text-align: center; color: blue;'>B</h6>", unsafe_allow_html=True)
            

        with col12:
            st.write(f"<h3 style='text-align: center; color: black;'>{st.session_state['board']['C']}</h3>", unsafe_allow_html=True)
            #st.write("<h6 style='text-align: center; color: blue;'>C</h6>", unsafe_allow_html=True) 

        with col13:
            st.write(f"<h3 style='text-align: center; color: black;'>{st.session_state['board']['D']}</h3>", unsafe_allow_html=True)
            #st.write("<h6 style='text-align: center; color: blue;'>D</h6>", unsafe_allow_html=True)

        with col14:
            st.write(f"<h3 style='text-align: center; color: black;'>{st.session_state['board']['E']}</h3>", unsafe_allow_html=True)
            #st.write("<h6 style='text-align: center; color: blue;'>E</h6>", unsafe_allow_html=True)
            
        with col15:
            st.write(f"<h3 style='text-align: center; color: black;'>{st.session_state['board']['F']}</h3>", unsafe_allow_html=True)
            #st.write("<h6 style='text-align: center; color: blue;'>F</h6>", unsafe_allow_html=True)
            
        

    def make_move(self, playerTurn, pit):
        seedsToSow = st.session_state['board'][pit]  # Get number of seeds from selected pit.
        st.session_state['board'][pit] = 0  # Empty out the selected pit.

        while seedsToSow > 0:
            self.render()
            time.sleep(1.3)
            pit = MancalaGame.next_pit(pit)  # Move on to the next pit.
            if (playerTurn == '1' and pit == '2') or (
                playerTurn == '2' and pit == '1'
            ):
                continue  # Skip opponent's store.
            st.session_state['board'][pit] += 1
            seedsToSow -= 1

        # If the last seed went into the player's store, they go again.
        if (pit == playerTurn == '1') or (pit == playerTurn == '2'):
            # The last seed landed in the player's store; take another turn.
            return playerTurn

        # Check if last seed was in an empty pit; take opposite pit's seeds.
        if playerTurn == '1' and pit in PLAYER_1_PITS and st.session_state['board'][pit] == 1:
            oppositePit = MancalaGame.opposite_pit(pit)
            if st.session_state['board'][oppositePit] != 0:
                st.session_state['board']['1'] += st.session_state['board'][oppositePit]
                st.session_state['board'][oppositePit] = 0
                st.session_state['board']['1'] += st.session_state['board'][pit]
                st.session_state['board'][pit] = 0
        elif playerTurn == '2' and pit in PLAYER_2_PITS and st.session_state['board'][pit] == 1:
            oppositePit = MancalaGame.opposite_pit(pit)
            if st.session_state['board'][oppositePit] != 0:
                st.session_state['board']['2'] += st.session_state['board'][oppositePit]
                st.session_state['board'][oppositePit] = 0
                st.session_state['board']['2'] += st.session_state['board'][pit]
                st.session_state['board'][pit] = 0

        # Return the other player as the next player:
        
        if playerTurn == '1':
            self.render()
            return '2'
        elif playerTurn == '2':
            self.render()
            return '1'
    
    
    def check_for_winner(self):

        player1Total = st.session_state['board']['A'] + st.session_state['board']['B'] + st.session_state['board']['C']
        player1Total += st.session_state['board']['D'] + st.session_state['board']['E'] + st.session_state['board']['F']
        player2Total = st.session_state['board']['G'] + st.session_state['board']['H'] + st.session_state['board']['I']
        player2Total += st.session_state['board']['J'] + st.session_state['board']['K'] + st.session_state['board']['L']

        if player1Total == 0:
            st.session_state['board']['2'] += player2Total
            for pit in PLAYER_2_PITS:
                st.session_state['board'][pit] = 0  
        elif player2Total == 0:
            st.session_state['board']['1'] += player1Total
            for pit in PLAYER_1_PITS:
                st.session_state['board'][pit] = 0  
        else:
            return 'no winner'  

        if st.session_state['board']['1'] > st.session_state['board']['2']:
            return '1'
        elif st.session_state['board']['2'] > st.session_state['board']['1']:
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

        if st.session_state['agent'] == 'A' or st.session_state['agent'] == 'B':
             for pit in PLAYER_2_PITS_REVERSE:
                score = GameAI.evaluate_move(board.copy(),'2',pit)
                eval_score.append(score)
        else:
             for pit in PLAYER_2_PITS_REVERSE:
                score = GameAI.evaluate_move_hoarder_vs_hoarder(board.copy(),'2',pit)
                eval_score.append(score)
        
                
        min_eval = -999
        selected_idx = 0
        #temp_board_num = 0
        if st.session_state['agent'] == 'B' or st.session_state['agent'] == 'D':
            for i, score in enumerate(eval_score):
                if score >= min_eval and board[PLAYER_2_PITS_REVERSE[i]] != 0:
                    selected_idx = i
                    min_eval = score
        else:
            for i, score in enumerate(eval_score):
                if score > min_eval and board[PLAYER_2_PITS_REVERSE[i]] != 0:
                    selected_idx = i
                    min_eval = score

        return PLAYER_2_PITS_REVERSE[selected_idx]