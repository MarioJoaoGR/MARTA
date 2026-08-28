
import pytest
from pysnooper.variables import Keys, Indices, Attrs
from collections.abc import Mapping, Sequence

class Exploding:
    def __init__(self):
        self.source = None
        self.exclude = []
    
    def _items(self, main_value, normalize=False):
        if isinstance(main_value, Mapping):
            cls = Keys
        elif isinstance(main_value, Sequence):
            cls = Indices
        else:
            cls = Attrs
        
        return cls(self.source, self.exclude)._items(main_value, normalize)



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_variables_Exploding__items_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_________________________ test_exploding_items_mapping _________________________

    def test_exploding_items_mapping():
        exploding = Exploding()
        with pytest.raises(NameError):
>           result = exploding._items({"a": 1, "b": 2}, normalize=True)

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_variables_Exploding__items_0.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_variables_Exploding__items_0.py:19: in _items
    return cls(self.source, self.exclude)._items(main_value, normalize)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pysnooper.variables.Keys object at 0x7f73174b21a0>, source = None
exclude = []

    def __init__(self, source, exclude=()):
        self.source = source
        self.exclude = utils.ensure_tuple(exclude)
>       self.code = compile(source, '<variable>', 'eval')
E       TypeError: compile() arg 1 must be a string, bytes or AST object

/opt/marta/baselines/codamosa/replication/test-apps/PySnooper/pysnooper/variables.py:24: TypeError
________________________ test_exploding_items_sequence _________________________

    def test_exploding_items_sequence():
        exploding = Exploding()
        with pytest.raises(NameError):
>           result = exploding._items([3, 4, 5], normalize=False)

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_variables_Exploding__items_0.py:29: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_variables_Exploding__items_0.py:19: in _items
    return cls(self.source, self.exclude)._items(main_value, normalize)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pysnooper.variables.Indices object at 0x7f73174ec4c0>, source = None
exclude = []

    def __init__(self, source, exclude=()):
        self.source = source
        self.exclude = utils.ensure_tuple(exclude)
>       self.code = compile(source, '<variable>', 'eval')
E       TypeError: compile() arg 1 must be a string, bytes or AST object

/opt/marta/baselines/codamosa/replication/test-apps/PySnooper/pysnooper/variables.py:24: TypeError
__________________________ test_exploding_items_other __________________________

    def test_exploding_items_other():
        exploding = Exploding()
        with pytest.raises(NameError):
>           result = exploding._items({"a": 1}, normalize=True)

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_variables_Exploding__items_0.py:34: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_variables_Exploding__items_0.py:19: in _items
    return cls(self.source, self.exclude)._items(main_value, normalize)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pysnooper.variables.Keys object at 0x7f731760f4f0>, source = None
exclude = []

    def __init__(self, source, exclude=()):
        self.source = source
        self.exclude = utils.ensure_tuple(exclude)
>       self.code = compile(source, '<variable>', 'eval')
E       TypeError: compile() arg 1 must be a string, bytes or AST object

/opt/marta/baselines/codamosa/replication/test-apps/PySnooper/pysnooper/variables.py:24: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_variables_Exploding__items_0.py::test_exploding_items_mapping
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_variables_Exploding__items_0.py::test_exploding_items_sequence
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_variables_Exploding__items_0.py::test_exploding_items_other
============================== 3 failed in 0.28s ===============================
"""