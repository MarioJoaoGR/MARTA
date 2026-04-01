
import pytest
from pytutils.env import expand

@pytest.mark.parametrize("invalid_input", ["~invalid_user", "$INVALID_VAR/Projects", "~/nonexistent_directory"])
def test_invalid_input_error_handling(invalid_input):
    # The function should return the input string as it is, without raising an error
    result = expand(invalid_input)
    assert result == invalid_input  # Check if the result matches the original input

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

pytutils/Test4DT_tests/test_pytutils_env_expand_5_test_invalid_input_error_handling.py . [ 33%]
.F                                                                       [100%]

=================================== FAILURES ===================================
__________ test_invalid_input_error_handling[~/nonexistent_directory] __________

invalid_input = '~/nonexistent_directory'

    @pytest.mark.parametrize("invalid_input", ["~invalid_user", "$INVALID_VAR/Projects", "~/nonexistent_directory"])
    def test_invalid_input_error_handling(invalid_input):
        # The function should return the input string as it is, without raising an error
        result = expand(invalid_input)
>       assert result == invalid_input  # Check if the result matches the original input
E       AssertionError: assert '/home/joaovi...ent_directory' == '~/nonexistent_directory'
E         
E         - ~/nonexistent_directory
E         + /home/joaovitorino/nonexistent_directory

pytutils/Test4DT_tests/test_pytutils_env_expand_5_test_invalid_input_error_handling.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_env_expand_5_test_invalid_input_error_handling.py::test_invalid_input_error_handling[~/nonexistent_directory]
========================= 1 failed, 2 passed in 0.07s ==========================
"""