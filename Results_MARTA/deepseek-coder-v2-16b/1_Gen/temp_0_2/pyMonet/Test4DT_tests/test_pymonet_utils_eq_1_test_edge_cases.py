
import pytest

def eq(value, value1) -> bool:
    return value == value1

@pytest.mark.parametrize("test_input, expected", [
    (None, None),
    ([], []),
    ("", ""),
    (0, 0),
    (True, True),
    (False, False)
])
def test_edge_cases(test_input, expected):
    assert eq(test_input, expected) == (test_input == expected)
