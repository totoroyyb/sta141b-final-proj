from typing import List
from utils import Utils
from comparable_enum_base import ComparableEnum

class FluSurvRegion(ComparableEnum):
    CA = "CA"
    CO = "CO"
    CT = "CT"
    GA = "GA"
    IA = "IA"
    ID = "ID"
    MD = "MD"
    MI = "MI"
    MN = "MN"
    NM = "NM"
    NY_ALBANY = "NY_albany"
    NY_ROCHESTER = "NY_rochester"
    OH = "OH"
    OK = "OK"
    OR = "OR"
    RI = "RI"
    SD = "SD"
    TN = "TN"
    UT = "UT"
    NETWORK_ALL = "network_all"
    NETWORK_EIP = "network_eip"
    NETWORK_IHSP = "network_ihsp"

class FluSurvParams():
    def __init__(
        self, 
        epiweeks: List[str], 
        regions: List[FluSurvRegion],
        issues: List[str] = None,
        lag: int = None
    ):
        self.epiweeks = Utils.vectorize_if_need(epiweeks)
        self.regions = Utils.vectorize_if_need(regions)

        # Optional Params
        self.issues = Utils.vectorize_if_need(issues)
        self.lag = lag

    def query(self) -> dict:
        query_dict = {
            "epiweeks": Utils.flatten_list(self.epiweeks),
            "locations": Utils.flatten_list(self.regions)
        }
        if self.issues != None:
            query_dict["issues"] = Utils.flatten_list(self.issues)

        if self.lag != None:
            query_dict["lag"] = self.lag

        return query_dict