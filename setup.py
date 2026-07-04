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