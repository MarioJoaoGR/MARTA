
import pytest
from unittest.mock import patch
from string_utils.manipulation import strip_margin, InvalidInputError

def test_edge_case_none():
    with pytest.raises(InvalidInputError):
        strip_margin(None)
