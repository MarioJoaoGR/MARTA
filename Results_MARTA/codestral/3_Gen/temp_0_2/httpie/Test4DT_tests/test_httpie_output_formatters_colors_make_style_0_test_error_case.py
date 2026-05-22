
import pytest
from httpie.output.formatters.colors import make_style

@pytest.mark.parametrize("shade", [None, "invalid_shade"])
def test_error_case(shade):
    with pytest.raises(TypeError):
        make_style('MyStyle', {'Token.Keyword': "bold red", 'Token.Number': "green"}, shade)
