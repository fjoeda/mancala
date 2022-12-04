import streamlit as st
from ui_helper import MancalaGame, GameAI
    


def render_button(ph,game_obj):
    _, col2, col3, col4, col5, col6, col7, _ = ph.columns(8)
    
    with col2:
        st.button('A', on_click=game_obj.make_move_player, args=('A'))

    with col3:
        st.button('B', on_click=game_obj.make_move_player, args=('B'))

    with col4:
        st.button('C', on_click=game_obj.make_move_player, args=('C'))

    with col5:
        st.button('D', on_click=game_obj.make_move_player, args=('D'))

    with col6:
        st.button('E', on_click=game_obj.make_move_player, args=('E'))

    with col7:
        st.button('F', on_click=game_obj.make_move_player, args=('F'))



    #MancalaGame.display_board()
    #print(st.session_state)
    #render_button(ph_button)


ph_button = st.empty()    
ph_board = st.empty() 
game = MancalaGame(ph_board)    

if st.session_state['game_state'] == 'start':
    col_left, col_center, col_right = ph_button.columns(3)
    with col_center:
        st.button("Start", on_click=game.start)
elif st.session_state['game_state'] == 'playing':
    render_button(ph_button, game)
    game.render()
elif st.session_state['game_state'] == 'end':
    col_left, col_center, col_right = ph_button.columns(3)
    with col_center:
        st.button("Restart", on_click=game.restart)
    

print("run this")





