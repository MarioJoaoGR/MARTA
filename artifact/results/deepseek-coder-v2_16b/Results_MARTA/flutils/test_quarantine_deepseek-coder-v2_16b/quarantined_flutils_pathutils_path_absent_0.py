
import os
from pathlib import Path
import pytest
from flutils.pathutils import path_absent, normalize_path


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_path_absent_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
________________________ test_file_instead_of_directory ________________________

    def test_file_instead_of_directory():
        # Arrange
        test_file = 'test_file'
        with open(test_file, 'w') as f:
            f.write('content')
    
        try:
            # Act & Assert
>           with pytest.raises(IsADirectoryError):
E           Failed: DID NOT RAISE <class 'IsADirectoryError'>

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_path_absent_0.py:15: Failed

During handling of the above exception, another exception occurred:

    def test_file_instead_of_directory():
        # Arrange
        test_file = 'test_file'
        with open(test_file, 'w') as f:
            f.write('content')
    
        try:
            # Act & Assert
            with pytest.raises(IsADirectoryError):
                path_absent(test_file)
        finally:
>           os.remove(test_file)
E           FileNotFoundError: [Errno 2] No such file or directory: 'test_file'

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_path_absent_0.py:18: FileNotFoundError
______________________________ test_symlink_path _______________________________

    def test_symlink_path():
        # Arrange
        target = Path('target_of_symlink')
>       target.mkdir()

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_path_absent_0.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = PosixPath('target_of_symlink'), mode = 511, parents = False
exist_ok = False

    def mkdir(self, mode=0o777, parents=False, exist_ok=False):
        """
        Create a new directory at this given path.
        """
        try:
>           self._accessor.mkdir(self, mode)
E           FileExistsError: [Errno 17] File exists: 'target_of_symlink'

/opt/conda/envs/test4py_env/lib/python3.10/pathlib.py:1175: FileExistsError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_path_absent_0.py::test_file_instead_of_directory
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_path_absent_0.py::test_symlink_path
============================== 2 failed in 0.11s ===============================
"""