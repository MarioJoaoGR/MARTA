
import pytest
from ansible.module_utils.common.arg_spec import ModuleArgumentSpecValidator

def test_init_without_args():
    with pytest.raises(TypeError):
        validator = ModuleArgumentSpecValidator()
