
import pytest
from dataclasses_json.core import _support_extended_types
from datetime import datetime, timezone
from decimal import Decimal
from uuid import UUID

def test_valid_inputs():
    # Test with datetime
    field_type = datetime
    field_value = 1633072800  # Timestamp equivalent to a specific date and time
    assert isinstance(_support_extended_types(field_type, field_value), datetime)
    
    # Test with Decimal
    field_type = Decimal
    field_value = "123.45"
    assert isinstance(_support_extended_types(field_type, field_value), Decimal)
    
    # Test with UUID
    field_type = UUID
    field_value = "a1b2c3d4-e5f6-7789-a0b1-c2d3e4f5g6h7"
    assert isinstance(_support_extended_types(field_type, field_value), UUID)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__support_extended_types_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Test with datetime
        field_type = datetime
        field_value = 1633072800  # Timestamp equivalent to a specific date and time
        assert isinstance(_support_extended_types(field_type, field_value), datetime)
    
        # Test with Decimal
        field_type = Decimal
        field_value = "123.45"
        assert isinstance(_support_extended_types(field_type, field_value), Decimal)
    
        # Test with UUID
        field_type = UUID
        field_value = "a1b2c3d4-e5f6-7789-a0b1-c2d3e4f5g6h7"
>       assert isinstance(_support_extended_types(field_type, field_value), UUID)

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__support_extended_types_0_test_valid_inputs.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
dataclasses-json/dataclasses_json/core.py:270: in _support_extended_types
    else UUID(field_value))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'UUID' object has no attribute 'int'") raised in repr()] UUID object at 0x1028e4dc0>
hex = 'a1b2c3d4e5f67789a0b1c2d3e4f5g6h7', bytes = None, bytes_le = None
fields = None, int = None, version = None

    def __init__(self, hex=None, bytes=None, bytes_le=None, fields=None,
                       int=None, version=None,
                       *, is_safe=SafeUUID.unknown):
        r"""Create a UUID from either a string of 32 hexadecimal digits,
        a string of 16 bytes as the 'bytes' argument, a string of 16 bytes
        in little-endian order as the 'bytes_le' argument, a tuple of six
        integers (32-bit time_low, 16-bit time_mid, 16-bit time_hi_version,
        8-bit clock_seq_hi_variant, 8-bit clock_seq_low, 48-bit node) as
        the 'fields' argument, or a single 128-bit integer as the 'int'
        argument.  When a string of hex digits is given, curly braces,
        hyphens, and a URN prefix are all optional.  For example, these
        expressions all yield the same UUID:
    
        UUID('{12345678-1234-5678-1234-567812345678}')
        UUID('12345678123456781234567812345678')
        UUID('urn:uuid:12345678-1234-5678-1234-567812345678')
        UUID(bytes='\x12\x34\x56\x78'*4)
        UUID(bytes_le='\x78\x56\x34\x12\x34\x12\x78\x56' +
                      '\x12\x34\x56\x78\x12\x34\x56\x78')
        UUID(fields=(0x12345678, 0x1234, 0x5678, 0x12, 0x34, 0x567812345678))
        UUID(int=0x12345678123456781234567812345678)
    
        Exactly one of 'hex', 'bytes', 'bytes_le', 'fields', or 'int' must
        be given.  The 'version' argument is optional; if given, the resulting
        UUID will have its variant and version set according to RFC 4122,
        overriding the given 'hex', 'bytes', 'bytes_le', 'fields', or 'int'.
    
        is_safe is an enum exposed as an attribute on the instance.  It
        indicates whether the UUID has been generated in a way that is safe
        for multiprocessing applications, via uuid_generate_time_safe(3).
        """
    
        if [hex, bytes, bytes_le, fields, int].count(None) != 4:
            raise TypeError('one of the hex, bytes, bytes_le, fields, '
                            'or int arguments must be given')
        if hex is not None:
            hex = hex.replace('urn:', '').replace('uuid:', '')
            hex = hex.strip('{}').replace('-', '')
            if len(hex) != 32:
                raise ValueError('badly formed hexadecimal UUID string')
>           int = int_(hex, 16)
E           ValueError: invalid literal for int() with base 16: 'a1b2c3d4e5f67789a0b1c2d3e4f5g6h7'

/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/uuid.py:178: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__support_extended_types_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.04s ===============================
"""