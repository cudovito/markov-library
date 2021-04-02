import numpy as np

# Assert messages
from assert_messages.simulation.index import simulation_assert

class Simulation:

    def __init__(self):
        pass

    # Get next n simulations paths
    def simulation(self, trans, n):
        """
        Description: Generation of path using transation matrix
        Args: trans(2D Array): Probability matrix of states, n(int): Number of simulations we want
        Response: simululation_list(List)
        """

        # Args validation
        assert isinstance(trans, list), simulation_assert.get('TRANS_TYPE_CHECK')
        assert isinstance(n, int), simulation_assert.get('N_TYPE_CHECK')

        assert isinstance(trans[0][0], float), simulation_assert.get('TRANS_NULL_CHECK')
        assert n > 0, simulation_assert.get('N_NULL_CHECK')

        assert isinstance(trans, list), simulation_assert.get('TRANS_DIMENSION_CHECK')
        assert isinstance(trans[0], list), simulation_assert.get('TRANS_DIMENSION_CHECK')       

    # Type check
    'TRANS_TYPE_CHECK': 'Type of arg "trans" must be a 2D list',
    'N_TYPE_CHECK': 'Type of "n" must be int', 

    # Null value check
    'TRANS_NULL_CHECK': 'Value of arg "trans" cannot be null',
    'N_NULL_CHECK': 'Value of "n" cannot be null', 

    # Dimension check
    'TRANS_DIMENSION_CHECK': 'Dimension of "trans" must be a 2',



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
