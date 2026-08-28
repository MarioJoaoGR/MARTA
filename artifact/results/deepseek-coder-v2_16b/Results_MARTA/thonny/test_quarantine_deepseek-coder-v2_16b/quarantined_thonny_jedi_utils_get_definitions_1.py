
import pytest
from thonny.jedi_utils import get_definitions



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_get_definitions_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        source = "def hello(): pass"
        filename = "example.py"
        row, column = 0, 4
>       definitions = get_definitions(source, row, column, filename)

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_get_definitions_1.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/thonny/thonny/jedi_utils.py:131: in get_definitions
    return script.infer(line=row, column=column)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <Script: 'example.py' <SameEnvironment: 3.10.20 in /opt/conda/envs/test4py_env>>
line = 0, column = 4, args = (), kwargs = {}

    @wraps(func)
    def wrapper(self, line=None, column=None, *args, **kwargs):
        line = max(len(self._code_lines), 1) if line is None else line
        if not (0 < line <= len(self._code_lines)):
>           raise ValueError('`line` parameter is not in a valid range.')
E           ValueError: `line` parameter is not in a valid range.

/data/pydeps/marta/jedi/api/helpers.py:473: ValueError
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        source = None
        filename = "example.py"
        row, column = 0, 4
        with pytest.raises(TypeError):
>           get_definitions(source, row, column, filename)

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_get_definitions_1.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/thonny/thonny/jedi_utils.py:130: in get_definitions
    script = jedi.Script(code=source, path=filename)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'Script' object has no attribute '_inference_state'") raised in repr()] Script object at 0x7f6ba145ae60>
code = None

    def __init__(self, code=None, *, path=None, environment=None, project=None):
        self._orig_path = path
        if isinstance(path, str):
            path = Path(path)
    
        self.path = path.absolute() if path else None
    
        if code is None:
            if path is None:
                raise ValueError("Must provide at least one of code or path")
    
            # TODO add a better warning than the traceback!
>           with open(path, 'rb') as f:
E           FileNotFoundError: [Errno 2] No such file or directory: 'example.py'

/data/pydeps/marta/jedi/api/__init__.py:112: FileNotFoundError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        source = "def hello() pass"
        filename = "example.py"
        row, column = 0, 4
        with pytest.raises(SyntaxError):
>           get_definitions(source, row, column, filename)

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_get_definitions_1.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/thonny/thonny/jedi_utils.py:131: in get_definitions
    return script.infer(line=row, column=column)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <Script: 'example.py' <SameEnvironment: 3.10.20 in /opt/conda/envs/test4py_env>>
line = 0, column = 4, args = (), kwargs = {}

    @wraps(func)
    def wrapper(self, line=None, column=None, *args, **kwargs):
        line = max(len(self._code_lines), 1) if line is None else line
        if not (0 < line <= len(self._code_lines)):
>           raise ValueError('`line` parameter is not in a valid range.')
E           ValueError: `line` parameter is not in a valid range.

/data/pydeps/marta/jedi/api/helpers.py:473: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_get_definitions_1.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_get_definitions_1.py::test_edge_case_none
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_get_definitions_1.py::test_invalid_input
============================== 3 failed in 0.32s ===============================
"""