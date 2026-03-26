
# Importing necessary modules and classes for testing
from pytutils.lazy.simple_import import NonLocal  # Corrected import path

def test_edge_case():
    """
    Test edge case for NonLocal class initialization.
    """
    # Arrange
    value = 10
    
    # Act
    nl = NonLocal(value)
    
    # Assert
    assert hasattr(nl, 'value'), "NonLocal instance should have a 'value' attribute."
    assert nl.value == value, f"Expected initial value to be {value}, but got {nl.value}."
