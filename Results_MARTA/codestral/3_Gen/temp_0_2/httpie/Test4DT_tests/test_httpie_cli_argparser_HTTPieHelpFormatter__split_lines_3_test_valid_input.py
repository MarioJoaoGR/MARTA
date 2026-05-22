
import pytest
from httpie.cli.argparser import HTTPieHelpFormatter

class TestHTTPieHelpFormatter:
    def test_valid_input(self):
        with pytest.raises(TypeError) as excinfo:
            formatter = HTTPieHelpFormatter(max_help_position=8)
        assert "HelpFormatter.__init__() missing 1 required positional argument: 'prog'" in str(excinfo.value)
