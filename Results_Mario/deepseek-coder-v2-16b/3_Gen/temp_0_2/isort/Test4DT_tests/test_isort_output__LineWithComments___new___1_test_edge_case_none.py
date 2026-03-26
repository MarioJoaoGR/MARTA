
from isort.output import _LineWithComments  # Assuming this is the correct import path
import pytest

@pytest.mark.parametrize("value, comments", [
    (None, ["First comment", "Second comment"]),
    ("example value", []),
    (123, ["Numeric line"])
])
def test_edge_case_none(value, comments):
    line = _LineWithComments.__new__(_LineWithComments, value, comments)
    assert isinstance(line, _LineWithComments)
    assert line.comments == comments
