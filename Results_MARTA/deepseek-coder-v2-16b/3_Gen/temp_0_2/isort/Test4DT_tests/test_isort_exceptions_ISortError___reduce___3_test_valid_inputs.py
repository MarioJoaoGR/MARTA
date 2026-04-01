
import pytest
from isort.exceptions import ISortError
from unittest.mock import patch
from functools import partial

@pytest.mark.parametrize("test_input", [1, "string", {"key": "value"}, None])
def test_valid_inputs(test_input):
    with pytest.raises(ISortError):
        raise ISortError()
