
import pytest
from isort._vendored.tomli._parser import Flags

def test_set_flag():
    flags = Flags()
    flags.set("a.b.c", Flags.EXPLICIT_NEST, recursive=True)
    assert "a" in flags._flags and "b" in flags._flags["a"] and "c" in flags._flags["a"]["b"]

def test_set_flag_non_recursive():
    flags = Flags()
    flags.set("a.b.c", Flags.FROZEN, recursive=False)
    assert "a" in flags._flags and "b" in flags._flags["a"] and "c" in flags._flags["a"]["b"]

def test_set_flag_multiple():
    flags = Flags()
    flags.set("a.b.c", Flags.EXPLICIT_NEST, recursive=True)
    flags.set("a.b.c", Flags.FROZEN, recursive=False)
    assert "a" in flags._flags and "b" in flags._flags["a"] and "c" in flags._flags["a"]["b"]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_1_test_edge_case.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
________________________________ test_set_flag _________________________________

    def test_set_flag():
        flags = Flags()
        flags.set("a.b.c", Flags.EXPLICIT_NEST, recursive=True)
>       assert "a" in flags._flags and "b" in flags._flags["a"] and "c" in flags._flags["a"]["b"]
E       AssertionError: assert ('a' in {'a': {'flags': set(), 'nested': {'.': {'flags': set(), 'nested': {'b': {'flags': set(), 'nested': {...}, 'recursive_flags': set()}}, 'recursive_flags': set()}}, 'recursive_flags': set()}} and 'b' in {'flags': set(), 'nested': {'.': {'flags': set(), 'nested': {'b': {'flags': set(), 'nested': {'.': {...}}, 'recursive_flags': set()}}, 'recursive_flags': set()}}, 'recursive_flags': set()})
E        +  where {'a': {'flags': set(), 'nested': {'.': {'flags': set(), 'nested': {'b': {'flags': set(), 'nested': {...}, 'recursive_flags': set()}}, 'recursive_flags': set()}}, 'recursive_flags': set()}} = <isort._vendored.tomli._parser.Flags object at 0x7ff8c884c590>._flags

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_1_test_edge_case.py:8: AssertionError
_________________________ test_set_flag_non_recursive __________________________

    def test_set_flag_non_recursive():
        flags = Flags()
        flags.set("a.b.c", Flags.FROZEN, recursive=False)
>       assert "a" in flags._flags and "b" in flags._flags["a"] and "c" in flags._flags["a"]["b"]
E       AssertionError: assert ('a' in {'a': {'flags': set(), 'nested': {'.': {'flags': set(), 'nested': {'b': {'flags': set(), 'nested': {...}, 'recursive_flags': set()}}, 'recursive_flags': set()}}, 'recursive_flags': set()}} and 'b' in {'flags': set(), 'nested': {'.': {'flags': set(), 'nested': {'b': {'flags': set(), 'nested': {'.': {...}}, 'recursive_flags': set()}}, 'recursive_flags': set()}}, 'recursive_flags': set()})
E        +  where {'a': {'flags': set(), 'nested': {'.': {'flags': set(), 'nested': {'b': {'flags': set(), 'nested': {...}, 'recursive_flags': set()}}, 'recursive_flags': set()}}, 'recursive_flags': set()}} = <isort._vendored.tomli._parser.Flags object at 0x7ff8c884eb90>._flags

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_1_test_edge_case.py:13: AssertionError
____________________________ test_set_flag_multiple ____________________________

    def test_set_flag_multiple():
        flags = Flags()
        flags.set("a.b.c", Flags.EXPLICIT_NEST, recursive=True)
        flags.set("a.b.c", Flags.FROZEN, recursive=False)
>       assert "a" in flags._flags and "b" in flags._flags["a"] and "c" in flags._flags["a"]["b"]
E       AssertionError: assert ('a' in {'a': {'flags': set(), 'nested': {'.': {'flags': set(), 'nested': {'b': {'flags': set(), 'nested': {...}, 'recursive_flags': set()}}, 'recursive_flags': set()}}, 'recursive_flags': set()}} and 'b' in {'flags': set(), 'nested': {'.': {'flags': set(), 'nested': {'b': {'flags': set(), 'nested': {'.': {...}}, 'recursive_flags': set()}}, 'recursive_flags': set()}}, 'recursive_flags': set()})
E        +  where {'a': {'flags': set(), 'nested': {'.': {'flags': set(), 'nested': {'b': {'flags': set(), 'nested': {...}, 'recursive_flags': set()}}, 'recursive_flags': set()}}, 'recursive_flags': set()}} = <isort._vendored.tomli._parser.Flags object at 0x7ff8c883f2d0>._flags

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_1_test_edge_case.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_1_test_edge_case.py::test_set_flag
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_1_test_edge_case.py::test_set_flag_non_recursive
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_1_test_edge_case.py::test_set_flag_multiple
============================== 3 failed in 0.11s ===============================
"""