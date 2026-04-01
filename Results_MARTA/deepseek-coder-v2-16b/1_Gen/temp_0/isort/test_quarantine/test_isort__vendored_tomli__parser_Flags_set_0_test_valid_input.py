
import pytest
from isort._vendored.tomli._parser import Flags

def test_valid_input():
    flags = Flags()
    
    # Test setting a flag non-recursively
    flags.set('a', Flags.EXPLICIT_NEST, recursive=False)
    assert 'a' in flags._flags and Flags.EXPLICIT_NEST in flags._flags['a']['flags']
    
    # Test setting a flag recursively
    flags.set('b/c/d', Flags.FROZEN, recursive=True)
    assert 'b' in flags._flags and 'c' in flags._flags['b']['nested'] and 'd' in flags._flags['b']['nested']['c']['nested']

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        flags = Flags()
    
        # Test setting a flag non-recursively
        flags.set('a', Flags.EXPLICIT_NEST, recursive=False)
        assert 'a' in flags._flags and Flags.EXPLICIT_NEST in flags._flags['a']['flags']
    
        # Test setting a flag recursively
        flags.set('b/c/d', Flags.FROZEN, recursive=True)
>       assert 'b' in flags._flags and 'c' in flags._flags['b']['nested'] and 'd' in flags._flags['b']['nested']['c']['nested']
E       AssertionError: assert ('b' in {'a': {'flags': {1}, 'nested': {}, 'recursive_flags': set()}, 'b': {'flags': set(), 'nested': {'/': {'flags': set(), '...': {'flags': set(), 'nested': {...}, 'recursive_flags': set()}}, 'recursive_flags': set()}}, 'recursive_flags': set()}} and 'c' in {'/': {'flags': set(), 'nested': {'c': {'flags': set(), 'nested': {'/': {'flags': set(), 'nested': {...}, 'recursive_flags': set()}}, 'recursive_flags': set()}}, 'recursive_flags': set()}})
E        +  where {'a': {'flags': {1}, 'nested': {}, 'recursive_flags': set()}, 'b': {'flags': set(), 'nested': {'/': {'flags': set(), '...': {'flags': set(), 'nested': {...}, 'recursive_flags': set()}}, 'recursive_flags': set()}}, 'recursive_flags': set()}} = <isort._vendored.tomli._parser.Flags object at 0x7f3febf8fc10>._flags

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_0_test_valid_input.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""