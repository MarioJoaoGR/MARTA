
import pytest
import os
import collections
import typing
from pytutils.env import load_env_file

def parse_env_file_contents(lines: typing.Iterable[str]) -> typing.List[typing.Tuple[str, str]]:
    values = []
    for line in lines:
        if '=' in line:
            key, value = line.split('=', 1)
            values.append((key.strip(), value.strip()))
    return values

def expand(value: str) -> str:
    expanded_value = os.path.expanduser(value)
    if '$PATH' in expanded_value:
        expanded_value = expanded_value.replace('$PATH', os.getenv('PATH', ''))
    return expanded_value


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_env_load_env_file_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        lines = ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
        result = load_env_file(lines)
        assert isinstance(result, collections.OrderedDict), "Result should be an OrderedDict"
        assert len(result) == 3, "Expected 3 key-value pairs in the result"
>       assert result['TEST'] == os.path.expanduser('~/yeee-$PATH'), f"Expected {os.path.expanduser('~/yeee-$PATH')} but got {result['TEST']}"
E       AssertionError: Expected /home/joaovitorino/yeee-$PATH but got /home/joaovitorino/yeee-/opt/conda/bin:/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
E       assert '/home/joaovi...in:/sbin:/bin' == '/home/joaovi...no/yeee-$PATH'
E         
E         - /home/joaovitorino/yeee-$PATH
E         + /home/joaovitorino/yeee-/opt/conda/bin:/usr/local/nvidia/bin:/usr/local/cuda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_env_load_env_file_0.py:27: AssertionError
_____________________________ test_invalid_format ______________________________

    def test_invalid_format():
        lines = ['INVALIDFORMATTEST', 'THISIS=~/a/test']
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_env_load_env_file_0.py:31: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_env_load_env_file_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_env_load_env_file_0.py::test_invalid_format
============================== 2 failed in 0.05s ===============================
"""