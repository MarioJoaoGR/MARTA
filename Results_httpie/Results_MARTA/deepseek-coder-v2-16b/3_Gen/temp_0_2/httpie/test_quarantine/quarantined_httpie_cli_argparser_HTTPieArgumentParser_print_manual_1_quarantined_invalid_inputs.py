
import pytest
from httpie.cli.argparser import HTTPieArgumentParser

@pytest.mark.parametrize("invalid_input", [123, None, True, [], {}])
def test_invalid_inputs(invalid_input):
    with pytest.raises(TypeError):
        parser = HTTPieArgumentParser()
        parser.parse_args([invalid_input])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_1_test_invalid_inputs.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_inputs[123] ___________________________

invalid_input = 123

    @pytest.mark.parametrize("invalid_input", [123, None, True, [], {}])
    def test_invalid_inputs(invalid_input):
        with pytest.raises(TypeError):
            parser = HTTPieArgumentParser()
>           parser.parse_args([invalid_input])

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_1_test_invalid_inputs.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = HTTPieArgumentParser(prog='__main__.py', usage=None, description=None, formatter_class=<class 'httpie.cli.argparser.HTTPieHelpFormatter'>, conflict_handler='error', add_help=False)
env = [123], args = None, namespace = None

    def parse_args(
        self,
        env: Environment,
        args=None,
        namespace=None
    ) -> argparse.Namespace:
        self.env = env
>       self.env.args = namespace = namespace or argparse.Namespace()
E       AttributeError: 'list' object has no attribute 'args'

httpie/httpie/cli/argparser.py:158: AttributeError
__________________________ test_invalid_inputs[None] ___________________________

invalid_input = None

    @pytest.mark.parametrize("invalid_input", [123, None, True, [], {}])
    def test_invalid_inputs(invalid_input):
        with pytest.raises(TypeError):
            parser = HTTPieArgumentParser()
>           parser.parse_args([invalid_input])

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_1_test_invalid_inputs.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = HTTPieArgumentParser(prog='__main__.py', usage=None, description=None, formatter_class=<class 'httpie.cli.argparser.HTTPieHelpFormatter'>, conflict_handler='error', add_help=False)
env = [None], args = None, namespace = None

    def parse_args(
        self,
        env: Environment,
        args=None,
        namespace=None
    ) -> argparse.Namespace:
        self.env = env
>       self.env.args = namespace = namespace or argparse.Namespace()
E       AttributeError: 'list' object has no attribute 'args'

httpie/httpie/cli/argparser.py:158: AttributeError
__________________________ test_invalid_inputs[True] ___________________________

invalid_input = True

    @pytest.mark.parametrize("invalid_input", [123, None, True, [], {}])
    def test_invalid_inputs(invalid_input):
        with pytest.raises(TypeError):
            parser = HTTPieArgumentParser()
>           parser.parse_args([invalid_input])

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_1_test_invalid_inputs.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = HTTPieArgumentParser(prog='__main__.py', usage=None, description=None, formatter_class=<class 'httpie.cli.argparser.HTTPieHelpFormatter'>, conflict_handler='error', add_help=False)
env = [True], args = None, namespace = None

    def parse_args(
        self,
        env: Environment,
        args=None,
        namespace=None
    ) -> argparse.Namespace:
        self.env = env
>       self.env.args = namespace = namespace or argparse.Namespace()
E       AttributeError: 'list' object has no attribute 'args'

httpie/httpie/cli/argparser.py:158: AttributeError
_____________________ test_invalid_inputs[invalid_input3] ______________________

invalid_input = []

    @pytest.mark.parametrize("invalid_input", [123, None, True, [], {}])
    def test_invalid_inputs(invalid_input):
        with pytest.raises(TypeError):
            parser = HTTPieArgumentParser()
>           parser.parse_args([invalid_input])

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_1_test_invalid_inputs.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = HTTPieArgumentParser(prog='__main__.py', usage=None, description=None, formatter_class=<class 'httpie.cli.argparser.HTTPieHelpFormatter'>, conflict_handler='error', add_help=False)
env = [[]], args = None, namespace = None

    def parse_args(
        self,
        env: Environment,
        args=None,
        namespace=None
    ) -> argparse.Namespace:
        self.env = env
>       self.env.args = namespace = namespace or argparse.Namespace()
E       AttributeError: 'list' object has no attribute 'args'

httpie/httpie/cli/argparser.py:158: AttributeError
_____________________ test_invalid_inputs[invalid_input4] ______________________

invalid_input = {}

    @pytest.mark.parametrize("invalid_input", [123, None, True, [], {}])
    def test_invalid_inputs(invalid_input):
        with pytest.raises(TypeError):
            parser = HTTPieArgumentParser()
>           parser.parse_args([invalid_input])

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_1_test_invalid_inputs.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = HTTPieArgumentParser(prog='__main__.py', usage=None, description=None, formatter_class=<class 'httpie.cli.argparser.HTTPieHelpFormatter'>, conflict_handler='error', add_help=False)
env = [{}], args = None, namespace = None

    def parse_args(
        self,
        env: Environment,
        args=None,
        namespace=None
    ) -> argparse.Namespace:
        self.env = env
>       self.env.args = namespace = namespace or argparse.Namespace()
E       AttributeError: 'list' object has no attribute 'args'

httpie/httpie/cli/argparser.py:158: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_1_test_invalid_inputs.py::test_invalid_inputs[123]
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_1_test_invalid_inputs.py::test_invalid_inputs[None]
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_1_test_invalid_inputs.py::test_invalid_inputs[True]
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_1_test_invalid_inputs.py::test_invalid_inputs[invalid_input3]
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argparser_HTTPieArgumentParser_print_manual_1_test_invalid_inputs.py::test_invalid_inputs[invalid_input4]
============================== 5 failed in 0.30s ===============================
"""