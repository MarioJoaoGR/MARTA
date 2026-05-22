
import pytest
from httpie.cli.argparser import HTTPieHelpFormatter

def test_invalid_input():
    with pytest.raises(TypeError):
        formatter = HTTPieHelpFormatter(max_help_position='not_an_int')
