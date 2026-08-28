
import pytest
from dataclasses_json import mm
from dataclasses import dataclass

# Define a simple dataclass for demonstration
@dataclass
class ExampleDataclass:
    id: int
    name: str

# Test the SchemaF class initialization
def test_schemaf_initialization():
    with pytest.raises(NotImplementedError):
        schema = mm.SchemaF()
