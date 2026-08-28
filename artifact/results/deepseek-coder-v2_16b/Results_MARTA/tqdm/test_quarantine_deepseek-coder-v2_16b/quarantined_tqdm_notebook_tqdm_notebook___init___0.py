
import pytest
from tqdm.notebook import tqdm_notebook
import time


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_notebook_tqdm_notebook___init___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
>       for i in tqdm_notebook(range(10)):

/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_notebook_tqdm_notebook___init___0.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/notebook.py:242: in __init__
    self.container = self.status_printer(self.fp, total, self.desc, self.ncols)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

_ = <tqdm.utils.DisableOnWriteError object at 0x7f09f49cc1c0>, total = 10
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
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        args = [None]
        kwargs = {}
>       pb = tqdm_notebook(*args, **kwargs)

/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_notebook_tqdm_notebook___init___0.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/notebook.py:242: in __init__
    self.container = self.status_printer(self.fp, total, self.desc, self.ncols)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

_ = <tqdm.utils.DisableOnWriteError object at 0x7f09f4a0fee0>, total = None
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
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_notebook_tqdm_notebook___init___0.py::test_valid_input_happy_path
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_notebook_tqdm_notebook___init___0.py::test_edge_case_none
============================== 2 failed in 0.47s ===============================

Exception ignored in: <function tqdm.__del__ at 0x7f09f5ba9c60>
Traceback (most recent call last):
  File "/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/std.py", line 1147, in __del__
    self.close()
  File "/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/notebook.py", line 286, in close
    self.disp(bar_style='danger', check_delay=False)
AttributeError: 'tqdm_notebook' object has no attribute 'disp'
Exception ignored in: <function tqdm.__del__ at 0x7f09f5ba9c60>
Traceback (most recent call last):
  File "/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/std.py", line 1147, in __del__
  File "/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/notebook.py", line 289, in close
AttributeError: 'tqdm_notebook' object has no attribute 'disp'
"""