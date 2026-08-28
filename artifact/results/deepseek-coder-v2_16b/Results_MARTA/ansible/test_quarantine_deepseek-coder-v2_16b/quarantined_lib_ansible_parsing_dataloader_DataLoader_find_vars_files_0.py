
import pytest
from ansible.parsing.dataloader import DataLoader
import os


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_dataloader_DataLoader_find_vars_files_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
________________________ test_edge_case_find_vars_files ________________________

    def test_edge_case_find_vars_files():
        dl = DataLoader()
        with pytest.raises(ValueError) as excinfo:
>           dl.find_vars_files('.', None, None, False)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_dataloader_DataLoader_find_vars_files_0.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/parsing/dataloader.py:427: in find_vars_files
    b_path = to_bytes(os.path.join(path, name))
/opt/conda/envs/test4py_env/lib/python3.10/posixpath.py:90: in join
    genericpath._check_arg_types('join', a, *p)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

funcname = 'join', args = ('.', None), hasstr = True, hasbytes = False, s = None

    def _check_arg_types(funcname, *args):
        hasstr = hasbytes = False
        for s in args:
            if isinstance(s, str):
                hasstr = True
            elif isinstance(s, bytes):
                hasbytes = True
            else:
>               raise TypeError(f'{funcname}() argument must be str, bytes, or '
                                f'os.PathLike object, not {s.__class__.__name__!r}') from None
E               TypeError: join() argument must be str, bytes, or os.PathLike object, not 'NoneType'

/opt/conda/envs/test4py_env/lib/python3.10/genericpath.py:152: TypeError
______________________ test_invalid_input_find_vars_files ______________________

    def test_invalid_input_find_vars_files():
        dl = DataLoader()
        with pytest.raises(TypeError) as excinfo:
            dl.find_vars_files(123, 'config', ['.json'], True)
>       assert str(excinfo.value) == "path must be a string"
E       AssertionError: assert 'expected str...ject, not int' == 'path must be a string'
E         
E         - path must be a string
E         + expected str, bytes or os.PathLike object, not int

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_dataloader_DataLoader_find_vars_files_0.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_dataloader_DataLoader_find_vars_files_0.py::test_edge_case_find_vars_files
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_dataloader_DataLoader_find_vars_files_0.py::test_invalid_input_find_vars_files
============================== 2 failed in 0.28s ===============================
"""