
import pytest
from unittest.mock import patch
from string_utils.manipulation import __RomanNumbers

@pytest.mark.parametrize("input_string, expected", [('IX', 9), ('XIV', 14), ('MMXVII', 2017)])
def test_valid_case(input_string, expected):
    with patch.object(__RomanNumbers, '__index_for_sign', return_value=0):
        assert __RomanNumbers().decode(input_string) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers_decode_0_test_valid_case.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
____________________________ test_valid_case[IX-9] _____________________________

input_string = 'IX', expected = 9

    @pytest.mark.parametrize("input_string, expected", [('IX', 9), ('XIV', 14), ('MMXVII', 2017)])
    def test_valid_case(input_string, expected):
>       with patch.object(__RomanNumbers, '__index_for_sign', return_value=0):

python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers_decode_0_test_valid_case.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/unittest/mock.py:1447: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x102944cd0>

    def get_original(self):
        target = self.getter()
        name = self.attribute
    
        original = DEFAULT
        local = False
    
        try:
            original = target.__dict__[name]
        except (AttributeError, KeyError):
            original = getattr(target, name, DEFAULT)
        else:
            local = True
    
        if name in _builtins and isinstance(target, ModuleType):
            self.create = True
    
        if not self.create and original is DEFAULT:
>           raise AttributeError(
                "%s does not have the attribute %r" % (target, name)
            )
E           AttributeError: <class 'string_utils.manipulation.__RomanNumbers'> does not have the attribute '__index_for_sign'

/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/unittest/mock.py:1420: AttributeError
___________________________ test_valid_case[XIV-14] ____________________________

input_string = 'XIV', expected = 14

    @pytest.mark.parametrize("input_string, expected", [('IX', 9), ('XIV', 14), ('MMXVII', 2017)])
    def test_valid_case(input_string, expected):
>       with patch.object(__RomanNumbers, '__index_for_sign', return_value=0):

python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers_decode_0_test_valid_case.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/unittest/mock.py:1447: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x1028af8e0>

    def get_original(self):
        target = self.getter()
        name = self.attribute
    
        original = DEFAULT
        local = False
    
        try:
            original = target.__dict__[name]
        except (AttributeError, KeyError):
            original = getattr(target, name, DEFAULT)
        else:
            local = True
    
        if name in _builtins and isinstance(target, ModuleType):
            self.create = True
    
        if not self.create and original is DEFAULT:
>           raise AttributeError(
                "%s does not have the attribute %r" % (target, name)
            )
E           AttributeError: <class 'string_utils.manipulation.__RomanNumbers'> does not have the attribute '__index_for_sign'

/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/unittest/mock.py:1420: AttributeError
_________________________ test_valid_case[MMXVII-2017] _________________________

input_string = 'MMXVII', expected = 2017

    @pytest.mark.parametrize("input_string, expected", [('IX', 9), ('XIV', 14), ('MMXVII', 2017)])
    def test_valid_case(input_string, expected):
>       with patch.object(__RomanNumbers, '__index_for_sign', return_value=0):

python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers_decode_0_test_valid_case.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/unittest/mock.py:1447: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x10309ba60>

    def get_original(self):
        target = self.getter()
        name = self.attribute
    
        original = DEFAULT
        local = False
    
        try:
            original = target.__dict__[name]
        except (AttributeError, KeyError):
            original = getattr(target, name, DEFAULT)
        else:
            local = True
    
        if name in _builtins and isinstance(target, ModuleType):
            self.create = True
    
        if not self.create and original is DEFAULT:
>           raise AttributeError(
                "%s does not have the attribute %r" % (target, name)
            )
E           AttributeError: <class 'string_utils.manipulation.__RomanNumbers'> does not have the attribute '__index_for_sign'

/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/unittest/mock.py:1420: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers_decode_0_test_valid_case.py::test_valid_case[IX-9]
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers_decode_0_test_valid_case.py::test_valid_case[XIV-14]
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers_decode_0_test_valid_case.py::test_valid_case[MMXVII-2017]
============================== 3 failed in 0.11s ===============================
"""