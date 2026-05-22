
import pytest
from httpie.cli.options import Argument

def test_edge_case():
    with pytest.raises(TypeError):
        arg = Argument()
