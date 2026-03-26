
import pytest
from pytutils.env import parse_env_file_contents

@pytest.mark.parametrize("lines", [[]])
def test_empty_list_input(lines):
    with pytest.raises(StopIteration):
        list(parse_env_file_contents(lines))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_env_parse_env_file_contents_4_test_empty_list_input.py F [100%]

=================================== FAILURES ===================================
________________________ test_empty_list_input[lines0] _________________________

lines = []

    @pytest.mark.parametrize("lines", [[]])
    def test_empty_list_input(lines):
>       with pytest.raises(StopIteration):
E       Failed: DID NOT RAISE <class 'StopIteration'>

pytutils/Test4DT_tests/test_pytutils_env_parse_env_file_contents_4_test_empty_list_input.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_env_parse_env_file_contents_4_test_empty_list_input.py::test_empty_list_input[lines0]
============================== 1 failed in 0.06s ===============================
"""