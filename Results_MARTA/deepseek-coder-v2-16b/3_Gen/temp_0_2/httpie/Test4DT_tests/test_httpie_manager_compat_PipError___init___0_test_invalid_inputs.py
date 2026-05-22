
import pytest
from httpie.manager.compat import PipError

@pytest.mark.parametrize("stdout, stderr", [
    ("", ""),  # Both stdout and stderr are empty strings
    (None, None),  # Both stdout and stderr are None
    ("some output", None),  # stdout is a string, stderr is None
    (None, "some error")  # stdout is None, stderr is a string
])
def test_invalid_inputs(stdout, stderr):
    with pytest.raises(PipError) as excinfo:
        raise PipError(stdout, stderr)
