
import pytest
from uuid import uuid4

def uuid(as_hex: bool = False) -> str:
    """
    Generates a universally unique identifier (UUID) which is represented as a string. By default, the UUID is returned in its standard format. However, if the parameter `as_hex` is set to True, the function will return the hexadecimal representation of the UUID.

    *Examples:*

    >>> uuid() # possible output: '97e3a716-6b33-4ab9-9bb1-8128cb24d76b'
    >>> uuid(as_hex=True) # possible output: '97e3a7166b334ab99bb18128cb24d76b'

    :param as_hex: A boolean flag to determine the format of the UUID string. If True, returns the hex value; if False (default), returns the standard UUID representation.
    :return: A string representing the UUID in either its default or hexadecimal format based on the `as_hex` parameter.
    """
    uid = uuid4()

    if as_hex:
        return uid.hex

    return str(uid)

def test_valid_uuid_hex():
    # Test standard UUID representation
    std_uuid = uuid()
    assert isinstance(std_uuid, str), "Expected a string"
    assert len(std_uuid) == 36, "Standard UUID should be 36 characters long"
    
    # Test hexadecimal UUID representation
    hex_uuid = uuid(as_hex=True)
    assert isinstance(hex_uuid, str), "Expected a string"
    assert len(hex_uuid) == 32, "Hexadecimal UUID should be 32 characters long"
    
    # Additional test to ensure both forms are different
    assert std_uuid != hex_uuid, "Standard and Hexadecimal UUIDs should not be the same"
