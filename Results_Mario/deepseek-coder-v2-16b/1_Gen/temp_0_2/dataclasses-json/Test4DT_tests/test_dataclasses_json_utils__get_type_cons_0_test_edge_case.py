
import sys
from dataclasses import dataclass
from typing import List, Union
import pytest
from dataclasses_json.utils import _get_type_cons

# Mocking the necessary parts of the `typing` module for Python 3.6 compatibility
if sys.version_info < (3, 7):
    from unittest.mock import MagicMock
else:
    from unittest.mock import patch

@pytest.mark.parametrize("type_, expected", [
    (List[int], list),
    (Union[int, str], Union),
])
def test_get_type_cons(type_, expected):
    if sys.version_info < (3, 7):
        # For Python versions less than 3.7, we need to mock the __origin__ attribute
        with patch('dataclasses_json.utils._get_type_cons.__origin__', new=MagicMock(return_value=expected)):
            assert _get_type_cons(type_) == expected
    else:
        # For Python 3.7 and above, we can directly check the __origin__ attribute
        assert _get_type_cons(type_) == expected
