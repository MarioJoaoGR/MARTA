
# Module: isort.core
import pytest
from io import StringIO
from isort import process, Config
from isort.settings import DEFAULT_CONFIG
from isort.exceptions import FileSkipComment  # Importing the exception here

def test_process_with_default_settings():
    input_stream = StringIO("""import os
import sys
""")
    output_stream = StringIO()
    
    made_changes = process(input_stream, output_stream)
    
    assert output_stream.getvalue().strip() == "import os\nimport sys"
    assert made_changes is True

def test_process_with_custom_extension():
    input_stream = StringIO("""# isort: off
import os
import sys
# isort: on
""")
    output_stream = StringIO()
    
    made_changes = process(input_stream, output_stream, extension="txt", raise_on_skip=False)
    
    assert output_stream.getvalue().strip() == "import os\nimport sys"
    assert made_changes is True

def test_process_with_custom_config():
    input_stream = StringIO("""import os
import sys
""")
    output_stream = StringIO()
    
    config = Config(sections=('standard', 'thirdparty'))
    made_changes = process(input_stream, output_stream, config=config)
    
    assert output_stream.getvalue().strip() == "import os\nimport sys"
    assert made_changes is True

def test_process_with_skip_comment():
    input_stream = StringIO("""# isort: off
import os
import sys
# isort: on
""")
    output_stream = StringIO()
    
    with pytest.raises(FileSkipComment):
        process(input_stream, output_stream, raise_on_skip=True)

def test_process_with_no_raise_on_skip():
    input_stream = StringIO("""# isort: off
import os
import sys
# isort: on
""")
    output_stream = StringIO()
    
    made_changes = process(input_stream, output_stream, raise_on_skip=False)
    
    assert output_stream.getvalue().strip() == "import os\nimport sys"
    assert made_changes is True

def test_process_with_no_changes():
    input_stream = StringIO("""import os
import sys
""")
    output_stream = StringIO()
    
    made_changes = process(input_stream, output_stream)
    
    assert output_stream.getvalue().strip() == "import os\nimport sys"
    assert made_changes is False

def test_process_with_float_to_top():
    input_stream = StringIO("""# isort: off
import os
import sys
# isort: on
""")
    output_stream = StringIO()
    
    made_changes = process(input_stream, output_stream, config=Config(float_to_top=True))
    
    assert output_stream.getvalue().strip() == "import os\nimport sys"
    assert made_changes is True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_core_process_0
isort/Test4DT_tests/test_isort_core_process_0.py:5:0: E0611: No name 'process' in module 'isort' (no-name-in-module)


"""