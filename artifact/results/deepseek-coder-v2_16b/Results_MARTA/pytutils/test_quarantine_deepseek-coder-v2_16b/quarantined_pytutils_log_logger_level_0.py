
import logging
import pytest
from pytutils.log import logger_level



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_log_logger_level_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__________________________ test_logger_level_context ___________________________

    def test_logger_level_context():
        log = logging.getLogger(__name__)
        initial_level = log.level
    
        with pytest.raises(TypeError):  # logger_level expects a Logger instance, not None
>           with logger_level(None, logging.DEBUG):

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_log_logger_level_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/contextlib.py:135: in __enter__
    return next(self.gen)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

logger = None, level = 10

    @contextmanager
    def logger_level(logger, level):
        """Set logger level to `level` within a context block. Don't use this except for debugging please, it's gross."""
>       initial = logger.level
E       AttributeError: 'NoneType' object has no attribute 'level'

/opt/marta/baselines/codamosa/replication/test-apps/pytutils/pytutils/log.py:165: AttributeError
_____________________________ test_invalid_logger ______________________________

    def test_invalid_logger():
        with pytest.raises(TypeError):
>           with logger_level("not a logger", logging.DEBUG):

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_log_logger_level_0.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/contextlib.py:135: in __enter__
    return next(self.gen)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

logger = 'not a logger', level = 10

    @contextmanager
    def logger_level(logger, level):
        """Set logger level to `level` within a context block. Don't use this except for debugging please, it's gross."""
>       initial = logger.level
E       AttributeError: 'str' object has no attribute 'level'

/opt/marta/baselines/codamosa/replication/test-apps/pytutils/pytutils/log.py:165: AttributeError
______________________________ test_invalid_level ______________________________

    def test_invalid_level():
        log = logging.getLogger(__name__)
        initial_level = log.level
    
>       with pytest.raises(ValueError):  # Invalid level should raise a ValueError
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_log_logger_level_0.py:23: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_log_logger_level_0.py::test_logger_level_context
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_log_logger_level_0.py::test_invalid_logger
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_log_logger_level_0.py::test_invalid_level
============================== 3 failed in 0.07s ===============================
"""