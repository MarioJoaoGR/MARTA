
import pytest
from flutes.multiproc import ForkingPickler
import pickle

def test_edge_cases():
    # Create an instance of ForkingPickler and check if it uses the highest protocol available
    pickler = ForkingPickler(protocol=pickle.HIGHEST_PROTOCOL)
    assert pickler._Pickler__protocol == pickle.HIGHEST_PROTOCOL

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_ForkingPickler___init___0_test_edge_cases
flutes/Test4DT_tests/test_flutes_multiproc_ForkingPickler___init___0_test_edge_cases.py:3:0: E0611: No name 'ForkingPickler' in module 'flutes.multiproc' (no-name-in-module)


"""