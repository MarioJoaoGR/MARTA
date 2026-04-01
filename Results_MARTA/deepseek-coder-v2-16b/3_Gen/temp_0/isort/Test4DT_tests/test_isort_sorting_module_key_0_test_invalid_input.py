
import pytest

from isort.sorting import Config, module_key


def test_invalid_input():
    with pytest.raises(TypeError):
        # Test invalid input by passing None as the module name
        module_key(None, Config())
