
import pytest
from ansible.module_utils.common.validation import check_required_together

def count_terms(term, parameters):
    return 1 if term in parameters else 0

@pytest.mark.parametrize("terms, parameters, expected", [
    (None, {"param1": 1, "param2": 2}, []),
    ([["param1", "param2"], ["param3"]], {"param1": 1, "param2": 2, "param3": 3}, []),
    ([["param1", "param2"], ["param4"]], {"param1": 1, "param3": 3}, [["param1", "param2"], ["param4"]])
])
def test_check_required_together(terms, parameters, expected):
    if expected:
        with pytest.raises(TypeError) as excinfo:
            check_required_together(terms, parameters)
        assert str(excinfo.value) == f"parameters are required together: {', '.join(expected[0])}"
    else:
        result = check_required_together(terms, parameters)
        assert result == []
