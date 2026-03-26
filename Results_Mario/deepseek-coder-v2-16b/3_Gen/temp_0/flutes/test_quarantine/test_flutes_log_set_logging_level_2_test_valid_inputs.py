
import pytest
from flutes.log import set_logging_level, LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, LOGGER

@pytest.mark.parametrize("level, console, file", [
    ('DEBUG', True, True),
    ('INFO', False, True),
    ('WARNING', True, False),
    ('ERROR', False, False)
])
def test_valid_inputs(level, console, file):
    set_logging_level(level, console=console, file=file)
    
    if console:
        assert _CONSOLE_LOGGING_LEVEL.value == LEVEL_MAP[level]
    else:
        with pytest.raises(AttributeError):
            assert _CONSOLE_LOGGING_LEVEL.value
    
    if file:
        assert LOGGER.getEffectiveLevel() == LEVEL_MAP[level]
    else:
        with pytest.raises(AttributeError):
            assert LOGGER.getEffectiveLevel()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

flutes/Test4DT_tests/test_flutes_log_set_logging_level_2_test_valid_inputs.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
______________________ test_valid_inputs[DEBUG-True-True] ______________________

level = 'DEBUG', console = True, file = True

    @pytest.mark.parametrize("level, console, file", [
        ('DEBUG', True, True),
        ('INFO', False, True),
        ('WARNING', True, False),
        ('ERROR', False, False)
    ])
    def test_valid_inputs(level, console, file):
>       set_logging_level(level, console=console, file=file)

flutes/Test4DT_tests/test_flutes_log_set_logging_level_2_test_valid_inputs.py:12: 
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
______________________ test_valid_inputs[INFO-False-True] ______________________

level = 'INFO', console = False, file = True

    @pytest.mark.parametrize("level, console, file", [
        ('DEBUG', True, True),
        ('INFO', False, True),
        ('WARNING', True, False),
        ('ERROR', False, False)
    ])
    def test_valid_inputs(level, console, file):
>       set_logging_level(level, console=console, file=file)

flutes/Test4DT_tests/test_flutes_log_set_logging_level_2_test_valid_inputs.py:12: 
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
____________________ test_valid_inputs[WARNING-True-False] _____________________

level = 'WARNING', console = True, file = False

    @pytest.mark.parametrize("level, console, file", [
        ('DEBUG', True, True),
        ('INFO', False, True),
        ('WARNING', True, False),
        ('ERROR', False, False)
    ])
    def test_valid_inputs(level, console, file):
>       set_logging_level(level, console=console, file=file)

flutes/Test4DT_tests/test_flutes_log_set_logging_level_2_test_valid_inputs.py:12: 
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
_____________________ test_valid_inputs[ERROR-False-False] _____________________

level = 'ERROR', console = False, file = False

    @pytest.mark.parametrize("level, console, file", [
        ('DEBUG', True, True),
        ('INFO', False, True),
        ('WARNING', True, False),
        ('ERROR', False, False)
    ])
    def test_valid_inputs(level, console, file):
>       set_logging_level(level, console=console, file=file)

flutes/Test4DT_tests/test_flutes_log_set_logging_level_2_test_valid_inputs.py:12: 
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
FAILED flutes/Test4DT_tests/test_flutes_log_set_logging_level_2_test_valid_inputs.py::test_valid_inputs[DEBUG-True-True]
FAILED flutes/Test4DT_tests/test_flutes_log_set_logging_level_2_test_valid_inputs.py::test_valid_inputs[INFO-False-True]
FAILED flutes/Test4DT_tests/test_flutes_log_set_logging_level_2_test_valid_inputs.py::test_valid_inputs[WARNING-True-False]
FAILED flutes/Test4DT_tests/test_flutes_log_set_logging_level_2_test_valid_inputs.py::test_valid_inputs[ERROR-False-False]
============================== 4 failed in 0.13s ===============================
"""