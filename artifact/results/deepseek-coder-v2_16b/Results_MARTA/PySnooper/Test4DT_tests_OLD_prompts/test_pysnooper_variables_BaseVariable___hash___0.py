
import pytest
from pysnooper.variables import BaseVariable



def test_invalid_input_without_parentheses():
    with pytest.raises(TypeError):
        var_without_parentheses = BaseVariable("x + y")