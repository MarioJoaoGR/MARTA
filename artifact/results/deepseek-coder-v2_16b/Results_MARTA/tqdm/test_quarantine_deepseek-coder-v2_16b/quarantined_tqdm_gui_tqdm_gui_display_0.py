
import pytest
from tqdm.gui import tqdm_gui



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_gui_tqdm_gui_display_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
____________________________ test_tqdm_gui_default _____________________________

    def test_tqdm_gui_default():
>       for i in tqdm_gui(range(100)):

/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_gui_tqdm_gui_display_0.py:6: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <tqdm.gui.tqdm_gui object at 0x7fc6c0947220>, args = (range(0, 100),)
kwargs = {}, deque = <class 'collections.deque'>

    def __init__(self, *args, **kwargs):
        from collections import deque
    
>       import matplotlib as mpl
E       ModuleNotFoundError: No module named 'matplotlib'

/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/gui.py:32: ModuleNotFoundError
__________________________ test_tqdm_gui_custom_color __________________________

    def test_tqdm_gui_custom_color():
>       for i in tqdm_gui(range(100), colour='r'):

/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_gui_tqdm_gui_display_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <tqdm.gui.tqdm_gui object at 0x7fc6bbf23ca0>, args = (range(0, 100),)
kwargs = {'colour': 'r'}, deque = <class 'collections.deque'>

    def __init__(self, *args, **kwargs):
        from collections import deque
    
>       import matplotlib as mpl
E       ModuleNotFoundError: No module named 'matplotlib'

/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/gui.py:32: ModuleNotFoundError
___________________________ test_tqdm_gui_enable_gui ___________________________

    def test_tqdm_gui_enable_gui():
>       for i in tqdm_gui(range(100), gui=True):

/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_gui_tqdm_gui_display_0.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <tqdm.gui.tqdm_gui object at 0x7fc6c0a9b190>, args = (range(0, 100),)
kwargs = {'gui': True}, deque = <class 'collections.deque'>

    def __init__(self, *args, **kwargs):
        from collections import deque
    
>       import matplotlib as mpl
E       ModuleNotFoundError: No module named 'matplotlib'

/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/gui.py:32: ModuleNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_gui_tqdm_gui_display_0.py::test_tqdm_gui_default
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_gui_tqdm_gui_display_0.py::test_tqdm_gui_custom_color
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_gui_tqdm_gui_display_0.py::test_tqdm_gui_enable_gui
============================== 3 failed in 0.07s ===============================

Exception ignored in: <function tqdm.__del__ at 0x7fc6c096cdc0>
Traceback (most recent call last):
  File "/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/std.py", line 1147, in __del__
    self.close()
  File "/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/gui.py", line 91, in close
    if self.disable:
AttributeError: 'tqdm_gui' object has no attribute 'disable'
Exception ignored in: <function tqdm.__del__ at 0x7fc6c096cdc0>
Traceback (most recent call last):
  File "/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/std.py", line 1147, in __del__
    self.close()
  File "/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/gui.py", line 91, in close
    if self.disable:
AttributeError: 'tqdm_gui' object has no attribute 'disable'
Exception ignored in: <function tqdm.__del__ at 0x7fc6c096cdc0>
Traceback (most recent call last):
  File "/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/std.py", line 1147, in __del__
  File "/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/gui.py", line 91, in close
AttributeError: 'tqdm_gui' object has no attribute 'disable'
"""