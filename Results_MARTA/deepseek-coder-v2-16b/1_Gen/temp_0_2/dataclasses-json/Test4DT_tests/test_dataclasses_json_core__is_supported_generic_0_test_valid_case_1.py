
import pytest
from typing import List, Union, Optional
from dataclasses_json.core import _is_supported_generic

class MyType: pass

def test_valid_case_1():
    assert _is_supported_generic(List[int]) == True
