
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.common.validation import check_required_together

def count_terms(term, parameters):
    return sum([1 for key in parameters if term == key])

@pytest.mark.parametrize("terms, parameters, expected", [
    (None, {"param1": 1, "param2": 2}, []),
    ([["param1", "param2"], ["param3"]], {"param1": 1, "param2": 2, "param3": 3}, []),
    ([["param1", "param2"], ["param4"]], {"param1": 1, "param3": 3}, TypeError),
])
def test_check_required_together(terms, parameters, expected):
    if isinstance(expected, type) and issubclass(expected, BaseException):
        with pytest.raises(expected):
            check_required_together(terms, parameters)
    else:
        result = check_required_together(terms, parameters)
        assert result == expected
