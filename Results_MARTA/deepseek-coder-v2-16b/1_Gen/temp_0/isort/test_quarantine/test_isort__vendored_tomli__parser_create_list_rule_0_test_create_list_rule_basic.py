
from isort._vendored.tomli._parser import create_list_rule
import pytest

def test_create_list_rule_basic():
    src = "[[example]]\nkey1 = 1\nkey2 = 2"
    pos = 0
    
    class OutputMock:
        def __init__(self):
            self.flags = FlagsMock()
            self.data = DataMock()
    
    class FlagsMock:
        FROZEN = False

        def is_(self, key, flag):
            return False  # Mock implementation for testing

        def unset_all(self, key):
            pass  # Mock implementation for testing
    
        def set(self, key, flag, recursive=False):
            pass  # Mock implementation for testing
    
    class DataMock:
        def append_nest_to_list(self, key):
            assert key == 'example'
            return None  # Mock implementation for testing

        def overwrite(self, key, value):
            raise KeyError("Can not overwrite a value")  # Mock implementation for testing
    
    with pytest.raises(Exception) as exc_info:
        new_pos, key = create_list_rule(src, pos, OutputMock())
    
    assert str(exc_info.value) == "Expected ']]' at the end of an array declaration"

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_create_list_rule_0_test_create_list_rule_basic.py F [100%]

=================================== FAILURES ===================================
_________________________ test_create_list_rule_basic __________________________

    def test_create_list_rule_basic():
        src = "[[example]]\nkey1 = 1\nkey2 = 2"
        pos = 0
    
        class OutputMock:
            def __init__(self):
                self.flags = FlagsMock()
                self.data = DataMock()
    
        class FlagsMock:
            FROZEN = False
    
            def is_(self, key, flag):
                return False  # Mock implementation for testing
    
            def unset_all(self, key):
                pass  # Mock implementation for testing
    
            def set(self, key, flag, recursive=False):
                pass  # Mock implementation for testing
    
        class DataMock:
            def append_nest_to_list(self, key):
                assert key == 'example'
                return None  # Mock implementation for testing
    
            def overwrite(self, key, value):
                raise KeyError("Can not overwrite a value")  # Mock implementation for testing
    
        with pytest.raises(Exception) as exc_info:
            new_pos, key = create_list_rule(src, pos, OutputMock())
    
>       assert str(exc_info.value) == "Expected ']]' at the end of an array declaration"
E       assert "assert ('exa... == 'example'" == "Expected ']]...y declaration"
E         
E         - Expected ']]' at the end of an array declaration
E         + assert ('example',) == 'example'

isort/Test4DT_tests/test_isort__vendored_tomli__parser_create_list_rule_0_test_create_list_rule_basic.py:37: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_create_list_rule_0_test_create_list_rule_basic.py::test_create_list_rule_basic
============================== 1 failed in 0.10s ===============================
"""