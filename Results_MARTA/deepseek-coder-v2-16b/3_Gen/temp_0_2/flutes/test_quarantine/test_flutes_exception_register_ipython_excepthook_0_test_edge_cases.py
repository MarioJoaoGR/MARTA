
import sys
from typing import List, Type
from unittest.mock import patch
from flutes.exception import ultratb
from IPython.core import ultratb as ipy_ultratb

def test_register_ipython_excepthook():
    with patch('flutes.exception.ultratb.FormattedTB', new=ipy_ultratb.FormattedTB) as mock_formattetb:
        from flutes.exception import register_ipython_excepthook
        register_ipython_excepthook()
        assert mock_formattetb.called

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_exception_register_ipython_excepthook_0_test_edge_cases
flutes/Test4DT_tests/test_flutes_exception_register_ipython_excepthook_0_test_edge_cases.py:5:0: E0611: No name 'ultratb' in module 'flutes.exception' (no-name-in-module)


"""