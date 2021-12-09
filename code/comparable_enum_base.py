from enum import Enum

class ComparableEnum(str, Enum):
    '''
    Based class for all enums to make sure they are properly comparable.
    '''
    def __str__(self) -> str:
        return self.value
    
    def equals(self, endpoint_type):
        return str(self) == str(endpoint_type)
