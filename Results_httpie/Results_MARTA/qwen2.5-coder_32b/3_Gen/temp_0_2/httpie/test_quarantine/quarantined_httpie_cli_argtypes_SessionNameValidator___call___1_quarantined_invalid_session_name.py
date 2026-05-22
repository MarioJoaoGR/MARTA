
import pytest
from unittest.mock import patch
from httpie.cli.argtypes import SessionNameValidator

def test_invalid_session_name():
    validator = SessionNameValidator("Invalid session name")
    
    with pytest.raises(argparse.ArgumentError) as excinfo:
        validator("my/session")
        
    assert str(excinfo.value) == "Invalid session name"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_cli_argtypes_SessionNameValidator___call___1_test_invalid_session_name
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argtypes_SessionNameValidator___call___1_test_invalid_session_name.py:9:23: E0602: Undefined variable 'argparse' (undefined-variable)


"""