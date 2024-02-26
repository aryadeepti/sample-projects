import numpy as np


'''
    This function will calculate the cost matrix of two time series using the
    DTW formulation.
    
    params:
        x (Numpy Array) : The first time series
        y (Numpy Array) : The second time series
        
    returns:
        The cost matrix associated to the two time series.
        
    
        x = np.array([0,2,0,1,0, -1, 1])
        y = np.array([0,1,-1,-0,2,-1,0])
        dtw(x,y)
'''
def dtw(x,y):

  n, m = len(x), len(y)
    
    # generate & initialize cost matrix
  cost_matrix = np.zeros((n+1, m+1))
  for i in range(n+1):
      for j in range(m+1):
          if i == 0 and j == 0:
              cost_matrix[i,j] = 0
          else:
              cost_matrix[i,j] = np.inf

    # Fill the cost matrix 
  for i in range(1, n+1):
  
    for j in range(1, m+1):
        min_c =0
        c = abs(x[i-1] - y[j-1])
        min_c = min([cost_matrix[i-1,j-1], cost_matrix[i-1,j], cost_matrix[i, j-1]])
        cost_matrix[i,j] = c + min_c
  return cost_matrix
   