from typing import List
from comparable_enum_base import ComparableEnum
from utils import Utils

class GFTRegion(ComparableEnum):
    '''
    Enums for all valid google flu trend regions.
    '''
    NAT = "nat"
    HHS1 = "hhs1"
    HHS2 = "hhs2"
    HHS3 = "hhs3"
    HHS4 = "hhs4"
    HHS5 = "hhs5"
    HHS6 = "hhs6"
    HHS7 = "hhs7"
    HHS8 = "hhs8"
    HHS9 = "hhs9"
    HHS10 = "hhs10"
    CEN1 = "cen1"
    CEN2 = "cen2"
    CEN3 = "cen3"
    CEN4 = "cen4"
    CEN5 = "cen5"
    CEN6 = "cen6"
    CEN7 = "cen7"
    CEN8 = "cen8"
    CEN9 = "cen9"

class GTFParams():
    def __init__(
        self, 
        epiweeks: List[str], 
        regions: List[GFTRegion]
    ):
        self.epiweeks = Utils.vectorize_if_need(epiweeks)
        self.regions = Utils.vectorize_if_need(regions)

    def query(self) -> dict:
        '''
        Return the query defined by this param class.
        '''
        
        query_dict = {
            "epiweeks": Utils.flatten_list(self.epiweeks),
            "locations": Utils.flatten_list(self.regions)
        }

        return query_dict
