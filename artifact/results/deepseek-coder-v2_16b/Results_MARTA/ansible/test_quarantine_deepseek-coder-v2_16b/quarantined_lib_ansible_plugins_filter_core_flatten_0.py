
import pytest
from ansible.plugins.filter.core import flatten

def is_sequence(obj):
    return isinstance(obj, (list, tuple))

@pytest.mark.parametrize("input_list, expected", [
    ([1, [2, 3], [[4, 5], 6]], [1, 2, 3, 4, 5, 6]),
    ([1, [2, None, 'null', [3, 4]], [[5, 6], 7]], [1, 2, 3, 4, 5, 6, 7]),
    ([1, [2, [3, [4, 5]]]], [1, 2, 3, 4, 5]),
    ([1, [2, [3, [4, 5]]]], [1, 2, 3, 4, 5], id="one_level"),
    ([1, [2, [3, [4, 5]]]], [1, 2, 3, 4, 5], id="two_levels", levels=1),
])
def test_flatten(input_list, expected):
    result = flatten(input_list)
    assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='? (line 12, col 46)
    ([1, [2, [3, [4, 5]]]], [1, 2, 3, 4, 5], id="one_level"),
"""