
import pytest
from docstring_parser.tests.test_google import parse, compose

@pytest.fixture(params=[
    ("This is a summary.\n\nArgs:\n    param1 (int): Description of parameter 1.\n    param2 (str): Description of parameter 2.\n\nReturns:\n    int: The result of the operation, which could be an integer.",
     """This is a summary.

Args:
    param1 (int): Description of parameter 1.
    param2 (str): Description of parameter 2.

Returns:
    int: The result of the operation, which could be an integer."""),
])
def source_expected_pairs(request):
    return request.param

def test_compose(source_expected_pairs):
    source, expected = source_expected_pairs
    assert compose(parse(source)) == expected
