
from isort.settings import Config

class TestConfig:
    def test_skip_globs(self):
        config = Config()
        assert isinstance(config.skip_globs(), frozenset)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings_Config_skip_globs_0_test_error_handling
isort/Test4DT_tests/test_isort_settings_Config_skip_globs_0_test_error_handling.py:7:26: E1102: config.skip_globs is not callable (not-callable)


"""