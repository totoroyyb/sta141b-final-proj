from typing import List
from utils import Utils
from comparable_enum_base import ComparableEnum

class FluViewRegion(ComparableEnum):
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

class FluViewParams():
    def __init__(
        self, 
        epiweeks: List[str], 
        regions: List[FluViewRegion],
        issues: List[str] = None,
        lag: int = None,
        auth: str = None
    ):
        self.epiweeks = Utils.vectorize_if_need(epiweeks)
        self.regions = Utils.vectorize_if_need(regions)
        
        # Optional Params
        self.issues = Utils.vectorize_if_need(issues)
        self.lag = lag
        self.auth = auth

    def query(self) -> dict:
        query_dict = {
            "epiweeks": Utils.flatten_list(self.epiweeks),
            "regions": Utils.flatten_list(self.regions)
        }
        if self.issues != None:
            query_dict["issues"] = Utils.flatten_list(self.issues)

        if self.lag != None:
            query_dict["lag"] = self.lag

        if self.auth != None:
            query_dict["auth"] = self.auth

        return query_dict