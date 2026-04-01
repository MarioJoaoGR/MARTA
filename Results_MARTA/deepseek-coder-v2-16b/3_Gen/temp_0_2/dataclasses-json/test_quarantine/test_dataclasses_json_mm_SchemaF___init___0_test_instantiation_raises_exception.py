
from dataclasses_json import mm  # Importing from dataclasses-json module
import pytest

class SchemaF(metaclass=mm.Schema):
    """Lift Schema into a type constructor"""
    
    def __init__(self, *args, **kwargs):
        """
        Raises an exception because this class should not be inherited. This class is helper only.
        
        Args:
            None (This function does not accept any parameters)
        
        Returns:
            Nothing (The function does not return anything)
        
        Example:
            schema_f = SchemaF()
            # Raises NotImplementedError because the class should not be instantiated directly.
        
        Note:
            This class is intended to be used as a base or helper class and should not be instantiated directly.
        """
        super().__init__(*args, **kwargs)
        raise NotImplementedError()

def test_instantiation_raises_exception():
    with pytest.raises(NotImplementedError):
        SchemaF()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_SchemaF___init___0_test_instantiation_raises_exception
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF___init___0_test_instantiation_raises_exception.py:5:0: E1139: Invalid metaclass 'Schema' used (invalid-metaclass)


"""