
import pytest
from httpie.cli.argparser import HTTPieArgumentParser

def test_apply_no_options_invalid():
    parser = HTTPieArgumentParser()
    with pytest.raises(SystemExit) as cm:
        parser._apply_no_options(['invalid_arg'])
    
    assert str(cm.value) == 'unrecognized arguments: invalid_arg'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argparser_HTTPieArgumentParser__apply_no_options_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________ test_apply_no_options_invalid _________________________

    def test_apply_no_options_invalid():
        parser = HTTPieArgumentParser()
        with pytest.raises(SystemExit) as cm:
>           parser._apply_no_options(['invalid_arg'])

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argparser_HTTPieArgumentParser__apply_no_options_0_test_edge_case.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/cli/argparser.py:380: in _apply_no_options
    self.error(f'unrecognized arguments: {" ".join(invalid)}')
httpie/httpie/cli/argparser.py:601: in error
    self.print_usage(sys.stderr)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = HTTPieArgumentParser(prog='__main__.py', usage=None, description=None, formatter_class=<class 'httpie.cli.argparser.HTTPieHelpFormatter'>, conflict_handler='error', add_help=False)
file = <_io.TextIOWrapper name="<_io.FileIO name=8 mode='rb+' closefd=True>" mode='r+' encoding='utf-8'>

    def print_usage(self, file):
        from rich.text import Text
        from httpie.output.ui import rich_help
    
        whitelist = set()
        _, exception, _ = sys.exc_info()
        if (
            isinstance(exception, argparse.ArgumentError)
            and len(exception.args) >= 1
            and isinstance(exception.args[0], argparse.Action)
            and exception.args[0].option_strings
        ):
            # add_usage path is also taken when you pass an invalid option,
            # e.g --style=invalid. If something like that happens, we want
            # to include to action that caused to the invalid usage into
            # the list of actions we are displaying.
            whitelist.add(exception.args[0].option_strings[0])
    
        usage_text = Text('usage', style='bold')
        usage_text.append(':\n    ')
>       usage_text.append(rich_help.to_usage(self.spec, whitelist=whitelist))
E       AttributeError: 'HTTPieArgumentParser' object has no attribute 'spec'

httpie/httpie/cli/argparser.py:595: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argparser_HTTPieArgumentParser__apply_no_options_0_test_edge_case.py::test_apply_no_options_invalid
============================== 1 failed in 0.34s ===============================
"""