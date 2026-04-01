
import pytest
from unittest.mock import patch
from flutes.multiproc import DummyApplyResult

def test_valid_input():
    dummy = DummyApplyResult(42)
    assert dummy.get() == 42
