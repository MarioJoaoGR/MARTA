
import pytest
from dataclasses_json import mm  # Assuming this is the correct module path

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
            schema_f = SchemaF()  # Raises NotImplementedError because the class should not be instantiated directly.
        """
        super().__init__(*args, **kwargs)
        raise NotImplementedError("This class is a helper only and should not be inherited or instantiated.")

def test_inheritance_raises_exception():
    with pytest.raises(NotImplementedError):
        SchemaF()
