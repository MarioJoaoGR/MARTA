
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.streams import RawStream

def test_invalid_input():
    with pytest.raises(TypeError):
        stream = RawStream('not_a_number')
