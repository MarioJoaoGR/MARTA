
from codetiming._timer import FloatArg  # Corrected import from the appropriate module
import pytest

@pytest.fixture
def float_arg_instance():
    return FloatArg()

def test_float_arg_call(float_arg_instance):
    class TimeConverter(FloatArg):
        def __call__(self, seconds: float) -> None:
            assert isinstance(seconds, float), "The argument should be a float"
            print(f"Time in seconds is {seconds}")
    
    converter = TimeConverter()
    converter(3600.0)  # This will output: "Time in seconds is 3600.0"
