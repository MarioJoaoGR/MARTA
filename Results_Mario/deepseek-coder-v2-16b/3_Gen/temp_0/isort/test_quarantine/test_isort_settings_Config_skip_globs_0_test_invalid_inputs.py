
import pytest
from isort.settings import Config

def test_skip_globs():
    config = Config()
    assert isinstance(config.skip_globs(), frozenset)
    assert len(config.skip_globs()) == 0

@pytest.mark.parametrize("skip_glob, extend_skip_glob", [
    ("*.py", set()),
    (set(), {"*.txt"}),
    ({"test_*.py"}, {"*_test.py"})
])
def test_skip_globs_with_params(skip_glob, extend_skip_glob):
    config = Config()
    config.skip_glob = skip_glob
    config.extend_skip_glob = extend_skip_glob
    expected_set = frozenset(list(skip_glob) + list(extend_skip_glob))
    assert config.skip_globs() == expected_set

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings_Config_skip_globs_0_test_invalid_inputs
isort/Test4DT_tests/test_isort_settings_Config_skip_globs_0_test_invalid_inputs.py:7:22: E1102: config.skip_globs is not callable (not-callable)
isort/Test4DT_tests/test_isort_settings_Config_skip_globs_0_test_invalid_inputs.py:8:15: E1102: config.skip_globs is not callable (not-callable)
isort/Test4DT_tests/test_isort_settings_Config_skip_globs_0_test_invalid_inputs.py:20:11: E1102: config.skip_globs is not callable (not-callable)


"""