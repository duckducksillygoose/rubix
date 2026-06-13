# one hot encode rubix vectors
#create all possible moves U u etc blah blah

#use positional to represent cube state

#create a move table and move names
# def apply move
# def scramble, make a set number of moves
#heuristic distance
#def compute_rewards(state):
    #d0 = heuristic_distance(state)
    #rewards = []

    #for move in MOVE_NAMES:
        #next_state = apply_move(state, move)
        #d1 = heuristic_distance(next_state)
        #rewards.append(d1 - d0)  # positive = closer to solved

    #return np.array(rewards, dtype=np.float32)

#import mlp regressor


#training loop and greedy solver