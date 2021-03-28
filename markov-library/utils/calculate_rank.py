from enums.calculate_rank.enum import Type

class Rank:

    def __init__(self):
        pass

    def calculate_rank(self, rank_type, vector):
        """
        Description: Calculutate column rank
        Input: vector(1D Array) , rank_type(enum)
        Output: rank_vector(1D Array)
        """
        a={}
        rank=0
        for num in sorted(vector):
            if num not in a:
                a[num]=rank
                rank=rank+1
            
        # Constructing vector of ranks   
        rank_result = [a[i] for i in vector]
        
        return rank_result
