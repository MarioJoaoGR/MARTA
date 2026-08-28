
import pytest
from ansible.context import _init_global_context
from ansible.utils.context_objects import GlobalCLIArgs


def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Attempt to initialize the global context with an invalid type for options
        _init_global_context({'verbose': True, 'output_format': 'json', 'loglevel': 123})