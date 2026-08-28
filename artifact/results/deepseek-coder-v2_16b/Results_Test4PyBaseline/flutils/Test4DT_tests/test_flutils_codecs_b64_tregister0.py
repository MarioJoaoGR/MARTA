# Module: flutils.codecs.b64
# Import the function correctly using its module name
import pytest
from flutils.codecs import b64

def test_register():
    """Test that the register function does not raise an error when called."""
    try:
        b64.register()
    except Exception as e:
        assert False, f"The register function raised an unexpected exception: {e}"
