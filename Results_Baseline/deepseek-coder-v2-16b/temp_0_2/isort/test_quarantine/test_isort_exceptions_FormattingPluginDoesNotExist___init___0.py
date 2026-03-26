
# Module: isort.exceptions
# test_exceptions.py
from isort.exceptions import FormattingPluginDoesNotExist
import pytest

def test_formattingplugindoesnotexist_init():
    with pytest.raises(FormattingPluginDoesNotExist) as exc_info:
        raise FormattingPluginDoesNotExist("json_formatter")
    assert str(exc_info.value) == "Specified formatting plugin of json_formatter does not exist."

def test_formattingplugindoesnotexist_init_with_custom_message():
    with pytest.raises(FormattingPluginDoesNotExist) as exc_info:
        raise FormattingPluginDoesNotExist("xml_formatter")
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort_exceptions_FormattingPluginDoesNotExist___init___0.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
____________________ test_formattingplugindoesnotexist_init ____________________

    def test_formattingplugindoesnotexist_init():
        with pytest.raises(FormattingPluginDoesNotExist) as exc_info:
            raise FormattingPluginDoesNotExist("json_formatter")
>       assert str(exc_info.value) == "Specified formatting plugin of json_formatter does not exist."
E       AssertionError: assert 'Specified fo...s not exist. ' == 'Specified fo...es not exist.'
E         
E         Skipping 50 identical leading characters in diff, use -v to show
E         -  not exist.
E         +  not exist. 
E         ?            +

isort/Test4DT_tests/test_isort_exceptions_FormattingPluginDoesNotExist___init___0.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_FormattingPluginDoesNotExist___init___0.py::test_formattingplugindoesnotexist_init
========================= 1 failed, 1 passed in 0.09s ==========================
"""