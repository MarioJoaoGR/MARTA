
import pytest
from httpie.cli.argparser import HTTPieManagerArgumentParser
from unittest.mock import patch, MagicMock

def test_parse_known_args():
    parser = HTTPieManagerArgumentParser()
    
    # Test with known arguments
    args = ['--config', 'settings.cfg']
    parsed_args, unknown_args = parser.parse_known_args(args)
    assert parsed_args.config == 'settings.cfg'
    assert unknown_args == []

    # Test with unknown argument
    args = ['--unknown-arg', 'value']
    with pytest.raises(argparse.ArgumentError):
        parser.parse_known_args(args)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_cli_argparser_HTTPieManagerArgumentParser_parse_known_args_2_test_edge_cases
httpie/Test4DT_tests_codestral/test_httpie_cli_argparser_HTTPieManagerArgumentParser_parse_known_args_2_test_edge_cases.py:17:23: E0602: Undefined variable 'argparse' (undefined-variable)


"""