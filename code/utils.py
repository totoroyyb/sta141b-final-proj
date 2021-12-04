from typing import List
import pandas as pd

class Utils():
    @staticmethod
    def vectorize_if_need(val) -> list:
        if val == None:
            return None
            
        return val if isinstance(val, list) else [val]

    @staticmethod
    def flatten_list(vals) -> list:
        return [ str(val) for val in vals ]

    @staticmethod
    def extract_epidata(json: dict, variables: List[str] = None) -> pd.DataFrame:
        epidata = pd.DataFrame(json["epidata"])

        if variables != None:
            epidata = epidata[variables]

        return epidata
        