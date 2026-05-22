
import os
from httpie.cli.requestitems import load_text_file, KeyValueArg
from unittest.mock import patch

def test_invalid_path():
    with patch('httpie.cli.requestitems.os.path.expanduser') as mock_expanduser:
        mock_expanduser.side_effect = FileNotFoundError("File not found")
        
        arg = KeyValueArg(value="nonexistentfile.txt", orig="nonexistentfile.txt")
        
        with pytest.raises(ParseError) as excinfo:
            load_text_file(arg)
        
        assert str(excinfo.value) == "b'nonexistentfile.txt': File not found"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_cli_requestitems_load_text_file_0_test_invalid_path
httpie/Test4DT_tests_codestral/test_httpie_cli_requestitems_load_text_file_0_test_invalid_path.py:10:14: E1120: No value for argument 'key' in constructor call (no-value-for-parameter)
httpie/Test4DT_tests_codestral/test_httpie_cli_requestitems_load_text_file_0_test_invalid_path.py:10:14: E1120: No value for argument 'sep' in constructor call (no-value-for-parameter)
httpie/Test4DT_tests_codestral/test_httpie_cli_requestitems_load_text_file_0_test_invalid_path.py:12:13: E0602: Undefined variable 'pytest' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_cli_requestitems_load_text_file_0_test_invalid_path.py:12:27: E0602: Undefined variable 'ParseError' (undefined-variable)


"""