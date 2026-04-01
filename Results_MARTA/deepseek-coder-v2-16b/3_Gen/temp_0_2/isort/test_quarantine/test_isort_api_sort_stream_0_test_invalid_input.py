
import pytest
from io import StringIO
from isort.api import sort_stream

def test_sort_stream():
    input_code = """import os
import sys
from datetime import datetime
"""
    expected_output = """import sys
import os
from datetime import datetime
"""
    
    # Using StringIO to simulate file streams
    input_stream = StringIO(input_code)
    output_stream = StringIO()
    
    # Call the function with the mock streams
    result = sort_stream(input_stream, output_stream)
    
    # Read the content from the output stream to compare
    sorted_content = output_stream.getvalue().strip()
    
    assert sorted_content == expected_output.strip(), f"Expected:\n{expected_output}\nGot:\n{sorted_content}"

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

isort/Test4DT_tests/test_isort_api_sort_stream_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_sort_stream _______________________________

    def test_sort_stream():
        input_code = """import os
    import sys
    from datetime import datetime
    """
        expected_output = """import sys
    import os
    from datetime import datetime
    """
    
        # Using StringIO to simulate file streams
        input_stream = StringIO(input_code)
        output_stream = StringIO()
    
        # Call the function with the mock streams
        result = sort_stream(input_stream, output_stream)
    
        # Read the content from the output stream to compare
        sorted_content = output_stream.getvalue().strip()
    
>       assert sorted_content == expected_output.strip(), f"Expected:\n{expected_output}\nGot:\n{sorted_content}"
E       AssertionError: Expected:
E         import sys
E         import os
E         from datetime import datetime
E         
E         Got:
E         import os
E         import sys
E         from datetime import datetime
E       assert 'import os\ni...port datetime' == 'import sys\n...port datetime'
E         
E         + import os
E           import sys
E         - import os
E           from datetime import datetime

isort/Test4DT_tests/test_isort_api_sort_stream_0_test_invalid_input.py:26: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_api_sort_stream_0_test_invalid_input.py::test_sort_stream
============================== 1 failed in 0.13s ===============================
"""