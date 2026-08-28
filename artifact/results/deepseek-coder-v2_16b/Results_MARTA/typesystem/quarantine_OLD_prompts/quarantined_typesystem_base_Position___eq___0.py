
import pytest
from typesystem.base import Position


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_base_Position___eq___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        pos1 = Position(line_no=1, column_no=5, char_index=20)
        pos2 = None
    
        with pytest.raises(TypeError):
>           assert pos1 == pos2  # Should raise TypeError because of incompatible types
E           assert Position(line_no=1, column_no=5, char_index=20) == None

/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_base_Position___eq___0.py:10: AssertionError
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        pos1 = Position(line_no=1, column_no=5, char_index=20)
        pos2 = 'not a Position'
    
        with pytest.raises(TypeError):
>           assert pos1 == pos2  # Should raise TypeError because of incompatible types
E           AssertionError: assert Position(line_no=1, column_no=5, char_index=20) == 'not a Position'

/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_base_Position___eq___0.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_base_Position___eq___0.py::test_edge_cases
FAILED ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_base_Position___eq___0.py::test_invalid_inputs
============================== 2 failed in 0.13s ===============================
"""