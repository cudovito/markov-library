# Get unique elements from a list
class Unique:
    
    def __init__(self):
        pass

    def get_unique_list(self, list1):
        """
        Description: Calculate unique list to channels in the user journey path
        Input: list1(List): Contains the list of the elements
        Output: unique_list(list) 
        """
        
        # Variable declaration  
        unique_list = []

        for x in list1:
        
            if x not in unique_list:
                
                # If value not in list append
                unique_list.append(x)

        return (unique_list)
