
import pytest
from pathlib import Path
import os
from flutils.pathutils import find_paths, normalize_path

@pytest.mark.parametrize("pattern, expected_count", [
    ('~/tmp/*', 2),
    ('/home/user/data/*', 0),
    ('data/*', 0)
])
def test_find_paths(pattern, expected_count):
    normalized_pattern = normalize_path(pattern)
    paths = list(find_paths(normalized_pattern))
    assert len(paths) == expected_count, f"Expected {expected_count} paths but got {len(paths)}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_find_paths_0.py F [ 33%]
..                                                                       [100%]

=================================== FAILURES ===================================
__________________________ test_find_paths[~/tmp/*-2] __________________________

pattern = '~/tmp/*', expected_count = 2

    @pytest.mark.parametrize("pattern, expected_count", [
        ('~/tmp/*', 2),
        ('/home/user/data/*', 0),
        ('data/*', 0)
    ])
    def test_find_paths(pattern, expected_count):
        normalized_pattern = normalize_path(pattern)
        paths = list(find_paths(normalized_pattern))
>       assert len(paths) == expected_count, f"Expected {expected_count} paths but got {len(paths)}"
E       AssertionError: Expected 2 paths but got 4
E       assert 4 == 2
E        +  where 4 = len([PosixPath('/home/joaovitorino/tmp/test_path'), PosixPath('/home/joaovitorino/tmp/flutils.tests.osutils.txt'), PosixPath('/home/joaovitorino/tmp/subdir1'), PosixPath('/home/joaovitorino/tmp/file1.txt')])

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_find_paths_0.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_find_paths_0.py::test_find_paths[~/tmp/*-2]
========================= 1 failed, 2 passed in 0.06s ==========================
"""