
import pytest
from flutes.multiproc import FuncWrapper

def my_function(key, value):
    return key + value

class TestFuncWrapper:
    
    def test_edge_cases(self):
        func_wrapper = FuncWrapper(my_function, (1, 2), {'key': 'value'})
        
        # Test with None values
        with pytest.raises(TypeError) as excinfo:
            assert func_wrapper(None, None) == 3
        assert str(excinfo.value) == "my_function() got multiple values for argument 'key'"
