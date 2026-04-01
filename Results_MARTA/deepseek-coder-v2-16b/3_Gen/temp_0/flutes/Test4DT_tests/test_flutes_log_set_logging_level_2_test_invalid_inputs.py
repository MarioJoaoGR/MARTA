
import pytest
from unittest.mock import patch
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

@pytest.mark.parametrize("invalid_level", ["INVALID_LEVEL", None, 123])
def test_invalid_inputs(invalid_level):
    with pytest.raises(ValueError):
        set_logging_level(invalid_level)
