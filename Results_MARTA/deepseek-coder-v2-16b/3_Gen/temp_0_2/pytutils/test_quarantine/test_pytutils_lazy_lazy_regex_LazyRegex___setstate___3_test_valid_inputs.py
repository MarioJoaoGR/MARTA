
import pytest
from pytutils.lazy.lazy_regex import LazyRegex
import re

class TestLazyRegexSetstate:
    @pytest.mark.parametrize("pattern, flags", [
        ("hello", 0),
        ("world.*", re.DOTALL),
        (r"\d+", re.IGNORECASE),
        ("example(?:pattern)", re.VERBOSE)
    ])
    def test_valid_inputs(self, pattern, flags):
        lazy_regex = LazyRegex(args=(pattern,), kwargs={"flags": flags})
        
        # Check if the pattern and flags are correctly set
        assert lazy_regex._regex_args[0] == pattern
        assert lazy_regex._regex_kwargs["flags"] == flags
        
        # Accessing a regex attribute should trigger compilation
        with pytest.raises(AttributeError):
            _ = lazy_regex._real_regex

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___setstate___3_test_valid_inputs.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_______________ TestLazyRegexSetstate.test_valid_inputs[hello-0] _______________

self = <Test4DT_tests.test_pytutils_lazy_lazy_regex_LazyRegex___setstate___3_test_valid_inputs.TestLazyRegexSetstate object at 0x7fc1149a9210>
pattern = 'hello', flags = 0

    @pytest.mark.parametrize("pattern, flags", [
        ("hello", 0),
        ("world.*", re.DOTALL),
        (r"\d+", re.IGNORECASE),
        ("example(?:pattern)", re.VERBOSE)
    ])
    def test_valid_inputs(self, pattern, flags):
        lazy_regex = LazyRegex(args=(pattern,), kwargs={"flags": flags})
    
        # Check if the pattern and flags are correctly set
        assert lazy_regex._regex_args[0] == pattern
        assert lazy_regex._regex_kwargs["flags"] == flags
    
        # Accessing a regex attribute should trigger compilation
>       with pytest.raises(AttributeError):
E       Failed: DID NOT RAISE <class 'AttributeError'>

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___setstate___3_test_valid_inputs.py:21: Failed
__________ TestLazyRegexSetstate.test_valid_inputs[world.*-re.DOTALL] __________

self = <Test4DT_tests.test_pytutils_lazy_lazy_regex_LazyRegex___setstate___3_test_valid_inputs.TestLazyRegexSetstate object at 0x7fc1148357d0>
pattern = 'world.*', flags = re.DOTALL

    @pytest.mark.parametrize("pattern, flags", [
        ("hello", 0),
        ("world.*", re.DOTALL),
        (r"\d+", re.IGNORECASE),
        ("example(?:pattern)", re.VERBOSE)
    ])
    def test_valid_inputs(self, pattern, flags):
        lazy_regex = LazyRegex(args=(pattern,), kwargs={"flags": flags})
    
        # Check if the pattern and flags are correctly set
        assert lazy_regex._regex_args[0] == pattern
        assert lazy_regex._regex_kwargs["flags"] == flags
    
        # Accessing a regex attribute should trigger compilation
>       with pytest.raises(AttributeError):
E       Failed: DID NOT RAISE <class 'AttributeError'>

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___setstate___3_test_valid_inputs.py:21: Failed
_________ TestLazyRegexSetstate.test_valid_inputs[\\d+-re.IGNORECASE] __________

self = <Test4DT_tests.test_pytutils_lazy_lazy_regex_LazyRegex___setstate___3_test_valid_inputs.TestLazyRegexSetstate object at 0x7fc114834c50>
pattern = '\\d+', flags = re.IGNORECASE

    @pytest.mark.parametrize("pattern, flags", [
        ("hello", 0),
        ("world.*", re.DOTALL),
        (r"\d+", re.IGNORECASE),
        ("example(?:pattern)", re.VERBOSE)
    ])
    def test_valid_inputs(self, pattern, flags):
        lazy_regex = LazyRegex(args=(pattern,), kwargs={"flags": flags})
    
        # Check if the pattern and flags are correctly set
        assert lazy_regex._regex_args[0] == pattern
        assert lazy_regex._regex_kwargs["flags"] == flags
    
        # Accessing a regex attribute should trigger compilation
>       with pytest.raises(AttributeError):
E       Failed: DID NOT RAISE <class 'AttributeError'>

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___setstate___3_test_valid_inputs.py:21: Failed
____ TestLazyRegexSetstate.test_valid_inputs[example(?:pattern)-re.VERBOSE] ____

self = <Test4DT_tests.test_pytutils_lazy_lazy_regex_LazyRegex___setstate___3_test_valid_inputs.TestLazyRegexSetstate object at 0x7fc1148368d0>
pattern = 'example(?:pattern)', flags = re.VERBOSE

    @pytest.mark.parametrize("pattern, flags", [
        ("hello", 0),
        ("world.*", re.DOTALL),
        (r"\d+", re.IGNORECASE),
        ("example(?:pattern)", re.VERBOSE)
    ])
    def test_valid_inputs(self, pattern, flags):
        lazy_regex = LazyRegex(args=(pattern,), kwargs={"flags": flags})
    
        # Check if the pattern and flags are correctly set
        assert lazy_regex._regex_args[0] == pattern
        assert lazy_regex._regex_kwargs["flags"] == flags
    
        # Accessing a regex attribute should trigger compilation
>       with pytest.raises(AttributeError):
E       Failed: DID NOT RAISE <class 'AttributeError'>

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___setstate___3_test_valid_inputs.py:21: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___setstate___3_test_valid_inputs.py::TestLazyRegexSetstate::test_valid_inputs[hello-0]
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___setstate___3_test_valid_inputs.py::TestLazyRegexSetstate::test_valid_inputs[world.*-re.DOTALL]
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___setstate___3_test_valid_inputs.py::TestLazyRegexSetstate::test_valid_inputs[\\d+-re.IGNORECASE]
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_LazyRegex___setstate___3_test_valid_inputs.py::TestLazyRegexSetstate::test_valid_inputs[example(?:pattern)-re.VERBOSE]
============================== 4 failed in 0.07s ===============================
"""