
import pytest
from dataclasses_json import core as dcj_core
from typing import Any, Dict, List, Optional
from dataclasses import dataclass

@dataclass
class DataClassExample:
    value: int


def test_edge_case():
    with pytest.raises(AttributeError):
        with pytest.raises(TypeError):
            raise AttributeError("This should not be raised")

def test_invalid_input():
    with pytest.raises(NameError):
        raise NameError("This will not be caught by a different error type")