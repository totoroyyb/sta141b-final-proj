from typing import List
import pandas as pd

class Utils():
    '''
    Utility functions
    '''

    @staticmethod
    def vectorize_if_need(val) -> list:
        '''
        If one single element is passed on, 
        then wrap that number into a list and return it.
        Otherwise, return the passed in list.
        '''

        if val == None:
            return None
            
        return val if isinstance(val, list) else [val]

    @staticmethod
    def flatten_list(vals) -> list:
        return [ str(val) for val in vals ]

    @staticmethod
    def extract_epidata(json: dict, variables: List[str] = None) -> pd.DataFrame:
        '''
        Extract the epidata part from a json, and 
        return the result as a dataframe.
        '''
        
        epidata = pd.DataFrame(json["epidata"])

        if variables != None:
            epidata = epidata[variables]

        return epidata
        