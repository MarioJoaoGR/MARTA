
import pytest
from unittest.mock import patch
from tqdm.notebook import tqdm_notebook



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_notebook_tqdm_notebook_colour_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_with_colour _________________________

    def test_valid_input_with_colour():
        with patch('tqdm.notebook.display', autospec=True) as mock_display:
>           pb = tqdm_notebook(range(10), colour='green')

/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_notebook_tqdm_notebook_colour_0.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/notebook.py:242: in __init__
    self.container = self.status_printer(self.fp, total, self.desc, self.ncols)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

_ = <tqdm.utils.DisableOnWriteError object at 0x7f28a6f15270>, total = 10
desc = '', ncols = None

    @staticmethod
    def status_printer(_, total=None, desc=None, ncols=None):
        """
        Manage the printing of an IPython/Jupyter Notebook progress bar widget.
        """
        # Fallback to text bar if there's no total
        # DEPRECATED: replaced with an 'info' style bar
        # if not total:
        #    return super(tqdm_notebook, tqdm_notebook).status_printer(file)
    
        # fp = file
    
        # Prepare IPython progress bar
        if IProgress is None:  # #187 #451 #558 #872
>           raise ImportError(
                "IProgress not found. Please update jupyter and ipywidgets."
                " See https://ipywidgets.readthedocs.io/en/stable"
                "/user_install.html")
E           ImportError: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html

/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/notebook.py:115: ImportError
__________________________ test_edge_case_no_display ___________________________

    def test_edge_case_no_display():
        with patch('tqdm.notebook.display', autospec=True) as mock_display:
>           pb = tqdm_notebook(range(10))

/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_notebook_tqdm_notebook_colour_0.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/notebook.py:242: in __init__
    self.container = self.status_printer(self.fp, total, self.desc, self.ncols)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

_ = <tqdm.utils.DisableOnWriteError object at 0x7f28a655ee60>, total = 10
desc = '', ncols = None

    @staticmethod
    def status_printer(_, total=None, desc=None, ncols=None):
        """
        Manage the printing of an IPython/Jupyter Notebook progress bar widget.
        """
        # Fallback to text bar if there's no total
        # DEPRECATED: replaced with an 'info' style bar
        # if not total:
        #    return super(tqdm_notebook, tqdm_notebook).status_printer(file)
    
        # fp = file
    
        # Prepare IPython progress bar
        if IProgress is None:  # #187 #451 #558 #872
>           raise ImportError(
                "IProgress not found. Please update jupyter and ipywidgets."
                " See https://ipywidgets.readthedocs.io/en/stable"
                "/user_install.html")
E           ImportError: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html

/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/notebook.py:115: ImportError
______________________ test_invalid_input_error_handling _______________________

    def test_invalid_input_error_handling():
        with pytest.raises(TypeError):
>           tqdm_notebook(range(10), colour=12345)  # Passing an integer instead of a string should raise TypeError

/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_notebook_tqdm_notebook_colour_0.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/notebook.py:242: in __init__
    self.container = self.status_printer(self.fp, total, self.desc, self.ncols)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

_ = <tqdm.utils.DisableOnWriteError object at 0x7f28a656faf0>, total = 10
desc = '', ncols = None

    @staticmethod
    def status_printer(_, total=None, desc=None, ncols=None):
        """
        Manage the printing of an IPython/Jupyter Notebook progress bar widget.
        """
        # Fallback to text bar if there's no total
        # DEPRECATED: replaced with an 'info' style bar
        # if not total:
        #    return super(tqdm_notebook, tqdm_notebook).status_printer(file)
    
        # fp = file
    
        # Prepare IPython progress bar
        if IProgress is None:  # #187 #451 #558 #872
>           raise ImportError(
                "IProgress not found. Please update jupyter and ipywidgets."
                " See https://ipywidgets.readthedocs.io/en/stable"
                "/user_install.html")
E           ImportError: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html

/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/notebook.py:115: ImportError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_notebook_tqdm_notebook_colour_0.py::test_valid_input_with_colour
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_notebook_tqdm_notebook_colour_0.py::test_edge_case_no_display
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_notebook_tqdm_notebook_colour_0.py::test_invalid_input_error_handling
============================== 3 failed in 0.49s ===============================

Exception ignored in: <function tqdm.__del__ at 0x7f28a80e41f0>
Traceback (most recent call last):
  File "/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/std.py", line 1147, in __del__
    self.close()
  File "/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/notebook.py", line 286, in close
    self.disp(bar_style='danger', check_delay=False)
AttributeError: 'tqdm_notebook' object has no attribute 'disp'
Exception ignored in: <function tqdm.__del__ at 0x7f28a80e41f0>
Traceback (most recent call last):
  File "/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/std.py", line 1147, in __del__
    self.close()
  File "/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/notebook.py", line 286, in close
    self.disp(bar_style='danger', check_delay=False)
AttributeError: 'tqdm_notebook' object has no attribute 'disp'
Exception ignored in: <function tqdm.__del__ at 0x7f28a80e41f0>
Traceback (most recent call last):
  File "/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/std.py", line 1147, in __del__
  File "/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/notebook.py", line 286, in close
AttributeError: 'tqdm_notebook' object has no attribute 'disp'
"""