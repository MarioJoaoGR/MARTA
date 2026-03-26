
from isort._vendored.tomli._parser import Flags
import pytest
from typing import Dict

class TestFlags:
    def test_init(self):
        flags = Flags()
        assert isinstance(flags._flags, dict)
        assert flags._flags == {}
