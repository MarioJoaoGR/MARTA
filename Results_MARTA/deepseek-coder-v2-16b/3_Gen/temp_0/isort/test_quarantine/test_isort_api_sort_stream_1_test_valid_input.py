
import io
import pytest
from unittest.mock import MagicMock, patch
from isort.api import sort_stream, DEFAULT_CONFIG

@pytest.mark.parametrize("show_diff", [True, False])
def test_valid_input(show_diff):
    # Arrange
    input_code = "import os\nimport sys"
    expected_output = "import sys\nimport os"
    
    input_stream = io.StringIO(input_code)
    output_stream = io.StringIO()
    
    with patch('isort.api.DEFAULT_CONFIG', MagicMock()) as mock_config:
        # Act
        result = sort_stream(input_stream, output_stream, show_diff=show_diff)
        
        # Assert
        input_stream.seek(0)
        sorted_content = input_stream.read()
        assert sorted_content == expected_output, f"Expected {expected_output}, but got {sorted_content}"
        
        if show_diff:
            output_stream.seek(0)
            diff_output = output_stream.getvalue().strip()
            assert diff_output == "", "Diff should be empty when show_diff is True"

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

isort/Test4DT_tests/test_isort_api_sort_stream_1_test_valid_input.py FF  [100%]

=================================== FAILURES ===================================
____________________________ test_valid_input[True] ____________________________

show_diff = True

    @pytest.mark.parametrize("show_diff", [True, False])
    def test_valid_input(show_diff):
        # Arrange
        input_code = "import os\nimport sys"
        expected_output = "import sys\nimport os"
    
        input_stream = io.StringIO(input_code)
        output_stream = io.StringIO()
    
        with patch('isort.api.DEFAULT_CONFIG', MagicMock()) as mock_config:
            # Act
            result = sort_stream(input_stream, output_stream, show_diff=show_diff)
    
            # Assert
            input_stream.seek(0)
            sorted_content = input_stream.read()
>           assert sorted_content == expected_output, f"Expected {expected_output}, but got {sorted_content}"
E           AssertionError: Expected import sys
E             import os, but got import os
E             import sys
E           assert 'import os\nimport sys' == 'import sys\nimport os'
E             
E             + import os
E             - import sys
E             ?           -
E             + import sys
E             - import os

isort/Test4DT_tests/test_isort_api_sort_stream_1_test_valid_input.py:23: AssertionError
___________________________ test_valid_input[False] ____________________________

show_diff = False

    @pytest.mark.parametrize("show_diff", [True, False])
    def test_valid_input(show_diff):
        # Arrange
        input_code = "import os\nimport sys"
        expected_output = "import sys\nimport os"
    
        input_stream = io.StringIO(input_code)
        output_stream = io.StringIO()
    
        with patch('isort.api.DEFAULT_CONFIG', MagicMock()) as mock_config:
            # Act
            result = sort_stream(input_stream, output_stream, show_diff=show_diff)
    
            # Assert
            input_stream.seek(0)
            sorted_content = input_stream.read()
>           assert sorted_content == expected_output, f"Expected {expected_output}, but got {sorted_content}"
E           AssertionError: Expected import sys
E             import os, but got import os
E             import sys
E           assert 'import os\nimport sys' == 'import sys\nimport os'
E             
E             + import os
E             - import sys
E             ?           -
E             + import sys
E             - import os

isort/Test4DT_tests/test_isort_api_sort_stream_1_test_valid_input.py:23: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_api_sort_stream_1_test_valid_input.py::test_valid_input[True]
FAILED isort/Test4DT_tests/test_isort_api_sort_stream_1_test_valid_input.py::test_valid_input[False]
============================== 2 failed in 0.14s ===============================
"""