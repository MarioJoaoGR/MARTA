
import pytest
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional, List, Dict, Any

# Assuming SchemaF is defined somewhere in your module 'dataclasses_json.mm'
# from dataclasses_json.mm import SchemaF

@dataclass_json
@dataclass
class SchemaF:
    """Lift Schema into a type constructor"""
    
    def __init__(self, *args, **kwargs):
        """
        Raises exception because this class should not be inherited. This class is helper only.
        """
        super().__init__(*args, **kwargs)
        raise NotImplementedError()

# Test case for the edge case scenario
def test_edge_case():
    with pytest.raises(NotImplementedError):
        schema = SchemaF()  # This should raise an error because __init__ is not meant to be called directly
