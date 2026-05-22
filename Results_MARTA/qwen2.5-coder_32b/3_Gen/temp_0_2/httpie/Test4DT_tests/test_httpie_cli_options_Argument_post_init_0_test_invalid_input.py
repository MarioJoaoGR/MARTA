
import pytest
from httpie.cli.options import Argument

def test_invalid_input():
    with pytest.raises(TypeError):
        arg = Argument()
