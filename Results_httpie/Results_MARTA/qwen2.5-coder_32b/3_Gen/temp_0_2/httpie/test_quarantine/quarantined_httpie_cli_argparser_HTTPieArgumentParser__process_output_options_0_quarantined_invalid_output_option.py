
import pytest
from unittest.mock import patch
from httpie.cli.argparser import HTTPieArgumentParser

@pytest.fixture
def parser():
    return HTTPieArgumentParser()

def test_invalid_output_option(parser):
    with patch('sys.stderr', new=StringIO()) as mock_stderr:
        # Test invalid output option
        with pytest.raises(SystemExit) as excinfo:
            parser.parse_args(['--print', 'invalid'])
        assert str(excinfo.value) == "usage: -p"
        
        # Check that the error message includes the invalid option
        assert "invalid output option: --print=invalid" in mock_stderr.getvalue()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_cli_argparser_HTTPieArgumentParser__process_output_options_0_test_invalid_output_option
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argparser_HTTPieArgumentParser__process_output_options_0_test_invalid_output_option.py:11:33: E0602: Undefined variable 'StringIO' (undefined-variable)


"""