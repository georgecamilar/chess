import chess
from math import *
import random


class GameState:
    def __init__(self, board = None):
        # 1 means player1 moved
        # 2 means player2 moved
        self.player_moved = 2 # init with 2 so p1 can play

        if board == None:
            self.board_state = chess.Board()
        else:
            self.board_state = board

    def Serialize(self):
        import numpy as np
        assert self.board_states


    def getTurn(self):
        if(self.player_moved == 2):
            #black moved and its time for white
            return True
        else:
            #white moved and its time for black
            return False

    def Clone(self) :
        st = GameState()
        st.player_moved = self.player_moved
        return st
    

    def DoMove(self, move):
        self.player_moved = 3-self.player_moved
        self.board_state.push(move)
        #update for python-chess
        #white - True
        #black - False 
        #as defined in the python-chess library

    def GetMoves(self):
        #get all possible moves
        list = []

        for move in self.board_state.legal_moves:
            list.append(move)

        print(list)
        return list
        

    def GetResult(self):
        return self.board_state.result



if __name__ == "__main__":
    gamestate = GameState()
    print(gamestate.board_state)
    gamestate.DoMove(gamestate.GetMoves()[1])
    
    print(gamestate.board_state)
    gamestate.DoMove(gamestate.GetMoves()[1])
    
