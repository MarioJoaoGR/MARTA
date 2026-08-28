
import pytest
from unittest.mock import patch, MagicMock
import re

# Import the function you want to test from pytutils.lazy.lazy_regex
from pytutils.lazy.lazy_regex import lazy_compile


def test_edge_case_none():
    with pytest.raises(TypeError):
        re.compile(None)