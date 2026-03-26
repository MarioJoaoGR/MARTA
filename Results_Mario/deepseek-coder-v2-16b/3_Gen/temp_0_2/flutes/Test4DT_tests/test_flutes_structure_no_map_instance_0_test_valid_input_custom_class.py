
import pytest
from flutes.structure import no_map_instance, _NO_MAP_INSTANCE_ATTR  # Assuming this is the correct module path

@pytest.fixture
def custom_class():
    class MyClass:
        def __init__(self, value):
            self.value = value
    return MyClass(10)

def test_valid_input_custom_class(custom_class):
    no_map_instance(custom_class)
    assert hasattr(custom_class, _NO_MAP_INSTANCE_ATTR)
