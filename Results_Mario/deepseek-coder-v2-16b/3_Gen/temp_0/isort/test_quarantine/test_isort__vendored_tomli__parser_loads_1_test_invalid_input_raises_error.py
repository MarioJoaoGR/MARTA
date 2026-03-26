
import pytest
from isort._vendored.tomli._parser import loads

def test_invalid_input_raises_error():
    malformed_toml = 'invalid toml'
    with pytest.raises(Exception) as e:
        loads(malformed_toml)
    assert str(e.value).startswith("Invalid statement")

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_loads_1_test_invalid_input_raises_error.py F [100%]

=================================== FAILURES ===================================
_______________________ test_invalid_input_raises_error ________________________

    def test_invalid_input_raises_error():
        malformed_toml = 'invalid toml'
        with pytest.raises(Exception) as e:
            loads(malformed_toml)
>       assert str(e.value).startswith("Invalid statement")
E       assert False
E        +  where False = <built-in method startswith of str object at 0x7f6456f6d930>('Invalid statement')
E        +    where <built-in method startswith of str object at 0x7f6456f6d930> = 'Expected "=" after a key in a key/value pair (at line 1, column 9)'.startswith
E        +      where 'Expected "=" after a key in a key/value pair (at line 1, column 9)' = str(TOMLDecodeError('Expected "=" after a key in a key/value pair (at line 1, column 9)'))
E        +        where TOMLDecodeError('Expected "=" after a key in a key/value pair (at line 1, column 9)') = <ExceptionInfo TOMLDecodeError('Expected "=" after a key in a key/value pair (at line 1, column 9)') tblen=4>.value

isort/Test4DT_tests/test_isort__vendored_tomli__parser_loads_1_test_invalid_input_raises_error.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_loads_1_test_invalid_input_raises_error.py::test_invalid_input_raises_error
============================== 1 failed in 0.13s ===============================
"""