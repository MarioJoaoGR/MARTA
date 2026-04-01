
import pytest
from isort.settings import Config

@pytest.mark.parametrize("pattern", [
    "some_directory/",  # Pattern ending with a directory separator
    "some_file.py"      # A specific file, not a directory
])
def test_parse_known_pattern(pattern):
    config = Config()
    patterns = config._parse_known_pattern(pattern)
    
    if pattern.endswith(os.path.sep):
        assert all(os.path.isdir(os.path.join(config.directory, pattern, p)) for p in patterns), \
            f"Expected {pattern} to be a directory but it is not."
    else:
        assert patterns == [pattern], f"Unexpected patterns found: {patterns}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings_Config__parse_known_pattern_0_test_edge_case
isort/Test4DT_tests/test_isort_settings_Config__parse_known_pattern_0_test_edge_case.py:13:24: E0602: Undefined variable 'os' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__parse_known_pattern_0_test_edge_case.py:14:19: E0602: Undefined variable 'os' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__parse_known_pattern_0_test_edge_case.py:14:33: E0602: Undefined variable 'os' (undefined-variable)


"""