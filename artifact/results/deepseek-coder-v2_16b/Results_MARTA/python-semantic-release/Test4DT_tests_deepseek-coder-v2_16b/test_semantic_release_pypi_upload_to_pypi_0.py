
import pytest
from unittest.mock import patch
from semantic_release.pypi import upload_to_pypi
from semantic_release.errors import ImproperConfigurationError


def test_invalid_inputs():
    with patch('semantic_release.pypi.os.environ', {}):
        with pytest.raises(ImproperConfigurationError):
            upload_to_pypi()  # Call without parameters should raise a TypeError