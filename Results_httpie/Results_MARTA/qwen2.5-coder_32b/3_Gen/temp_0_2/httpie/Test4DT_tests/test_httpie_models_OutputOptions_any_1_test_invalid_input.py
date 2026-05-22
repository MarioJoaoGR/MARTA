
import pytest
from httpie.models import OutputOptions, RequestsMessageKind

def test_invalid_input():
    with pytest.raises(TypeError):
        options = OutputOptions()  # Missing arguments for headers, body, and meta
        assert not options.any()
