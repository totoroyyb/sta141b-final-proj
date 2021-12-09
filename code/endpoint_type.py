from comparable_enum_base import ComparableEnum

class EndpointType(ComparableEnum):
    '''
    Enum for all different endpoints
    '''
    FLUVIEW = "https://delphi.cmu.edu/epidata/fluview/"
    GFT = "https://delphi.cmu.edu/epidata/gft/"
    FLUSURV = "https://delphi.cmu.edu/epidata/flusurv/"
    WIKI = "https://delphi.cmu.edu/epidata/wiki/"
