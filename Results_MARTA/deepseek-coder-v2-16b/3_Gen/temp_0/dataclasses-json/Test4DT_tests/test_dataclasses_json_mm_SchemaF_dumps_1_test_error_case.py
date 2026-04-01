
import pytest
from dataclasses_json import mm  # Assuming this is the correct module for your test case

class SchemaF:
    """Lift Schema into a type constructor"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        raise NotImplementedError("This class is a helper only and should not be inherited or instantiated.")

def test_error_case():
    with pytest.raises(NotImplementedError):
        schema_f = SchemaF()  # This should raise the NotImplementedError
