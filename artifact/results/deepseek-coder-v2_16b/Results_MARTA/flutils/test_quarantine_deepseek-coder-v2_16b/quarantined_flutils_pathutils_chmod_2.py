
import pytest
from pathlib import Path
from flutils.pathutils import chmod

@pytest.fixture(scope="module")
def temp_dir():
    temp_dir = Path('~/tmp').expanduser()
    if not temp_dir.exists():
        temp_dir.mkdir(parents=True)
    
    (temp_dir / 'file1.txt').touch()
    (temp_dir / 'file2.txt').touch()
    
    yield temp_dir
    
    # Cleanup
    for file in temp_dir.glob('**/*'):
        if file.is_file():
            file.unlink()
        elif file.is_dir():
            file.rmdir()
    temp_dir.rmdir()


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_chmod_2.py F [ 50%]
FE                                                                       [100%]

==================================== ERRORS ====================================
____ ERROR at teardown of test_valid_input_glob_pattern_with_include_parent ____

    @pytest.fixture(scope="module")
    def temp_dir():
        temp_dir = Path('~/tmp').expanduser()
        if not temp_dir.exists():
            temp_dir.mkdir(parents=True)
    
        (temp_dir / 'file1.txt').touch()
        (temp_dir / 'file2.txt').touch()
    
        yield temp_dir
    
        # Cleanup
        for file in temp_dir.glob('**/*'):
            if file.is_file():
                file.unlink()
            elif file.is_dir():
>               file.rmdir()

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_chmod_2.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = PosixPath('/home/joaovitorino/tmp/subdir')

    def rmdir(self):
        """
        Remove this directory.  The directory must be empty.
        """
>       self._accessor.rmdir(self)
E       OSError: [Errno 39] Directory not empty: '/home/joaovitorino/tmp/subdir'

/opt/conda/envs/test4py_env/lib/python3.10/pathlib.py:1215: OSError
=================================== FAILURES ===================================
________________________ test_valid_input_glob_pattern _________________________

temp_dir = PosixPath('/home/joaovitorino/tmp')

    def test_valid_input_glob_pattern(temp_dir):
        chmod(temp_dir, mode_file=0o644, mode_dir=0o755)
    
        for file in temp_dir.glob('**/*'):
            if file.is_dir():
>               assert (file.stat().st_mode & 0o777) == 0o755
E               AssertionError: assert (16832 & 511) == 493
E                +  where 16832 = os.stat_result(st_mode=16832, st_ino=15481815, st_dev=49, st_nlink=2, st_uid=30988, st_gid=40988, st_size=4096, st_atime=1785244106, st_mtime=1785244106, st_ctime=1785245926).st_mode
E                +    where os.stat_result(st_mode=16832, st_ino=15481815, st_dev=49, st_nlink=2, st_uid=30988, st_gid=40988, st_size=4096, st_atime=1785244106, st_mtime=1785244106, st_ctime=1785245926) = stat()
E                +      where stat = PosixPath('/home/joaovitorino/tmp/test_path').stat

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_chmod_2.py:30: AssertionError
______________ test_valid_input_glob_pattern_with_include_parent _______________

temp_dir = PosixPath('/home/joaovitorino/tmp')

    def test_valid_input_glob_pattern_with_include_parent(temp_dir):
        chmod(temp_dir, mode_file=0o644, mode_dir=0o755, include_parent=True)
    
        for file in temp_dir.glob('**/*'):
            if file.is_dir():
>               assert (file.stat().st_mode & 0o777) == 0o755
E               AssertionError: assert (16832 & 511) == 493
E                +  where 16832 = os.stat_result(st_mode=16832, st_ino=15481815, st_dev=49, st_nlink=2, st_uid=30988, st_gid=40988, st_size=4096, st_atime=1785244106, st_mtime=1785244106, st_ctime=1785245926).st_mode
E                +    where os.stat_result(st_mode=16832, st_ino=15481815, st_dev=49, st_nlink=2, st_uid=30988, st_gid=40988, st_size=4096, st_atime=1785244106, st_mtime=1785244106, st_ctime=1785245926) = stat()
E                +      where stat = PosixPath('/home/joaovitorino/tmp/test_path').stat

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_chmod_2.py:39: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_chmod_2.py::test_valid_input_glob_pattern
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_chmod_2.py::test_valid_input_glob_pattern_with_include_parent
ERROR ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_pathutils_chmod_2.py::test_valid_input_glob_pattern_with_include_parent
========================== 2 failed, 1 error in 0.10s ==========================
"""