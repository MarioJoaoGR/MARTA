
import pytest
from thonny.jedi_utils import get_script_completions


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_get_script_completions_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        source = 'def my_function():\n    pass'
        row, column = 1, 5
        filename = 'example.py'
    
        completions = get_script_completions(source, row, column, filename)
        assert isinstance(completions, list), "Expected a list of completions"
>       assert len(completions) > 0, "Expected at least one completion"
E       AssertionError: Expected at least one completion
E       assert 0 > 0
E        +  where 0 = len([])

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_get_script_completions_1.py:12: AssertionError
________________________________ test_edge_case ________________________________

    def test_edge_case():
        source = None
        row = None
        column = None
        filename = 'example.py'
    
        with pytest.raises(TypeError):
>           get_script_completions(source, row, column, filename)

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_get_script_completions_1.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/thonny/thonny/jedi_utils.py:64: in get_script_completions
    script = jedi.Script(code=source, path=filename, project=_get_new_jedi_project(sys_path))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <[AttributeError("'Script' object has no attribute '_inference_state'") raised in repr()] Script object at 0x7f09d4f2fd60>
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
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_get_script_completions_1.py::test_valid_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_get_script_completions_1.py::test_edge_case
============================== 2 failed in 0.31s ===============================
"""