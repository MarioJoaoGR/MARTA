
import pytest
from docstring_parser.tests.test_google import parse, compose

@pytest.mark.parametrize("source, expected", [
    (
        "This is a summary.\n\nArgs:\n    param1 (int): Description of parameter 1.\n    param2 (str): Description of parameter 2.\n\nReturns:\n    int: The result of the operation, which could be an integer.",
        """This is a summary.

Args:
    param1 (int): Description of parameter 1.
    param2 (str): Description of parameter 2.

Returns:
    int: The result of the operation, which could be an integer."""
    )
])
def test_compose(source: str, expected: str) -> None:
    """Test compose in default mode."""
    assert compose(parse(source)) == expected
