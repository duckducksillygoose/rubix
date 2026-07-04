import numpy as np
import random
from movelist import move_table

COLOURS = ["W", "R", "B", "O", "G", "Y"]  # defining the moves

def solved_cube():
    # 6 faces × 9 stickers each
    print(np.array([c for c in COLOURS for _ in range(9)]))
    return

def one_hot_encode(state):
    mapping = {c: i for i, c in enumerate(COLOURS)}
    idxs = np.array([mapping[c] for c in state])
    one_hot = np.eye(len(COLOURS))[idxs]  # 1 dimensional vector
    return one_hot.flatten()  


solved_cube()

#add all of my moves

U_perm = np.array([
    6,3,0,7,4,1,8,5,2,   # U face rotated
    9,10,11,12,13,14,15,16,17,
    18,19,20,21,22,23,24,25,26,
    27,28,29,30,31,32,33,34,35,
    36,37,38,39,40,41,42,43,44,
    45,46,47,48,49,50,51,52,53
])

move_table= {"U:": U_perm}

MOVE_NAMES = list(move_table.keys())

def apply_move(state, move):
    perm = move_table[move]
    return state[perm] #make move function



def scramble(n_moves = 5):#random choice rn will change
    state = solved_cube()
    for _ in range(n_moves):
        move = random.choice(MOVE_NAMES)
        state = apply_move(state, move)


def heuristic_distance(state):
    return np.sum(state == solved_cube()) #how close are we to a complete cube?


def compute_rewards(state):
    d0 = heuristic_distance(state)
    rewards = []

    for move in MOVE_NAMES:
        next_state = apply_move(state, move)
        d1 = heuristic_distance(next_state)
        rewards.append(d1 - d0)  # positive = closer to solved

    return np.array(rewards, dtype=np.float32)