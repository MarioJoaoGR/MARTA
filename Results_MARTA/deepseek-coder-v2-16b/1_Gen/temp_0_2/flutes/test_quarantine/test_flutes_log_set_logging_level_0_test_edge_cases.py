
import pytest
from flutes.log import set_logging_level, LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, LOGGER

@pytest.mark.parametrize("level, expected", [
    ('DEBUG', None),
    ('INFO', None),
    ('WARNING', None),
    ('ERROR', None),
    ('CRITICAL', None)
])
def test_set_logging_level(level, expected):
    set_logging_level(level)
    if level == 'DEBUG':
        assert _CONSOLE_LOGGING_LEVEL.value == LEVEL_MAP['DEBUG']
        assert LOGGER.getEffectiveLevel() == LEVEL_MAP['DEBUG']
    elif level == 'INFO':
        assert _CONSOLE_LOGGING_LEVEL.value == LEVEL_MAP['INFO']
        assert LOGGER.getEffectiveLevel() == LEVEL_MAP['INFO']
    elif level == 'WARNING':
        assert _CONSOLE_LOGGING_LEVEL.value == LEVEL_MAP['WARNING']
        assert LOGGER.getEffectiveLevel() == LEVEL_MAP['WARNING']
    elif level == 'ERROR':
        assert _CONSOLE_LOGGING_LEVEL.value == LEVEL_MAP['ERROR']
        assert LOGGER.getEffectiveLevel() == LEVEL_MAP['ERROR']
    elif level == 'CRITICAL':
        assert _CONSOLE_LOGGING_LEVEL.value == LEVEL_MAP['CRITICAL']
        assert LOGGER.getEffectiveLevel() == LEVEL_MAP['CRITICAL']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

flutes/Test4DT_tests/test_flutes_log_set_logging_level_0_test_edge_cases.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
______________________ test_set_logging_level[DEBUG-None] ______________________

level = 'DEBUG', expected = None

    @pytest.mark.parametrize("level, expected", [
        ('DEBUG', None),
        ('INFO', None),
        ('WARNING', None),
        ('ERROR', None),
        ('CRITICAL', None)
    ])
    def test_set_logging_level(level, expected):
>       set_logging_level(level)

flutes/Test4DT_tests/test_flutes_log_set_logging_level_0_test_edge_cases.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

level = 'DEBUG', console = True, file = True

    def set_logging_level(level: LoggingLevel, console: bool = True, file: bool = True) -> None:
        r"""Set the global logging level to the specified level.
    
        :param level: Logging level.
        :param console: If ``True``, the specified logging level applies to console output.
        :param file: If ``True``, the specified logging level applies to file output.
        """
        if level not in LEVEL_MAP:
>           raise ValueError(f"Incorrect logging level '{level}'")
E           ValueError: Incorrect logging level 'DEBUG'

flutes/flutes/log.py:193: ValueError
______________________ test_set_logging_level[INFO-None] _______________________

level = 'INFO', expected = None

    @pytest.mark.parametrize("level, expected", [
        ('DEBUG', None),
        ('INFO', None),
        ('WARNING', None),
        ('ERROR', None),
        ('CRITICAL', None)
    ])
    def test_set_logging_level(level, expected):
>       set_logging_level(level)

flutes/Test4DT_tests/test_flutes_log_set_logging_level_0_test_edge_cases.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

level = 'INFO', console = True, file = True

    def set_logging_level(level: LoggingLevel, console: bool = True, file: bool = True) -> None:
        r"""Set the global logging level to the specified level.
    
        :param level: Logging level.
        :param console: If ``True``, the specified logging level applies to console output.
        :param file: If ``True``, the specified logging level applies to file output.
        """
        if level not in LEVEL_MAP:
>           raise ValueError(f"Incorrect logging level '{level}'")
E           ValueError: Incorrect logging level 'INFO'

