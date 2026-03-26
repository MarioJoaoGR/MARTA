
import pytest

from isort.wrap_modes import WrapModes


def from_string(value: str) -> "WrapModes":
    """
    Converts a string representation of a wrap mode to the corresponding enum value from the `WrapModes` class.

    Parameters:
        value (str): The string representing the wrap mode, which can be either an integer or a string that matches one of the enum member names in `WrapModes`.

    Returns:
        WrapModes: The enum value corresponding to the provided string representation. If no matching enum member is found, returns None.

    Examples:
        To convert a string representation of a wrap mode:
            from_string("WRAP") will return the enum member with name "WRAP" in the `WrapModes` class.
            from_string("1") will return the enum member corresponding to integer 1 in the `WrapModes` class.

        If the provided string does not match any known wrap mode, it returns None.

    Usage:
        import WrapModes
        
        # Example usage with a valid string representation of a wrap mode
        result = from_string("WRAP")
        print(result)  # Output will be the enum member for "WRAP" in `WrapModes` class
    """
    return getattr(WrapModes, str(value), None) or WrapModes(int(value))

def test_invalid_input_error_handling():
    with pytest.raises(ValueError):
        from_string("INVALID")  # This should raise a ValueError because "INVALID" is not a valid wrap mode
