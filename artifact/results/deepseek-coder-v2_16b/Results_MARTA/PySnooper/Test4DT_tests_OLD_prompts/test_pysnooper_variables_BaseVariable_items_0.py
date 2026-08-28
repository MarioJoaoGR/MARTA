
import pytest
from pysnooper.variables import BaseVariable


def test_edge_cases():
    with pytest.raises(TypeError):
        var_none = BaseVariable(None)
