
import pytest
from dataclasses_json.core import _decode_generic
from enum import Enum
from typing import List, Optional, Any
from dataclasses import dataclass

# Define a simple dataclass for demonstration
@dataclass
class DataClassExample:
    value: int



def test_invalid_input():
    with pytest.raises(ValueError):
        class MyInvalidEnum(Enum):
            A = 1
            B = 2
        
        res = _decode_generic(MyInvalidEnum, 'C', infer_missing=False)