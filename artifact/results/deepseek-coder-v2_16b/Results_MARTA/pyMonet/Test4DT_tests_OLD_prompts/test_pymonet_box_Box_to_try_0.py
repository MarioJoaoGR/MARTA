
import pytest
from pymonet.box import Box
from unittest.mock import patch, MagicMock


def test_invalid_input():
    with pytest.raises(TypeError):
        Box().to_try()