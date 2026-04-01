
import pytest
from dataclasses import dataclass
from typing import List, Union, Collection
from decimal import Decimal
from datetime import datetime
from dataclasses_json.core import _decode_items

@dataclass
class MyDataClass:
    pass

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test case for invalid type arguments (not a collection)
        expected = [MyDataClass()]
        xs = ["not a valid item"]  # Invalid input type
        infer_missing = False
        _decode_items(expected, xs, infer_missing)

    with pytest.raises(TypeError):
        # Test case for mismatching number of types and items
        expected = [MyDataClass(), Decimal]  # Mismatch in the number of types and items
        xs = ["not a valid item"]
        infer_missing = False
        _decode_items(expected, xs, infer_missing)
