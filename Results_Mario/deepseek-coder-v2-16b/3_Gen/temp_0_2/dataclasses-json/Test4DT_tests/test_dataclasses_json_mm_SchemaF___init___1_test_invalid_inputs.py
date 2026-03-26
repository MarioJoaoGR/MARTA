
from dataclasses_json import mm  # Importing from dataclasses_json.mm as per the error message hint
import pytest

class SchemaF:
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

def test_invalid_inputs():
    with pytest.raises(NotImplementedError):
        SchemaF()
