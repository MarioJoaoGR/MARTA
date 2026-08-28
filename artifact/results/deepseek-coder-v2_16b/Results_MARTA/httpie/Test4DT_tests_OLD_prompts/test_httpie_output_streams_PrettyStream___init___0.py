
import pytest
from httpie.output.streams import PrettyStream
from unittest.mock import patch, MagicMock

# Test for successful instantiation with provided conversion and formatting objects

# Test for default instantiation without providing conversion and formatting objects
def test_pretty_stream_default_instantiation():
    with pytest.raises(TypeError):
        pretty_stream = PrettyStream()

# Test for mocked instantiation to ensure it raises the expected TypeError