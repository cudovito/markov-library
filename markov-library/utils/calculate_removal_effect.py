import pandas as pd
import numpy as np


class RemovalEffect:

    def __init__(self):
        pass

    def removal_effects(df, conversion_rate):
        """
        Description: To calculate removal effect on based on the datafram passed
        Args: df(Dataframe) , conversion_rate(int)
        Response: removal_effects_dict(dataframe)
        """

        # Calculating len of dataframe
        num_rows = len(df['start'])
        
        # Declaring empty array with size same as num_rows
        zero_array = np.zeros(num_rows, dtype=int)

        # Adding Null colum to main dataframe with values of zero_array
        df['Null'] = zero_array

        df.loc[len(df)] = 0

        # Storing index of dataframe
        df['index'] = df.columns

        # Re setting the dataframe index and reordering in value 0
        df.set_index("index", inplace=True)

        # Declaring empty dict
        removal_effects_dict = {}
        
        # Finding all unique channels 
        channels = [channel for channel in df.columns if channel not in ['start',
                                                                        'Null',
                                                                        'convert']]
        
    
        for channel in channels:
            
            # Dropping channel colum
            removal_df = df.drop(channel, axis=1).drop(channel, axis=0)
            
            # Looping into columns of removal_df
            for column in removal_df.columns:

                # Calculating sum of columns of particular channel
                row_sum = np.sum(list(removal_df.loc[column]))
                
                # Checking if null_pct is 0
                null_pct = float(1) - row_sum
                
                if null_pct != 0:

                    # adding null_pct
                    removal_df.loc[column]['Null'] = null_pct
                
                removal_df.loc['Null']['Null'] = 1.0

            removal_to_conv = removal_df[
                ['Null', 'convert']].drop(['Null', 'convert'], axis=0)
            
            removal_to_non_conv = removal_df.drop(
                ['Null', 'convert'], axis=1).drop(['Null', 'convert'], axis=0)

            # Calculation removal effect
            removal_inv_diff = np.linalg.inv(
                np.identity(len(removal_to_non_conv.columns)) - np.asarray(removal_to_non_conv))
            
            removal_dot_prod = np.dot(removal_inv_diff, np.asarray(removal_to_conv))
            
            removal_cvr = pd.DataFrame(removal_dot_prod, index=removal_to_conv.index)[[1]].loc['start'].values[0]
            
            removal_effect = 1 - removal_cvr / conversion_rate
            
            removal_effects_dict[channel] = removal_effect

        return removal_effects_dict