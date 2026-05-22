
import pytest
from unittest.mock import patch
from httpie.config import Config, DEFAULT_CONFIG_DIR

def test_edge_case():
    with patch('httpie.config.DEFAULT_CONFIG_DIR', None):
        config = Config(None)
        assert config.directory is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_codestral/test_httpie_config_Config___init___0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        with patch('httpie.config.DEFAULT_CONFIG_DIR', None):
>           config = Config(None)

httpie/Test4DT_tests_codestral/test_httpie_config_Config___init___0_test_edge_case.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/config.py:144: in __init__
    self.directory = Path(directory)
/usr/local/lib/python3.11/pathlib.py:871: in __new__
    self = cls._from_parts(args)
/usr/local/lib/python3.11/pathlib.py:509: in _from_parts
    drv, root, parts = self._parse_args(args)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'pathlib.PosixPath'>, args = (None,)

    @classmethod
    def _parse_args(cls, args):
        # This is useful when you don't want to create an instance, just
        # canonicalize some constructor arguments.
        parts = []
        for a in args:
            if isinstance(a, PurePath):
                parts += a._parts
            else:
>               a = os.fspath(a)
E               TypeError: expected str, bytes or os.PathLike object, not NoneType

/usr/local/lib/python3.11/pathlib.py:493: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_config_Config___init___0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.12s ===============================
"""