
import pytest
from isort.wrap_modes import WrapModes
from unittest.mock import patch

def from_string(value: str) -> "WrapModes":
    return getattr(WrapModes, str(value), None) or WrapModes(int(value))

@pytest.mark.parametrize("invalid_input", ["invalid_wrap_mode", 999])
def test_invalid_input(invalid_input):
    with pytest.raises(AttributeError):
        from_string(invalid_input)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort_wrap_modes_from_string_1_test_invalid_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________ test_invalid_input[invalid_wrap_mode] _____________________

invalid_input = 'invalid_wrap_mode'

    @pytest.mark.parametrize("invalid_input", ["invalid_wrap_mode", 999])
    def test_invalid_input(invalid_input):
        with pytest.raises(AttributeError):
>           from_string(invalid_input)

isort/Test4DT_tests/test_isort_wrap_modes_from_string_1_test_invalid_input.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

value = 'invalid_wrap_mode'

    def from_string(value: str) -> "WrapModes":
>       return getattr(WrapModes, str(value), None) or WrapModes(int(value))
E       ValueError: invalid literal for int() with base 10: 'invalid_wrap_mode'

isort/Test4DT_tests/test_isort_wrap_modes_from_string_1_test_invalid_input.py:7: ValueError
___________________________ test_invalid_input[999] ____________________________

invalid_input = 999

    @pytest.mark.parametrize("invalid_input", ["invalid_wrap_mode", 999])
    def test_invalid_input(invalid_input):
        with pytest.raises(AttributeError):
>           from_string(invalid_input)

isort/Test4DT_tests/test_isort_wrap_modes_from_string_1_test_invalid_input.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/Test4DT_tests/test_isort_wrap_modes_from_string_1_test_invalid_input.py:7: in from_string
    return getattr(WrapModes, str(value), None) or WrapModes(int(value))
/usr/local/lib/python3.11/enum.py:714: in __call__
    return cls.__new__(cls, value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <enum 'WrapModes'>, value = 999

    def __new__(cls, value):
        # all enum instances are actually created during class construction
        # without calling this method; this method is called by the metaclass'
        # __call__ (i.e. Color(3) ), and by pickle
        if type(value) is cls:
            # For lookups like Color(Color.RED)
            return value
        # by-value search for a matching enum member
        # see if it's in the reverse mapping (for hashable values)
        try:
            return cls._value2member_map_[value]
        except KeyError:
            # Not found, no need to do long O(n) search
            pass
        except TypeError:
            # not there, now do long search -- O(n) behavior
            for member in cls._member_map_.values():
                if member._value_ == value:
                    return member
        # still not found -- verify that members exist, in-case somebody got here mistakenly
        # (such as via super when trying to override __new__)
        if not cls._member_map_:
            raise TypeError("%r has no members defined" % cls)
        #
        # still not found -- try _missing_ hook
        try:
            exc = None
            result = cls._missing_(value)
        except Exception as e:
            exc = e
            result = None
        try:
            if isinstance(result, cls):
                return result
            elif (
                    Flag is not None and issubclass(cls, Flag)
                    and cls._boundary_ is EJECT and isinstance(result, int)
                ):
                return result
            else:
                ve_exc = ValueError("%r is not a valid %s" % (value, cls.__qualname__))
                if result is None and exc is None:
>                   raise ve_exc
E                   ValueError: 999 is not a valid WrapModes

/usr/local/lib/python3.11/enum.py:1137: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_wrap_modes_from_string_1_test_invalid_input.py::test_invalid_input[invalid_wrap_mode]
FAILED isort/Test4DT_tests/test_isort_wrap_modes_from_string_1_test_invalid_input.py::test_invalid_input[999]
============================== 2 failed in 0.16s ===============================
"""