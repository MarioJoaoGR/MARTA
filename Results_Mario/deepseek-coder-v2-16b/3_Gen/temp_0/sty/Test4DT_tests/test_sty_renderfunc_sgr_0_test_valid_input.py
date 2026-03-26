
import pytest
from sty import renderfunc

def sgr(num: int) -> str:
    """
    Create a SGR escape sequence.
    """
    return "\033[" + str(num) + "m"

@pytest.mark.parametrize("num, expected", [
    (31, "\033[31m"),
    (32, "\033[32m"),
    (33, "\033[33m"),
    (34, "\033[34m"),
    (35, "\033[35m"),
    (36, "\033[36m"),
    (37, "\033[37m"),
    (91, "\033[91m"),
    (92, "\033[92m"),
    (93, "\033[93m"),
    (94, "\033[94m"),
    (95, "\033[95m"),
    (96, "\033[96m"),
    (97, "\033[97m")
])
def test_valid_input(num, expected):
    assert sgr(num) == expected
