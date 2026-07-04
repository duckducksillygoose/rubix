import numpy as np

COLORS = ["W", "R", "B", "O", "G", "Y"]  # defining the moves

def solved_cube():
    # 6 faces × 9 stickers each
    print(np.array([c for c in COLORS for _ in range(9)]))
    return

def one_hot_encode(state):
    mapping = {c: i for i, c in enumerate(COLORS)}
    idxs = np.array([mapping[c] for c in state])
    one_hot = np.eye(len(COLORS))[idxs]  # 1 dimensional vector
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