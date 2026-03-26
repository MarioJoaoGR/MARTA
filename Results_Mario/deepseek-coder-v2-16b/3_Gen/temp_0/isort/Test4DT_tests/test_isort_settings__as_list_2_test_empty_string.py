
import pytest
from isort.settings import _as_list

def test_empty_string():
    assert _as_list("") == []
