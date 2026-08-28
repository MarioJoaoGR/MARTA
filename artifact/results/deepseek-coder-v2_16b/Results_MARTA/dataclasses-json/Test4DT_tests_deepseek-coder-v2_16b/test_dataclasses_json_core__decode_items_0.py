
import pytest
from dataclasses import dataclass
from typing import List, Optional
from dataclasses_json.core import _decode_items

@dataclass
class DataClassExample:
    value: int


def test_decode_optional_with_infer_missing():
    optional_item = Optional[int]
    decoded_optional_item = list(_decode_items(optional_item, [1, None], infer_missing=True))
    assert decoded_optional_item == [1, None]
