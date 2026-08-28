
import pytest
from ansible.module_utils.pycompat24 import literal_eval


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_pycompat24_literal_eval_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_valid_case_string ____________________________

    def test_valid_case_string():
>       result = literal_eval('1 + 2')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_pycompat24_literal_eval_0.py:6: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:110: in literal_eval
    return _convert(node_or_string)
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:109: in _convert
    return _convert_signed_num(node)
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:83: in _convert_signed_num
    return _convert_num(node)
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:74: in _convert_num
    _raise_malformed_node(node)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

node = <ast.BinOp object at 0x7f8f7c6f9690>

    def _raise_malformed_node(node):
        msg = "malformed node or string"
        if lno := getattr(node, 'lineno', None):
            msg += f' on line {lno}'
>       raise ValueError(msg + f': {node!r}')
E       ValueError: malformed node or string on line 1: <ast.BinOp object at 0x7f8f7c6f9690>

/opt/conda/envs/test4py_env/lib/python3.10/ast.py:71: ValueError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(ValueError):
>           literal_eval('invalid input')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_pycompat24_literal_eval_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/ast.py:64: in literal_eval
    node_or_string = parse(node_or_string.lstrip(" \t"), mode='eval')
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

source = 'invalid input', filename = '<unknown>', mode = 'eval'

    def parse(source, filename='<unknown>', mode='exec', *,
              type_comments=False, feature_version=None):
        """
        Parse the source into an AST node.
        Equivalent to compile(source, filename, mode, PyCF_ONLY_AST).
        Pass type_comments=True to get back type comments where the syntax allows.
        """
        flags = PyCF_ONLY_AST
        if type_comments:
            flags |= PyCF_TYPE_COMMENTS
        if isinstance(feature_version, tuple):
            major, minor = feature_version  # Should be a 2-tuple.
            assert major == 3
            feature_version = minor
        elif feature_version is None:
            feature_version = -1
        # Else it should be an int giving the minor version for 3.x.
>       return compile(source, filename, mode, flags,
                       _feature_version=feature_version)
E         File "<unknown>", line 1
E           invalid input
E                   ^^^^^
E       SyntaxError: invalid syntax

/opt/conda/envs/test4py_env/lib/python3.10/ast.py:50: SyntaxError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_pycompat24_literal_eval_0.py::test_valid_case_string
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_pycompat24_literal_eval_0.py::test_invalid_input
============================== 2 failed in 0.39s ===============================
"""