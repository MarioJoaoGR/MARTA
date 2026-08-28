
import pytest
from ansible.vars.manager import VarsWithSources

def test_basic_usage():
    # Create an instance with initial data
    vs = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    
    # Access a variable's value and its source (debug message will be printed)
    assert str(vs['var1']) == "source1"  # Assuming the __str__ method returns the source information


def test_setitem_method():
    # Create an instance with initial data
    vs = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
    
    # Use setitem to add a new variable
    vs['var3'] = 'source3'
    
    # Access the newly added variable to see its value and source information
    assert str(vs['var3']) == "source3"  # Assuming the __str__ method returns the value and source information