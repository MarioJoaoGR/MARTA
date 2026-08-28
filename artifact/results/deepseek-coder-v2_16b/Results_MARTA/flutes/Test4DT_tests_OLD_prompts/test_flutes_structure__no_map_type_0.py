
import pytest
from typing import Type, List
from flutes.structure import _no_map_type, _NO_MAP_INSTANCE_ATTR



def test_invalid_input():
    from typing import List
    with pytest.raises(TypeError):
        _no_map_type(List)