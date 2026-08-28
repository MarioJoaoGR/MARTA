
import pytest
from ansible.module_utils.common.text.converters import to_text



def test_nonstring_passthru():
    with pytest.raises(TypeError):
        to_text({'key': 'value'}, nonstring='strict')