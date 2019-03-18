import chess
from node import Node
from state import GameState
import random
from math import *

def UTC (root_state, itermax, verbose = False):
    rootnode = Node(state = root_state)
    
    for i in range(itermax):
        node = rootnode
        state = root_state.Clone()
        # basicly while node is fully expanded
        while node.untried_moves == [] and node.childNodes != []:
            
            # Select
            node = node.UTCSelectChild()
            state.DoMove(node.move)

            # Expand
            if node.untried_moves != []:
                m = random.choice(node.untried_moves)
                state.DoMove(m)
                node = node.AddChild(m, state)
            
            # Rollout
            while state.GetMoves() != []:
                # so its while state is non-terminal
                state.DoMove(random.choice(state.GetMoves()))

            #Backprop
            while node != None:
                #backprop from the expanded node and work it back into the root
                node.Update(state.GetResult(node.player_moved))
                node = node.parentNode


    if (verbose) :
        print(rootnode.TreeToString(0))
    else:
        print(rootnode.ChildrenToString())
    print(rootnode.childNodes)
    return sorted(rootnode.childNodes, key = lambda c: c.visits)[-1].move

def play():
    state = GameState()
    while state.GetMoves() != []:
        #print(str(state))
        #TODO to implement to String state
        if state.player_moved == 1:
            m = UTC(root_state = state, itermax = 1000, verbose = False)
        else:
            m = UTC(root_state=state, itermax = 100 , verbose = False)
        #do the best chosen move
        state.DoMove(m)
    if state.GetResult(state.player_moved) == 0.0:
        print("Player" + str(state.player_moved) + "wins!")
    else:
        print("Player" + str(3 - state.player_moved) + "wins!")



if __name__ == "__main__":
    play()