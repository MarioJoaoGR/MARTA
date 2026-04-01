
from functools import partial

import pytest

from isort.exceptions import ISortError


def test_edge_cases():
    with pytest.raises(ISortError):
        raise ISortError()
    
    # Additional edge cases can be tested here if needed, but the basic assertion should suffice for now.
