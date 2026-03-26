
import pytest
from dataclasses import dataclass
from dataclasses_json import dataclass_json
import typing
from dataclasses_json.mm import TOneOrMultiEncoded, TOneOrMulti

@dataclass_json
@dataclass
class SchemaF:
    """Lift Schema into a type constructor"""
    
    def __init__(self, *args, **kwargs):
        """
        Raises exception because this class should not be inherited. This class is helper only.
        """
        super().__init__(*args, **kwargs)
        raise NotImplementedError()

    def load(self, data: TOneOrMultiEncoded, many: typing.Optional[bool] = None, partial: typing.Optional[bool] = None, unknown: typing.Optional[str] = None) -> TOneOrMulti:
        """
        Loads and decodes the provided encoded data using the schema defined in this class.
        
        Parameters:
            data (TOneOrMultiEncoded): The encoded data to be decoded. This should be a type that can be handled by the schema.
            many (bool, optional): If True, expects multiple items in the data; if False or None, expects a single item. Default is None.
            partial (bool, optional): If True, allows decoding of incomplete data; if False or None, requires complete data. Default is None.
            unknown (str, optional): Specifies how to handle unknown fields in the data. Possible values are 'ignore' and 'error'. Default is None.
        
        Returns:
            TOneOrMulti: The decoded data, which can be a single item or a list of items depending on the value of `many`.
        """
        pass

# Test case for error handling in SchemaF class
def test_error_handling():
    schema = SchemaF()
    encoded_data = b'...'  # some binary encoded data
    
    with pytest.raises(NotImplementedError):
        schema.__init__()
        
    with pytest.raises(NotImplementedError):
        schema.load(encoded_data)

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_load_0_test_error_handling.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_error_handling ______________________________

    def test_error_handling():
>       schema = SchemaF()

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_load_0_test_error_handling.py:37: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = SchemaF(), args = (), kwargs = {}

    def __init__(self, *args, **kwargs):
        """
        Raises exception because this class should not be inherited. This class is helper only.
        """
        super().__init__(*args, **kwargs)
>       raise NotImplementedError()
E       NotImplementedError

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_load_0_test_error_handling.py:18: NotImplementedError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF_load_0_test_error_handling.py::test_error_handling
============================== 1 failed in 0.04s ===============================
"""