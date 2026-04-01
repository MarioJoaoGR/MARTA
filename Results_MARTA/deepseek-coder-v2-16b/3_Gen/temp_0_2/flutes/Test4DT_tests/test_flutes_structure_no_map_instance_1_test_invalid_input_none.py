
import pytest
from flutes.structure import no_map_instance, _NO_MAP_INSTANCE_ATTR

def test_invalid_input_none():
    my_none = None
    with pytest.raises(TypeError):
        no_map_instance(my_none)
