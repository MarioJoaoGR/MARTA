
import pytest
from httpie.cli.argparser import HTTPieHelpFormatter

def test_edge_case():
    with pytest.raises(TypeError):
        formatter = HTTPieHelpFormatter()
