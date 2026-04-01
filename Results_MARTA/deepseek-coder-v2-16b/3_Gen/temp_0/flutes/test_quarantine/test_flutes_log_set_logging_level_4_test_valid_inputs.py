
import pytest
from flutes.log import LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, LOGGER

def set_logging_level(level: str, console: bool = True, file: bool = True) -> None:
    r"""Set the global logging level to the specified level.

    This function sets the logging level for both console and file outputs if specified. The `level` parameter should be one of the valid logging levels defined in `LEVEL_MAP`. If the provided level is not recognized, a ValueError will be raised.

    Parameters:
        level (str): The desired logging level. Must be one of the values defined in `LEVEL_MAP`.
        console (bool, optional): If ``True``, sets the specified logging level to console output. Defaults to True.
        file (bool, optional): If ``True``, sets the specified logging level to file output. Defaults to True.

    Raises:
        ValueError: If the provided `level` is not in `LEVEL_MAP`.

    Example:
        To set the logging level to 'DEBUG' and apply it to both console and file outputs, you can call the function as follows:

        >>> set_logging_level('DEBUG', console=True, file=True)

        If you only want to apply the 'DEBUG' level to the console output without affecting the file output, you can do:

        >>> set_logging_level('DEBUG', console=True, file=False)
    """
    if level not in LEVEL_MAP:
        raise ValueError(f"Incorrect logging level '{level}'")
    if console:
        _CONSOLE_LOGGING_LEVEL.value = LEVEL_MAP[level]
    if file:
        LOGGER.setLevel(LEVEL_MAP[level])

def test_valid_inputs():
    # Assuming LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, and LOGGER are properly defined in the flutes.log module
    
    set_logging_level('DEBUG', console=True, file=True)
    assert _CONSOLE_LOGGING_LEVEL.value == LEVEL_MAP['DEBUG']
    assert LOGGER.getLevel() == LEVEL_MAP['DEBUG']

    set_logging_level('INFO', console=True, file=False)
    assert _CONSOLE_LOGGING_LEVEL.value == LEVEL_MAP['INFO']
    assert LOGGER.getLevel() == LEVEL_MAP['INFO']

    set_logging_level('WARNING', console=False, file=True)
    assert _CONSOLE_LOGGING_LEVEL.value == LEVEL_MAP['WARNING']
    assert LOGGER.getLevel() == LEVEL_MAP['WARNING']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log_set_logging_level_4_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Assuming LEVEL_MAP, _CONSOLE_LOGGING_LEVEL, and LOGGER are properly defined in the flutes.log module
    
>       set_logging_level('DEBUG', console=True, file=True)

flutes/Test4DT_tests/test_flutes_log_set_logging_level_4_test_valid_inputs.py:37: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

level = 'DEBUG', console = True, file = True

    def set_logging_level(level: str, console: bool = True, file: bool = True) -> None:
        r"""Set the global logging level to the specified level.
    
        This function sets the logging level for both console and file outputs if specified. The `level` parameter should be one of the valid logging levels defined in `LEVEL_MAP`. If the provided level is not recognized, a ValueError will be raised.
    
        Parameters:
            level (str): The desired logging level. Must be one of the values defined in `LEVEL_MAP`.
            console (bool, optional): If ``True``, sets the specified logging level to console output. Defaults to True.
            file (bool, optional): If ``True``, sets the specified logging level to file output. Defaults to True.
    
        Raises:
            ValueError: If the provided `level` is not in `LEVEL_MAP`.
    
        Example:
            To set the logging level to 'DEBUG' and apply it to both console and file outputs, you can call the function as follows:
    
            >>> set_logging_level('DEBUG', console=True, file=True)
    
            If you only want to apply the 'DEBUG' level to the console output without affecting the file output, you can do:
    
            >>> set_logging_level('DEBUG', console=True, file=False)
        """
        if level not in LEVEL_MAP:
>           raise ValueError(f"Incorrect logging level '{level}'")
E           ValueError: Incorrect logging level 'DEBUG'

flutes/Test4DT_tests/test_flutes_log_set_logging_level_4_test_valid_inputs.py:28: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_log_set_logging_level_4_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.09s ===============================

"""