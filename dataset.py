import chess
import chess.pgn
import os
from state2 import State


class TrainingSet:
    def __init__(self):
        self.game_results = []
        self.state = State()
        self.labels = {"0-1":-1, "1/2-1/2": 0,"1-0":1}

        self.pieces = {'P':1, 'N':2, 'B':3, 'R':4, 'Q':5, 'K':6,
                        'p':9, 'n':10,'b':11,'r':12,'q':13,'k':14}



        self.path = 'games-pgn/'
        self.read_games()
        # 1 is white wins, -1 black victory, 0 is for draw 
        

    def getResults(self):
        return self.game_results


    def read_games(self):
        for fn in os.listdir(self.path):
            pgn = open(self.path+fn)
            game = chess.pgn.read_game(pgn) 
            self.serialize_results(game)           
            board = chess.Board()
            for move in game.mainline_moves():
                board.push(move)
            #print(board)
        self.state.serialize()



    def serialize_results(self, game):
        # creating the labels from we know the results
        self.game_results.append(self.labels[game.headers["Result"]])
        
        




if __name__ == "__main__":
    TrainingSet = TrainingSet()
    