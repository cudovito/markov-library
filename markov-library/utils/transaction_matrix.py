import numpy as np
import pandas as pd

import collections
from itertools import chain

from calculate_rank.Rank import calculate_rank
from unique.Unique import get_unique_list



class TransactionMatrix:

    def __init__(self):
        pass

    def split_fun(self, path):
        """
        Description: Split path on >
        Args: path(string)
        response: unique_list(List)
        """

        unique_list = path.split('>')
        
        return unique_list


    def get_transition_matrix_conversion(self, dataset):
        """
        Description: To calculate a transaction matrix of unique channels
        Args: dataset(DataFrame)
        Response: dataframe
        """
        # Variable declarations 
        path = []
        conversions_array = []
        i = 0

        # Creating initial matrix for channels
        for conversion_value in dataset['Conversion_Count']:
            for k in range(0, conversion_value):
                conversions_array.append(1)
                path.append(dataset['Path'][i])

            i = i + 1

        # Initializing initial dataframe to store processed data
        processing_dataset = pd.DataFrame()
        processing_dataset['Path'] = path
        processing_dataset['Conversion_Count'] = conversions_array

        # Appending all path with start at the begining
        processing_dataset['path1'] = 'start>' + processing_dataset['Path']
        
        # Appending all path with convert at the end 
        processing_dataset['path2'] = processing_dataset['path1'] + '>convert'

        processing_dataset['pair'] = processing_dataset['path2'].apply(self.split_fun)
        
        # Storing the split string and removing duplicates
        unique_list = processing_dataset['pair'].tolist()
        unique_list = list(chain.from_iterable(unique_list))
        unique_list = list(map(str.strip, unique_list))
    
        # Calculating rank of the columns
        vector_rank = calculate_rank(unique_list)
        
        # Generating matrix from the processed data
        matrix = [[0] * len(get_unique_list(unique_list)) for _ in range(len(get_unique_list(unique_list)))]


        for (i, j) in zip(vector_rank, vector_rank[1:]):
            matrix[i][j] += 1

        # Converting the matrix into a dataframe to be comsumed by other functions
        final_dataframe = pd.DataFrame(matrix)
        
        # Filling diagonal values with 0 as it represents same channels
        np.fill_diagonal(final_dataframe.values, 0)

        # Generating final dataframe only considering path ending with convert
        final_dataframe = pd.DataFrame(final_dataframe.values / final_dataframe.values.sum(axis=1)[:, None])
        final_dataframe.columns = sorted(get_unique_list(unique_list))
        final_dataframe['index'] = sorted(get_unique_list(unique_list))
        final_dataframe.set_index("index", inplace=True)
        final_dataframe.loc['convert', :] = 0
        
        return (final_dataframe)
