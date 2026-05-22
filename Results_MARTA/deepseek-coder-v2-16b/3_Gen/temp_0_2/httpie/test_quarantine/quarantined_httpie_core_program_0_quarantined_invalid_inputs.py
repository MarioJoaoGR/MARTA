
import pytest
from httpie.core import program, ExitStatus, argparse, Environment

@pytest.mark.parametrize("args", [
    argparse.Namespace(download=True, output_options=[], url='http://example.com'),
    argparse.Namespace(download=False, output_options=['body'], url='http://example.com')
])
def test_invalid_inputs(args):
    env = Environment()
    result = program(args, env)
    assert result == ExitStatus.ERROR

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_core_program_0_test_invalid_inputs.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
__________________________ test_invalid_inputs[args0] __________________________

args = Namespace(download=True, output_options=[], url='http://example.com')

    @pytest.mark.parametrize("args", [
        argparse.Namespace(download=True, output_options=[], url='http://example.com'),
        argparse.Namespace(download=False, output_options=['body'], url='http://example.com')
    ])
    def test_invalid_inputs(args):
        env = Environment()
>       result = program(args, env)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_core_program_0_test_invalid_inputs.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/core.py:180: in program
    processing_options = ProcessingOptions.from_raw_args(args)
httpie/httpie/output/models.py:36: in from_raw_args
    fetched_options = {
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

.0 = <tuple_iterator object at 0x7fbed2db6f80>

    fetched_options = {
>       option: getattr(options, option)
        for option in cls._fields
    }
E   AttributeError: 'Namespace' object has no attribute 'debug'

httpie/httpie/output/models.py:37: AttributeError
__________________________ test_invalid_inputs[args1] __________________________

args = Namespace(download=False, output_options=['body'], url='http://example.com')

    @pytest.mark.parametrize("args", [
        argparse.Namespace(download=True, output_options=[], url='http://example.com'),
        argparse.Namespace(download=False, output_options=['body'], url='http://example.com')
    ])
    def test_invalid_inputs(args):
        env = Environment()
>       result = program(args, env)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_core_program_0_test_invalid_inputs.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/core.py:180: in program
    processing_options = ProcessingOptions.from_raw_args(args)
httpie/httpie/output/models.py:36: in from_raw_args
    fetched_options = {
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

.0 = <tuple_iterator object at 0x7fbed2ee6ce0>

    fetched_options = {
>       option: getattr(options, option)
        for option in cls._fields
    }
E   AttributeError: 'Namespace' object has no attribute 'debug'

httpie/httpie/output/models.py:37: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_core_program_0_test_invalid_inputs.py::test_invalid_inputs[args0]
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_core_program_0_test_invalid_inputs.py::test_invalid_inputs[args1]
============================== 2 failed in 0.33s ===============================
"""