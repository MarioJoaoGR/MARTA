
import pytest
from httpie.cli.options import Argument

def test_invalid_inputs():
    with pytest.raises(TypeError):
        arg = Argument()
