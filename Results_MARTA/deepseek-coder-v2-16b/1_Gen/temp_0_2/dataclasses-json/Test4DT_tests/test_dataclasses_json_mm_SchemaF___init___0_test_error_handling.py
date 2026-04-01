
import pytest
from dataclasses_json import mm  # Assuming this is the correct module for SchemaF and its methods

class SchemaF:
    """Lift Schema into a type constructor"""
    
    def __init__(self, *args, **kwargs):
        """
        Raises an exception because this class should not be inherited. This class is helper only.
        
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
            
        Raises:
            NotImplementedError: Always raised to indicate that the class should not be instantiated directly.
        """
        super().__init__(*args, **kwargs)
        raise NotImplementedError()

def test_error_handling():
    with pytest.raises(NotImplementedError):
        SchemaF()
