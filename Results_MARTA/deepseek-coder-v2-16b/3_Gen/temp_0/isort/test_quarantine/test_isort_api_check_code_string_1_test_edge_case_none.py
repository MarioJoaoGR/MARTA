
import pytest
from io import StringIO
from pathlib import Path
from isort.api import check_code_string, Config, DEFAULT_CONFIG
from isort.exceptions import InvalidSettingsPath

@pytest.mark.parametrize("show_diff, extension, config, file_path, disregard_skip", [
    (False, None, DEFAULT_CONFIG, None, False),
    (True, '.py', DEFAULT_CONFIG, Path('test.py'), True)
])
def test_check_code_string(show_diff, extension, config, file_path, disregard_skip):
    code = "import os\nimport sys"
    with pytest.raises(InvalidSettingsPath):
        check_code_string(
            code,
            show_diff=show_diff,
            extension=extension,
            config=config,
            file_path=file_path,
            disregard_skip=disregard_skip
        )

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort_api_check_code_string_1_test_edge_case_none.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
____________ test_check_code_string[False-None-config0-None-False] _____________

show_diff = False, extension = None
config = Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'build', '_build', 'dist', '.pants.d', '.git', '.bz...ge}', format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False)
file_path = None, disregard_skip = False

    @pytest.mark.parametrize("show_diff, extension, config, file_path, disregard_skip", [
        (False, None, DEFAULT_CONFIG, None, False),
        (True, '.py', DEFAULT_CONFIG, Path('test.py'), True)
    ])
    def test_check_code_string(show_diff, extension, config, file_path, disregard_skip):
        code = "import os\nimport sys"
>       with pytest.raises(InvalidSettingsPath):
E       Failed: DID NOT RAISE <class 'isort.exceptions.InvalidSettingsPath'>

isort/Test4DT_tests/test_isort_api_check_code_string_1_test_edge_case_none.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_api_check_code_string_1_test_edge_case_none.py::test_check_code_string[False-None-config0-None-False]
========================= 1 failed, 1 passed in 0.13s ==========================
"""