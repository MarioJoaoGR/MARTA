
import pytest
from flutes.iterator import LazyList  # Adjust this import based on actual module path

def test_error_case():
    with pytest.raises(TypeError):
        # This will raise an error because the constructor expects an iterable, not a specific type like int
        lazy_list = LazyList(12345)
