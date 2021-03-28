import numpy as np

class Simulation:

    def __init__(self):
        pass

    # Get next n simulations paths
    def simulation(trans, n):
        """
        Description: Generation of path using transation matrix
        Args: trans(2D Array): Probability matrix of states, n(int): Number of simulations we want
        Response: simululation_list(List)
        """
        
        # Creating a 1d array to store the path
        sim = [''] * n
        
        # Initilizing the path string with start 
        sim[0] = 'start'
        i = 1
        
        while i < n:
            # Taking the channel value from the transaction matrix
            sim[i] = np.random.choice(trans.columns, 1, p=trans.loc[sim[i - 1], :])[0]
                
            # ending the string with convert 
            if sim[i] == 'convert':
                break
            i = i + 1

        simululation_list = sim[0:i + 1]
        
        return simululation_list
