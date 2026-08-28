
import pytest
from pysnooper.variables import Attrs


def test_invalid_input():
    with pytest.raises(TypeError):
        Attrs()