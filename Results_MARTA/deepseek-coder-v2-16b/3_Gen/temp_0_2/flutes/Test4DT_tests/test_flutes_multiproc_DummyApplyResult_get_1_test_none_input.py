
import pytest
from unittest.mock import patch
from flutes.multiproc import DummyApplyResult

def test_none_input():
    dummy = DummyApplyResult(None)
    assert dummy.get() is None
