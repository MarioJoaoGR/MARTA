
from isort.main import WrapModes  # Import the WrapModes enum from isort.main module

def test_valid_wrapmodes():
    # Arrange
    test_enum = WrapModes.MODE_A
    
    # Act and Assert
    assert test_enum == WrapModes.MODE_A

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_main__preconvert_0_test_valid_wrapmodes.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_valid_wrapmodes _____________________________

    def test_valid_wrapmodes():
        # Arrange
>       test_enum = WrapModes.MODE_A

isort/Test4DT_tests/test_isort_main__preconvert_0_test_valid_wrapmodes.py:6: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <enum 'WrapModes'>, name = 'MODE_A'

    def __getattr__(cls, name):
        """
        Return the enum member matching `name`
    
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        if _is_dunder(name):
            raise AttributeError(name)
        try:
            return cls._member_map_[name]
        except KeyError:
>           raise AttributeError(name) from None
E           AttributeError: MODE_A

/usr/local/lib/python3.11/enum.py:786: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_main__preconvert_0_test_valid_wrapmodes.py::test_valid_wrapmodes
============================== 1 failed in 0.13s ===============================
"""