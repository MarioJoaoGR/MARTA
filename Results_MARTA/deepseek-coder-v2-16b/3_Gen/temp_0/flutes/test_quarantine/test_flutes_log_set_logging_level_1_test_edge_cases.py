
import pytest
from flutes.log import set_logging_level, LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, LOGGER
from typing import Any, TypeVar

LoggingLevel = TypeVar('LoggingLevel')

@pytest.mark.parametrize("level, console, file", [
    ('DEBUG', True, True),
    ('INFO', False, True),
    ('WARNING', True, False),
    ('ERROR', False, False)
])
def test_set_logging_level(level: LoggingLevel, console: bool, file: bool):
    set_logging_level(level, console=console, file=file)
    if level == 'DEBUG' and console:
        assert _CONSOLE_LOGGING_LEVEL.value == LEVEL_MAP['DEBUG']
    elif level == 'INFO' and not console:
        assert _CONSOLE_LOGGING_LEVEL.value == LEVEL_MAP['INFO']
    elif level == 'WARNING' and file:
        assert LOGGER.level == LEVEL_MAP['WARNING']
    elif level == 'ERROR' and not file:
        assert LOGGER.level == LEVEL_MAP['ERROR']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

flutes/Test4DT_tests/test_flutes_log_set_logging_level_1_test_edge_cases.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
___________________ test_set_logging_level[DEBUG-True-True] ____________________

level = 'DEBUG', console = True, file = True

    @pytest.mark.parametrize("level, console, file", [
        ('DEBUG', True, True),
        ('INFO', False, True),
        ('WARNING', True, False),
        ('ERROR', False, False)
    ])
    def test_set_logging_level(level: LoggingLevel, console: bool, file: bool):
>       set_logging_level(level, console=console, file=file)

flutes/Test4DT_tests/test_flutes_log_set_logging_level_1_test_edge_cases.py:15: 
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
___________________ test_set_logging_level[INFO-False-True] ____________________

level = 'INFO', console = False, file = True

    @pytest.mark.parametrize("level, console, file", [
        ('DEBUG', True, True),
        ('INFO', False, True),
        ('WARNING', True, False),
        ('ERROR', False, False)
    ])
    def test_set_logging_level(level: LoggingLevel, console: bool, file: bool):
>       set_logging_level(level, console=console, file=file)

flutes/Test4DT_tests/test_flutes_log_set_logging_level_1_test_edge_cases.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

level = 'INFO', console = False, file = True

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
__________________ test_set_logging_level[WARNING-True-False] __________________

level = 'WARNING', console = True, file = False

    @pytest.mark.parametrize("level, console, file", [
        ('DEBUG', True, True),
        ('INFO', False, True),
        ('WARNING', True, False),
        ('ERROR', False, False)
    ])
    def test_set_logging_level(level: LoggingLevel, console: bool, file: bool):
>       set_logging_level(level, console=console, file=file)

flutes/Test4DT_tests/test_flutes_log_set_logging_level_1_test_edge_cases.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

level = 'WARNING', console = True, file = False

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
__________________ test_set_logging_level[ERROR-False-False] ___________________

level = 'ERROR', console = False, file = False

    @pytest.mark.parametrize("level, console, file", [
        ('DEBUG', True, True),
        ('INFO', False, True),
        ('WARNING', True, False),
        ('ERROR', False, False)
    ])
    def test_set_logging_level(level: LoggingLevel, console: bool, file: bool):
>       set_logging_level(level, console=console, file=file)

flutes/Test4DT_tests/test_flutes_log_set_logging_level_1_test_edge_cases.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

level = 'ERROR', console = False, file = False

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
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_set_logging_level_1_test_edge_cases.py::test_set_logging_level[DEBUG-True-True]
FAILED flutes/Test4DT_tests/test_flutes_log_set_logging_level_1_test_edge_cases.py::test_set_logging_level[INFO-False-True]
FAILED flutes/Test4DT_tests/test_flutes_log_set_logging_level_1_test_edge_cases.py::test_set_logging_level[WARNING-True-False]
FAILED flutes/Test4DT_tests/test_flutes_log_set_logging_level_1_test_edge_cases.py::test_set_logging_level[ERROR-False-False]
============================== 4 failed in 0.12s ===============================
"""