flutes/flutes/log.py:193: ValueError
_____________________ test_set_logging_level[WARNING-None] _____________________

level = 'WARNING', expected = None

    @pytest.mark.parametrize("level, expected", [
        ('DEBUG', None),
        ('INFO', None),
        ('WARNING', None),
        ('ERROR', None),
        ('CRITICAL', None)
    ])
    def test_set_logging_level(level, expected):
>       set_logging_level(level)

flutes/Test4DT_tests/test_flutes_log_set_logging_level_0_test_edge_cases.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

level = 'WARNING', console = True, file = True

    def set_logging_level(level: LoggingLevel, console: bool = True, file: bool = True) -> None:
        r"""Set the global logging level to the specified level.
    
        :param level: Logging level.
        :param console: If ``True``, the specified logging level applies to console output.
        :param file: If ``True``, the specified logging level applies to file output.
        """
        if level not in LEVEL_MAP:
>           raise ValueError(f"Incorrect logging level '{level}'")
E           ValueError: Incorrect logging level 'WARNING'

flutes/flutes/log.py:193: ValueError
______________________ test_set_logging_level[ERROR-None] ______________________

level = 'ERROR', expected = None

    @pytest.mark.parametrize("level, expected", [
        ('DEBUG', None),
        ('INFO', None),
        ('WARNING', None),
        ('ERROR', None),
        ('CRITICAL', None)
    ])
    def test_set_logging_level(level, expected):
>       set_logging_level(level)

flutes/Test4DT_tests/test_flutes_log_set_logging_level_0_test_edge_cases.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

level = 'ERROR', console = True, file = True

    def set_logging_level(level: LoggingLevel, console: bool = True, file: bool = True) -> None:
        r"""Set the global logging level to the specified level.
    
        :param level: Logging level.
        :param console: If ``True``, the specified logging level applies to console output.
        :param file: If ``True``, the specified logging level applies to file output.
        """
        if level not in LEVEL_MAP:
>           raise ValueError(f"Incorrect logging level '{level}'")
E           ValueError: Incorrect logging level 'ERROR'

flutes/flutes/log.py:193: ValueError
____________________ test_set_logging_level[CRITICAL-None] _____________________

level = 'CRITICAL', expected = None

    @pytest.mark.parametrize("level, expected", [
        ('DEBUG', None),
        ('INFO', None),
        ('WARNING', None),
        ('ERROR', None),
        ('CRITICAL', None)
    ])
    def test_set_logging_level(level, expected):
>       set_logging_level(level)

flutes/Test4DT_tests/test_flutes_log_set_logging_level_0_test_edge_cases.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

level = 'CRITICAL', console = True, file = True

    def set_logging_level(level: LoggingLevel, console: bool = True, file: bool = True) -> None:
        r"""Set the global logging level to the specified level.
    
        :param level: Logging level.
        :param console: If ``True``, the specified logging level applies to console output.
        :param file: If ``True``, the specified logging level applies to file output.
        """
        if level not in LEVEL_MAP:
>           raise ValueError(f"Incorrect logging level '{level}'")
E           ValueError: Incorrect logging level 'CRITICAL'

flutes/flutes/log.py:193: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_set_logging_level_0_test_edge_cases.py::test_set_logging_level[DEBUG-None]
FAILED flutes/Test4DT_tests/test_flutes_log_set_logging_level_0_test_edge_cases.py::test_set_logging_level[INFO-None]
FAILED flutes/Test4DT_tests/test_flutes_log_set_logging_level_0_test_edge_cases.py::test_set_logging_level[WARNING-None]
FAILED flutes/Test4DT_tests/test_flutes_log_set_logging_level_0_test_edge_cases.py::test_set_logging_level[ERROR-None]
FAILED flutes/Test4DT_tests/test_flutes_log_set_logging_level_0_test_edge_cases.py::test_set_logging_level[CRITICAL-None]
============================== 5 failed in 0.11s ===============================
"""