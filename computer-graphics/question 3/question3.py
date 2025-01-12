import numpy as np

def reconstruct_matrix(U, S, V):
   
    S_matrix = np.diag(S)  
    return np.dot(np.dot(U, S_matrix), V)