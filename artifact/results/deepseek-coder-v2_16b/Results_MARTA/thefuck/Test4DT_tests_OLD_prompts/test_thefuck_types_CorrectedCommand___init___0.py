
import pytest
from unittest.mock import patch
from thefuck.types import CorrectedCommand

def test_invalid_inputs():
    with pytest.raises(TypeError):
        CorrectedCommand()
