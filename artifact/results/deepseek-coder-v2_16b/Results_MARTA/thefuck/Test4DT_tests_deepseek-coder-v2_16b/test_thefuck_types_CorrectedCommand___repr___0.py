
import pytest
from unittest.mock import patch, MagicMock
from io import StringIO
from thefuck.types import CorrectedCommand



def test_invalid_inputs():
    with pytest.raises(TypeError):
        CorrectedCommand('echo Hello', None, 1).run()