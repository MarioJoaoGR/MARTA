
from isort.comments import add_to_line

def test_none_input():
    assert add_to_line(None, "print('Hello, World!')", removed=False) == "print('Hello, World!')"
    assert add_to_line([], "import os", removed=False) == "import os"
    assert add_to_line(['This is comment 1'], "import os", removed=False) == "import os  # This is comment 1"
    assert add_to_line(['This is comment 1', 'This is comment 2'], "import os", removed=False) == "import os  # This is comment 1; This is comment 2"

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

isort/Test4DT_tests/test_isort_comments_add_to_line_1_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        assert add_to_line(None, "print('Hello, World!')", removed=False) == "print('Hello, World!')"
        assert add_to_line([], "import os", removed=False) == "import os"
>       assert add_to_line(['This is comment 1'], "import os", removed=False) == "import os  # This is comment 1"
E       AssertionError: assert 'import os This is comment 1' == 'import os  #... is comment 1'
E         
E         - import os  # This is comment 1
E         ?          ---
E         + import os This is comment 1

isort/Test4DT_tests/test_isort_comments_add_to_line_1_test_none_input.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_comments_add_to_line_1_test_none_input.py::test_none_input
============================== 1 failed in 0.12s ===============================
"""