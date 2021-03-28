import pandas as pd
import numpy as np
import collections
from itertools import chain


# Helper Functions
from utils.calculate_rank.Rank import calculate_rank
from utils.calculate_removal_effect.RemovalEffect import removal_effects
from utils.simulation import simulation
from utils.unique.Unique import unique
from utils.transaction_matrix.TransactionMatrix import trans_mat


class Markov:

    # Cunstructor call
    def __init__(self):
        pass

    
    # Main Function ( Calculate removal effect for an input dataset)
    def get_markov_count(data_set, column_1, column_2 ):
        """
        Description:
        Args: column_1 (numeric) : Column to caluculate removal effect , column_2 (string) : Path to conversion  
        Response: Dataframe

        """
        # Taking copy of the dataset
        data_set_copy = data_set.copy()
        
        # Converting column_1 to numeric fomat to calculate removal effect
        data_set_copy[column_1] = pd.to_numeric(data_set_copy[column_1], errors='ignore')
        
        # Checking if the dataset column_1 is not empty
        if data_set_copy[column_1].sum() != 0:
            df1 = data_set_copy[data_set_copy[column_1]>=1]
        else:
            df1 = data_set_copy.copy()

        # Grouping dataset on colum_1 to get the count of conversion from that path
        df2 = df1.groupby(df1[column_2])[column_1].sum().reset_index()
        df3 = df1.groupby(df1[column_2]).count().reset_index()
        
        df4 = df2.merge(df3,on=column_2)
                    
        # Repeat each index a set number of times
        if final_df[column_1].sum() != 0:
            final_df = (
                final_df.reindex(final_df.index.repeat(final_df.Conversion_Count))).reset_index()

            final_df[column_1] = 1  # set conversion to 1 as 1 is coverted with a paticular path

            # Call just path and conversion columns
            final_df = final_df[[column_2, column_1]]
            data_set_copy = (final_df.groupby([column_2]).sum()).reset_index()
            data_set_copy['probability'] = data_set_copy[column_1] / data_set_copy[column_1].sum()

            # Initializing dataframe to store final dataframe 
            final = pd.DataFrame()  


            import_data = pd.DataFrame({column_2: np.random.choice(data_set_copy[column_2],
                                                                size=data_set_copy[column_1].sum(),
                                                                p=data_set_copy['probability'], replace=True)})

            import_data[column_1] = 1

            tr_matrix = trans_mat.get1(import_data)

            channel_only = list(filter(lambda k0: k0 not in ['start', 'convert'], tr_matrix.columns))

            ga_ex = pd.DataFrame()
            tr_mat = tr_matrix.copy()

            for i in range(len(import_data)):
                a = import_data[column_2][i]
                b=a.split('>')
                p.append(b)

            path = list(itertools.chain.from_iterable(p))
            counter = collections.Counter(path)

            df = pd.DataFrame({column_2: list(counter.keys()), 'count': list(counter.values())})

            df = df[[column_2, 'count']]
            ga_ex = ga_ex.append(df, ignore_index=True)

            df1 = (pd.DataFrame(ga_ex.groupby([column_2])[['count']].sum())).reset_index()

            # Removal effect is where removing a channel and checking how much is it affecting the probability of conversation
            df1 = df1[df1[column_2].isin(channel_only)]
            removal_effects_dict = removal_effects(tr_mat, 1)
            removal_effects_array = []

            for channel in df1[column_2]:
                if removal_effects_dict[channel]:
                    removal_effects_array.append(removal_effects_dict[channel])
                else:
                    removal_effects_array.append(0)

            df1['removal_effects'] = removal_effects_array
            df1['assisted_conversion_colum'] = removal_effects_array

            final = final.append(df1, ignore_index=True)

            #  Calculating unique channel
            unique_channel = unique.get(final[
                                            column_2])  

            final_df = pd.DataFrame()

            for i in range(0, len(unique_channel)):
                # Storing all paramaters in new dataframe
                x = (final['assisted_conversion_colum'][final[column_2] == unique_channel[i]]).values
                final_df.loc[i, 0] = unique_channel[i]
                final_df.loc[i, 1] = x.mean()

                
               
            final_df.columns = ['channel', 'assisted_column_1']
            final_df['assisted_conversion_colum'] = sum(data_set_copy[column_1]) * final_df['assisted_conversion_colum'] / sum(
                final_df['assisted_conversion_colum'])
        else:
            final_dict = {'channel': [], 'assisted_column_1': []}
            final_df = pd.DataFrame(final_dict)
            
            final_dict1 = {column_2: [], 'count': [], 'removal_effects': [], 'assisted_conversion_colum': []}
            final = pd.DataFrame(final_dict1)
        
        return final_df, final