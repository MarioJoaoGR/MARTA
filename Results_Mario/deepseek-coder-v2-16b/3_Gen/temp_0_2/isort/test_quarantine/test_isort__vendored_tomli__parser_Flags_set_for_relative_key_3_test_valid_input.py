
import pytest
from isort._vendored.tomli._parser import Flags

def test_set_for_relative_key():
    flags = Flags()
    
    # Test setting a flag in an empty structure
    head_key = ["a"]
    rel_key = ["b", "c"]
    flags.set_for_relative_key(head_key, rel_key, Flags.EXPLICIT_NEST)
    assert flags._flags == {"a": {"nested": {"b": {"nested": {"c": {"flags": {Flags.EXPLICIT_NEST}, "recursive_flags": set(), "nested": {}}}}}}}
    
    # Test setting a flag in an already existing structure
    head_key = ["x"]
    rel_key = ["y", "z"]
    flags.set_for_relative_key(head_key, rel_key, Flags.FROZEN)
    assert flags._flags == {"a": {"nested": {"b": {"nested": {"c": {"flags": {Flags.EXPLICIT_NEST}, "recursive_flags": set(), "nested": {}}}}}}, "x": {"nested": {"y": {"nested": {"z": {"flags": {Flags.FROZEN}, "recursive_flags": set(), "nested": {}}}}}}}
    
    # Test setting a flag in a non-existing path
    head_key = ["m"]
    rel_key = ["n", "o"]
    flags.set_for_relative_key(head_key, rel_key, Flags.EXPLICIT_NEST)
    assert flags._flags == {"a": {"nested": {"b": {"nested": {"c": {"flags": {Flags.EXPLICIT_NEST}, "recursive_flags": set(), "nested": {}}}}}}, "x": {"nested": {"y": {"nested": {"z": {"flags": {Flags.FROZEN}, "recursive_flags": set(), "nested": {}}}}}}, "m": {"nested": {"n": {"nested": {"o": {"flags": {Flags.EXPLICIT_NEST}, "recursive_flags": set(), "nested": {}}}}}}}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_for_relative_key_3_test_valid_input.py F [100%]

=================================== FAILURES ===================================
__________________________ test_set_for_relative_key ___________________________

    def test_set_for_relative_key():
        flags = Flags()
    
        # Test setting a flag in an empty structure
        head_key = ["a"]
        rel_key = ["b", "c"]
        flags.set_for_relative_key(head_key, rel_key, Flags.EXPLICIT_NEST)
>       assert flags._flags == {"a": {"nested": {"b": {"nested": {"c": {"flags": {Flags.EXPLICIT_NEST}, "recursive_flags": set(), "nested": {}}}}}}}
E       AssertionError: assert {'a': {'flags...lags': set()}} == {'a': {'neste...': set()}}}}}}
E         
E         Differing items:
E         {'a': {'flags': set(), 'nested': {'b': {'flags': {1}, 'nested': {'c': {'flags': {...}, 'nested': {}, 'recursive_flags': set()}}, 'recursive_flags': set()}}, 'recursive_flags': set()}} != {'a': {'nested': {'b': {'nested': {'c': {'flags': {...}, 'nested': {}, 'recursive_flags': set()}}}}}}
E         Use -v to get more diff

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_for_relative_key_3_test_valid_input.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_for_relative_key_3_test_valid_input.py::test_set_for_relative_key
============================== 1 failed in 0.14s ===============================
"""