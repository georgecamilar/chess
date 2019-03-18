import random
from math import *
from state import GameState



class Node :
    def __init__(self, move = None, parent = None, state= None):
        self.move = move
        self.parentNode = parent
        self.childNodes = []
        self.wins = 0
        self.visits = 0
        
        #future child nodes
        self.untriedMoves = state.GetMoves()

        self.player_moved = state.player_moved

    def UTCSelectChild(self):
        #UCB1 formula to select a child node
        s = sorted(self.childNodes, key = lambda c: c.wins/c.visits + sqrt(2*log(self.visits)/c.visits))[-1]
        return s


    def AddChild(self, m, s):
        '''
        create a new node with the next move and
         add it to the child node list
        '''
        n = Node(move = m, parent = self, state = s)
        self.untriedMoves.remove(m)
        self.childNodes.append(n)
        return n

    def Update(self, result):
        '''
            Update this node - one additional visit and 
            result additional wins 
            The result must be from the viewpoint of the self.player_moved
        '''

        self.visits += 1
        self.wins += result

    #TODO  def __repr__(self):


    def TreeToString(self, indent):
        s = s.IndentString(indent) + str(self)

    
    def IndentString(self, indent):
        s = "\n"
        for i in range(1, indent+1):
            s += "| "
        return s
    
    def ChildrenToString(self):
        s = ""
        for c in self.childNodes:
             s += str(c) + "\n"
        return s