
import pytest
from flutes.structure import no_map_instance

def test_none_input():
    invalid_instance = None
    with pytest.raises(TypeError):
        no_map_instance(invalid_instance)
