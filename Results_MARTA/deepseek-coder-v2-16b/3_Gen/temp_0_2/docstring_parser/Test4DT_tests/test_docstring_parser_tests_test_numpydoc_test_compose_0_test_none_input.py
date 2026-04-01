
import pytest
from docstring_parser.tests.test_numpydoc import parse, compose

@pytest.mark.parametrize("source, expected", [
    (None, "Expected output string")
])
def test_compose(source, expected):
    with pytest.raises(AssertionError):
        assert compose(parse(source)) == expected
