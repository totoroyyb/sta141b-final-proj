from enum import Enum

class ComparableEnum(str, Enum):
    def __str__(self) -> str:
        return self.value
    
    def equals(self, endpoint_type):
        return str(self) == str(endpoint_type)
