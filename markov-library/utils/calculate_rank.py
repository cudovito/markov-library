from enums.calculate_rank.enum import Type

# Assert messages
from assert_messages.calculate_rank.index import calculate_rank_assert

class Rank:

    def __init__(self):
        pass

    def calculate_rank(self, vector):
        """
        Description: Calculutate column rank
        Input: vector(1D Array)
        Output: rank_vector(1D Array)
        """

        # Args validation
        assert isinstance(vector, list), calculate_rank_assert.get('VECTOR_TYPE_CHECK')
        assert isinstance(vector[0], int), calculate_rank_assert.get('VECTOR_NULL_CHECK')
        assert not isinstance(vector[0], list), calculate_rank_assert.get('VECTOR_DIMENSION_CHECK')

        a={}

        rank = 0
        
        for num in sorted(vector):
            if num not in a:
                a[num] = rank
                rank = rank + 1
            
        # Constructing vector of ranks   
        rank_result = [a[i] for i in vector]
        
        return rank_result
