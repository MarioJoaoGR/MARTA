
import pytest
from pysnooper.utils import WritableStream

# Test valid input scenario

# Test missing method scenario
class ClassCWithoutWrite:
    pass

@pytest.fixture
def class_c_without_write():
    return ClassCWithoutWrite()

def test_missing_method(class_c_without_write):
    with pytest.raises(AttributeError):
        class_c_without_write.write("Hello, world!")

# Test invalid input scenario
def test_invalid_input():
    with pytest.raises(TypeError):
        WritableStream().write("Hello, world!")