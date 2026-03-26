
# Module: flutes.multiproc
import pytest
import pickle
from flutes.multiproc import ForkingPickler  # Fixed import statement

# Test default initialization of ForkingPickler
def test_default_initialization():
    with open('test_data.pkl', 'wb') as file:
        forked_pickler = ForkingPickler(file)
    assert isinstance(forked_pickler, ForkingPickler), "Initialization should create an instance of ForkingPickler"  # Fixed assertion message

# Test initialization with explicit protocol specification
def test_explicit_protocol_specification():
    with open('test_data.pkl', 'wb') as file:
        forked_pickler = ForkingPickler(file, protocol=pickle.DEFAULT_PROTOCOL)
    assert isinstance(forked_pickler, ForkingPickler), "Initialization should create an instance of ForkingPickler"  # Fixed assertion message

# Test default initialization with no arguments (should use highest protocol)
def test_default_initialization_no_args():
    with open('test_data.pkl', 'wb') as file:
        forked_pickler = ForkingPickler(file)
    assert forked_pickler._protocol == pickle.HIGHEST_PROTOCOL, "Default initialization should use the highest protocol"  # Fixed assertion message

# Test initialization with a specific protocol (should override and use highest protocol)
def test_specific_protocol():
    with open('test_data.pkl', 'wb') as file:
        forked_pickler = ForkingPickler(file, protocol=pickle.DEFAULT_PROTOCOL)
    assert forked_pickler._protocol == pickle.HIGHEST_PROTOCOL, "Explicit protocol specification should be overridden to use the highest protocol"  # Fixed assertion message

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_ForkingPickler___init___0
flutes/Test4DT_tests/test_flutes_multiproc_ForkingPickler___init___0.py:5:0: E0611: No name 'ForkingPickler' in module 'flutes.multiproc' (no-name-in-module)


"""