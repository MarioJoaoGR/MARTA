
import pytest
from io import StringIO
from isort.core import process, Config
from isort.settings import DEFAULT_CONFIG

@pytest.mark.parametrize("input_code, expected_output", [
    ("""# This is a test file with unsorted imports
import os
import sys
""", """import os
import sys
"""),
    ("""# This is another test file with unsorted imports
import math
import random
""", """import math
import random
""")
])
def test_valid_case(input_code, expected_output):
    input_stream = StringIO(input_code)
    output_stream = StringIO()
    
    config = Config(line_ending="\n", float_to_top=False, add_imports=[], ignore_whitespace=False)
    result = process(input_stream, output_stream, config=config)
    
    input_stream.seek(0)
    output_stream.seek(0)
    
    assert output_stream.read().strip() == expected_output.strip()

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

isort/Test4DT_tests/test_isort_core_process_1_test_valid_case.py FF      [100%]

=================================== FAILURES ===================================
_ test_valid_case[# This is a test file with unsorted imports\nimport os\nimport sys\n-import os\nimport sys\n] _

input_code = '# This is a test file with unsorted imports\nimport os\nimport sys\n'
expected_output = 'import os\nimport sys\n'

    @pytest.mark.parametrize("input_code, expected_output", [
        ("""# This is a test file with unsorted imports
    import os
    import sys
    """, """import os
    import sys
    """),
        ("""# This is another test file with unsorted imports
    import math
    import random
    """, """import math
    import random
    """)
    ])
    def test_valid_case(input_code, expected_output):
        input_stream = StringIO(input_code)
        output_stream = StringIO()
    
        config = Config(line_ending="\n", float_to_top=False, add_imports=[], ignore_whitespace=False)
        result = process(input_stream, output_stream, config=config)
    
        input_stream.seek(0)
        output_stream.seek(0)
    
>       assert output_stream.read().strip() == expected_output.strip()
E       AssertionError: assert '# This is a ...s\nimport sys' == 'import os\nimport sys'
E         
E         + # This is a test file with unsorted imports
E           import os
E           import sys

isort/Test4DT_tests/test_isort_core_process_1_test_valid_case.py:31: AssertionError
_ test_valid_case[# This is another test file with unsorted imports\nimport math\nimport random\n-import math\nimport random\n] _

input_code = '# This is another test file with unsorted imports\nimport math\nimport random\n'
expected_output = 'import math\nimport random\n'

    @pytest.mark.parametrize("input_code, expected_output", [
        ("""# This is a test file with unsorted imports
    import os
    import sys
    """, """import os
    import sys
    """),
        ("""# This is another test file with unsorted imports
    import math
    import random
    """, """import math
    import random
    """)
    ])
    def test_valid_case(input_code, expected_output):
        input_stream = StringIO(input_code)
        output_stream = StringIO()
    
        config = Config(line_ending="\n", float_to_top=False, add_imports=[], ignore_whitespace=False)
        result = process(input_stream, output_stream, config=config)
    
        input_stream.seek(0)
        output_stream.seek(0)
    
>       assert output_stream.read().strip() == expected_output.strip()
E       AssertionError: assert '# This is an...import random' == 'import math\nimport random'
E         
E         + # This is another test file with unsorted imports
E           import math
E           import random

isort/Test4DT_tests/test_isort_core_process_1_test_valid_case.py:31: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_core_process_1_test_valid_case.py::test_valid_case[# This is a test file with unsorted imports\nimport os\nimport sys\n-import os\nimport sys\n]
FAILED isort/Test4DT_tests/test_isort_core_process_1_test_valid_case.py::test_valid_case[# This is another test file with unsorted imports\nimport math\nimport random\n-import math\nimport random\n]
============================== 2 failed in 0.14s ===============================
"""