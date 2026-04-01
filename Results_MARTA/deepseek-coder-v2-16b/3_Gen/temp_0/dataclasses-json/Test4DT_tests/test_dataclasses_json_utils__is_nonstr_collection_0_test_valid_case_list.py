
import pytest
from dataclasses_json.utils import _is_nonstr_collection
from typing import List

def test_valid_case_list():
    assert _is_nonstr_collection(List[int]) is True
