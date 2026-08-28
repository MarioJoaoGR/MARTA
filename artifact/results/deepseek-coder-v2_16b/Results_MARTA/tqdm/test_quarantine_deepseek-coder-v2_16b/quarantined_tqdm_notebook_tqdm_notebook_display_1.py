
import pytest
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

../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_notebook_tqdm_notebook_display_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
>       pb = tqdm_notebook(range(10))

/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_notebook_tqdm_notebook_display_1.py:6: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/notebook.py:242: in __init__
    self.container = self.status_printer(self.fp, total, self.desc, self.ncols)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

_ = <tqdm.utils.DisableOnWriteError object at 0x7f354e7a1810>, total = 10
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
__________________________ test_edge_case_none_input ___________________________

    def test_edge_case_none_input():
        with pytest.raises(TypeError):
>           pb = tqdm_notebook(range=None)

/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_notebook_tqdm_notebook_display_1.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/notebook.py:231: in __init__
    super(tqdm_notebook, self).__init__(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <tqdm.notebook.tqdm_notebook object at 0x7f354e805ed0>, iterable = None
desc = None, total = None, leave = True
file = <tqdm.utils.DisableOnWriteError object at 0x7f354e805ea0>, ncols = None
mininterval = 0.1, maxinterval = 10.0, miniters = None, ascii = None
disable = False, unit = 'it', unit_scale = False, dynamic_ncols = False
smoothing = 0.3, bar_format = None, initial = 0, position = None, postfix = None
unit_divisor = 1000, write_bytes = False, lock_args = None, nrows = None
colour = None, delay = 0, gui = True, kwargs = {'range': None}

    def __init__(self, iterable=None, desc=None, total=None, leave=True, file=None,
                 ncols=None, mininterval=0.1, maxinterval=10.0, miniters=None,
                 ascii=None, disable=False, unit='it', unit_scale=False,
                 dynamic_ncols=False, smoothing=0.3, bar_format=None, initial=0,
                 position=None, postfix=None, unit_divisor=1000, write_bytes=None,
                 lock_args=None, nrows=None, colour=None, delay=0, gui=False,
                 **kwargs):
        """
        Parameters
        ----------
        iterable  : iterable, optional
            Iterable to decorate with a progressbar.
            Leave blank to manually manage the updates.
        desc  : str, optional
            Prefix for the progressbar.
        total  : int or float, optional
            The number of expected iterations. If unspecified,
            len(iterable) is used if possible. If float("inf") or as a last
            resort, only basic progress statistics are displayed
            (no ETA, no progressbar).
            If `gui` is True and this parameter needs subsequent updating,
            specify an initial arbitrary large positive number,
            e.g. 9e9.
        leave  : bool, optional
            If [default: True], keeps all traces of the progressbar
            upon termination of iteration.
            If `None`, will leave only if `position` is `0`.
        file  : `io.TextIOWrapper` or `io.StringIO`, optional
            Specifies where to output the progress messages
            (default: sys.stderr). Uses `file.write(str)` and `file.flush()`
            methods.  For encoding, see `write_bytes`.
        ncols  : int, optional
            The width of the entire output message. If specified,
            dynamically resizes the progressbar to stay within this bound.
            If unspecified, attempts to use environment width. The
            fallback is a meter width of 10 and no limit for the counter and
            statistics. If 0, will not print any meter (only stats).
        mininterval  : float, optional
            Minimum progress display update interval [default: 0.1] seconds.
        maxinterval  : float, optional
            Maximum progress display update interval [default: 10] seconds.
            Automatically adjusts `miniters` to correspond to `mininterval`
            after long display update lag. Only works if `dynamic_miniters`
            or monitor thread is enabled.
        miniters  : int or float, optional
            Minimum progress display update interval, in iterations.
            If 0 and `dynamic_miniters`, will automatically adjust to equal
            `mininterval` (more CPU efficient, good for tight loops).
            If > 0, will skip display of specified number of iterations.
            Tweak this and `mininterval` to get very efficient loops.
            If your progress is erratic with both fast and slow iterations
            (network, skipping items, etc) you should set miniters=1.
        ascii  : bool or str, optional
            If unspecified or False, use unicode (smooth blocks) to fill
            the meter. The fallback is to use ASCII characters " 123456789#".
        disable  : bool, optional
            Whether to disable the entire progressbar wrapper
            [default: False]. If set to None, disable on non-TTY.
        unit  : str, optional
            String that will be used to define the unit of each iteration
            [default: it].
        unit_scale  : bool or int or float, optional
            If 1 or True, the number of iterations will be reduced/scaled
            automatically and a metric prefix following the
            International System of Units standard will be added
            (kilo, mega, etc.) [default: False]. If any other non-zero
            number, will scale `total` and `n`.
        dynamic_ncols  : bool, optional
            If set, constantly alters `ncols` and `nrows` to the
            environment (allowing for window resizes) [default: False].
        smoothing  : float, optional
            Exponential moving average smoothing factor for speed estimates
            (ignored in GUI mode). Ranges from 0 (average speed) to 1
            (current/instantaneous speed) [default: 0.3].
        bar_format  : str, optional
            Specify a custom bar string formatting. May impact performance.
            [default: '{l_bar}{bar}{r_bar}'], where
            l_bar='{desc}: {percentage:3.0f}%|' and
            r_bar='| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, '
              '{rate_fmt}{postfix}]'
            Possible vars: l_bar, bar, r_bar, n, n_fmt, total, total_fmt,
              percentage, elapsed, elapsed_s, ncols, nrows, desc, unit,
              rate, rate_fmt, rate_noinv, rate_noinv_fmt,
              rate_inv, rate_inv_fmt, postfix, unit_divisor,
              remaining, remaining_s, eta.
            Note that a trailing ": " is automatically removed after {desc}
            if the latter is empty.
        initial  : int or float, optional
            The initial counter value. Useful when restarting a progress
            bar [default: 0]. If using float, consider specifying `{n:.3f}`
            or similar in `bar_format`, or specifying `unit_scale`.
        position  : int, optional
            Specify the line offset to print this bar (starting from 0)
            Automatic if unspecified.
            Useful to manage multiple bars at once (eg, from threads).
        postfix  : dict or *, optional
            Specify additional stats to display at the end of the bar.
            Calls `set_postfix(**postfix)` if possible (dict).
        unit_divisor  : float, optional
            [default: 1000], ignored unless `unit_scale` is True.
        write_bytes  : bool, optional
            If (default: None) and `file` is unspecified,
            bytes will be written in Python 2. If `True` will also write
            bytes. In all other cases will default to unicode.
        lock_args  : tuple, optional
            Passed to `refresh` for intermediate output
            (initialisation, iterating, and updating).
        nrows  : int, optional
            The screen height. If specified, hides nested bars outside this
            bound. If unspecified, attempts to use environment height.
            The fallback is 20.
        colour  : str, optional
            Bar colour (e.g. 'green', '#00ff00').
        delay  : float, optional
            Don't display until [default: 0] seconds have elapsed.
        gui  : bool, optional
            WARNING: internal parameter - do not use.
            Use tqdm.gui.tqdm(...) instead. If set, will attempt to use
            matplotlib animations for a graphical output [default: False].
    
        Returns
        -------
        out  : decorated iterator.
        """
        if write_bytes is None:
            write_bytes = file is None and sys.version_info < (3,)
    
        if file is None:
            file = sys.stderr
    
        if write_bytes:
            # Despite coercing unicode into bytes, py2 sys.std* streams
            # should have bytes written to them.
            file = SimpleTextIOWrapper(
                file, encoding=getattr(file, 'encoding', None) or 'utf-8')
    
        file = DisableOnWriteError(file, tqdm_instance=self)
    
        if disable is None and hasattr(file, "isatty") and not file.isatty():
            disable = True
    
        if total is None and iterable is not None:
            try:
                total = len(iterable)
            except (TypeError, AttributeError):
                total = None
        if total == float("inf"):
            # Infinite iterations, behave same as unknown
            total = None
    
        if disable:
            self.iterable = iterable
            self.disable = disable
            with self._lock:
                self.pos = self._get_free_pos(self)
                self._instances.remove(self)
            self.n = initial
            self.total = total
            self.leave = leave
            return
    
        if kwargs:
            self.disable = True
            with self._lock:
                self.pos = self._get_free_pos(self)
                self._instances.remove(self)
>           raise (
                TqdmDeprecationWarning(
                    "`nested` is deprecated and automated.\n"
                    "Use `position` instead for manual control.\n",
                    fp_write=getattr(file, 'write', sys.stderr.write))
                if "nested" in kwargs else
                TqdmKeyError("Unknown argument(s): " + str(kwargs)))
E           tqdm.std.TqdmKeyError: "Unknown argument(s): {'range': None}"

/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/std.py:1012: TqdmKeyError
______________________ test_invalid_input_error_handling _______________________

    def test_invalid_input_error_handling():
        try:
>           pb = tqdm_notebook(range='invalid', display=True)

/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_notebook_tqdm_notebook_display_1.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/notebook.py:231: in __init__
    super(tqdm_notebook, self).__init__(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <tqdm.notebook.tqdm_notebook object at 0x7f354e7f8520>, iterable = None
desc = None, total = None, leave = True
file = <tqdm.utils.DisableOnWriteError object at 0x7f354e7f87f0>, ncols = None
mininterval = 0.1, maxinterval = 10.0, miniters = None, ascii = None
disable = False, unit = 'it', unit_scale = False, dynamic_ncols = False
smoothing = 0.3, bar_format = None, initial = 0, position = None, postfix = None
unit_divisor = 1000, write_bytes = False, lock_args = None, nrows = None
colour = None, delay = 0, gui = True, kwargs = {'range': 'invalid'}

    def __init__(self, iterable=None, desc=None, total=None, leave=True, file=None,
                 ncols=None, mininterval=0.1, maxinterval=10.0, miniters=None,
                 ascii=None, disable=False, unit='it', unit_scale=False,
                 dynamic_ncols=False, smoothing=0.3, bar_format=None, initial=0,
                 position=None, postfix=None, unit_divisor=1000, write_bytes=None,
                 lock_args=None, nrows=None, colour=None, delay=0, gui=False,
                 **kwargs):
        """
        Parameters
        ----------
        iterable  : iterable, optional
            Iterable to decorate with a progressbar.
            Leave blank to manually manage the updates.
        desc  : str, optional
            Prefix for the progressbar.
        total  : int or float, optional
            The number of expected iterations. If unspecified,
            len(iterable) is used if possible. If float("inf") or as a last
            resort, only basic progress statistics are displayed
            (no ETA, no progressbar).
            If `gui` is True and this parameter needs subsequent updating,
            specify an initial arbitrary large positive number,
            e.g. 9e9.
        leave  : bool, optional
            If [default: True], keeps all traces of the progressbar
            upon termination of iteration.
            If `None`, will leave only if `position` is `0`.
        file  : `io.TextIOWrapper` or `io.StringIO`, optional
            Specifies where to output the progress messages
            (default: sys.stderr). Uses `file.write(str)` and `file.flush()`
            methods.  For encoding, see `write_bytes`.
        ncols  : int, optional
            The width of the entire output message. If specified,
            dynamically resizes the progressbar to stay within this bound.
            If unspecified, attempts to use environment width. The
            fallback is a meter width of 10 and no limit for the counter and
            statistics. If 0, will not print any meter (only stats).
        mininterval  : float, optional
            Minimum progress display update interval [default: 0.1] seconds.
        maxinterval  : float, optional
            Maximum progress display update interval [default: 10] seconds.
            Automatically adjusts `miniters` to correspond to `mininterval`
            after long display update lag. Only works if `dynamic_miniters`
            or monitor thread is enabled.
        miniters  : int or float, optional
            Minimum progress display update interval, in iterations.
            If 0 and `dynamic_miniters`, will automatically adjust to equal
            `mininterval` (more CPU efficient, good for tight loops).
            If > 0, will skip display of specified number of iterations.
            Tweak this and `mininterval` to get very efficient loops.
            If your progress is erratic with both fast and slow iterations
            (network, skipping items, etc) you should set miniters=1.
        ascii  : bool or str, optional
            If unspecified or False, use unicode (smooth blocks) to fill
            the meter. The fallback is to use ASCII characters " 123456789#".
        disable  : bool, optional
            Whether to disable the entire progressbar wrapper
            [default: False]. If set to None, disable on non-TTY.
        unit  : str, optional
            String that will be used to define the unit of each iteration
            [default: it].
        unit_scale  : bool or int or float, optional
            If 1 or True, the number of iterations will be reduced/scaled
            automatically and a metric prefix following the
            International System of Units standard will be added
            (kilo, mega, etc.) [default: False]. If any other non-zero
            number, will scale `total` and `n`.
        dynamic_ncols  : bool, optional
            If set, constantly alters `ncols` and `nrows` to the
            environment (allowing for window resizes) [default: False].
        smoothing  : float, optional
            Exponential moving average smoothing factor for speed estimates
            (ignored in GUI mode). Ranges from 0 (average speed) to 1
            (current/instantaneous speed) [default: 0.3].
        bar_format  : str, optional
            Specify a custom bar string formatting. May impact performance.
            [default: '{l_bar}{bar}{r_bar}'], where
            l_bar='{desc}: {percentage:3.0f}%|' and
            r_bar='| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, '
              '{rate_fmt}{postfix}]'
            Possible vars: l_bar, bar, r_bar, n, n_fmt, total, total_fmt,
              percentage, elapsed, elapsed_s, ncols, nrows, desc, unit,
              rate, rate_fmt, rate_noinv, rate_noinv_fmt,
              rate_inv, rate_inv_fmt, postfix, unit_divisor,
              remaining, remaining_s, eta.
            Note that a trailing ": " is automatically removed after {desc}
            if the latter is empty.
        initial  : int or float, optional
            The initial counter value. Useful when restarting a progress
            bar [default: 0]. If using float, consider specifying `{n:.3f}`
            or similar in `bar_format`, or specifying `unit_scale`.
        position  : int, optional
            Specify the line offset to print this bar (starting from 0)
            Automatic if unspecified.
            Useful to manage multiple bars at once (eg, from threads).
        postfix  : dict or *, optional
            Specify additional stats to display at the end of the bar.
            Calls `set_postfix(**postfix)` if possible (dict).
        unit_divisor  : float, optional
            [default: 1000], ignored unless `unit_scale` is True.
        write_bytes  : bool, optional
            If (default: None) and `file` is unspecified,
            bytes will be written in Python 2. If `True` will also write
            bytes. In all other cases will default to unicode.
        lock_args  : tuple, optional
            Passed to `refresh` for intermediate output
            (initialisation, iterating, and updating).
        nrows  : int, optional
            The screen height. If specified, hides nested bars outside this
            bound. If unspecified, attempts to use environment height.
            The fallback is 20.
        colour  : str, optional
            Bar colour (e.g. 'green', '#00ff00').
        delay  : float, optional
            Don't display until [default: 0] seconds have elapsed.
        gui  : bool, optional
            WARNING: internal parameter - do not use.
            Use tqdm.gui.tqdm(...) instead. If set, will attempt to use
            matplotlib animations for a graphical output [default: False].
    
        Returns
        -------
        out  : decorated iterator.
        """
        if write_bytes is None:
            write_bytes = file is None and sys.version_info < (3,)
    
        if file is None:
            file = sys.stderr
    
        if write_bytes:
            # Despite coercing unicode into bytes, py2 sys.std* streams
            # should have bytes written to them.
            file = SimpleTextIOWrapper(
                file, encoding=getattr(file, 'encoding', None) or 'utf-8')
    
        file = DisableOnWriteError(file, tqdm_instance=self)
    
        if disable is None and hasattr(file, "isatty") and not file.isatty():
            disable = True
    
        if total is None and iterable is not None:
            try:
                total = len(iterable)
            except (TypeError, AttributeError):
                total = None
        if total == float("inf"):
            # Infinite iterations, behave same as unknown
            total = None
    
        if disable:
            self.iterable = iterable
            self.disable = disable
            with self._lock:
                self.pos = self._get_free_pos(self)
                self._instances.remove(self)
            self.n = initial
            self.total = total
            self.leave = leave
            return
    
        if kwargs:
            self.disable = True
            with self._lock:
                self.pos = self._get_free_pos(self)
                self._instances.remove(self)
>           raise (
                TqdmDeprecationWarning(
                    "`nested` is deprecated and automated.\n"
                    "Use `position` instead for manual control.\n",
                    fp_write=getattr(file, 'write', sys.stderr.write))
                if "nested" in kwargs else
                TqdmKeyError("Unknown argument(s): " + str(kwargs)))
E           tqdm.std.TqdmKeyError: "Unknown argument(s): {'range': 'invalid'}"

/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/std.py:1012: TqdmKeyError

During handling of the above exception, another exception occurred:

    def test_invalid_input_error_handling():
        try:
            pb = tqdm_notebook(range='invalid', display=True)
        except Exception as e:
>           assert str(e) == "Invalid range type '<class 'str'>'. Expected a sequence.", f"Expected error message not received. Got {str(e)}"
E           AssertionError: Expected error message not received. Got "Unknown argument(s): {'range': 'invalid'}"
E           assert '"Unknown arg...\'invalid\'}"' == 'Invalid rang...d a sequence.'
E             
E             - Invalid range type '<class 'str'>'. Expected a sequence.
E             + "Unknown argument(s): {'range': 'invalid'}"

/opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_notebook_tqdm_notebook_display_1.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_notebook_tqdm_notebook_display_1.py::test_valid_input_happy_path
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_notebook_tqdm_notebook_display_1.py::test_edge_case_none_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tqdm/Test4DT_tests_deepseek-coder-v2_16b/test_tqdm_notebook_tqdm_notebook_display_1.py::test_invalid_input_error_handling
============================== 3 failed in 0.51s ===============================

Exception ignored in: <function tqdm.__del__ at 0x7f354f989cf0>
Traceback (most recent call last):
  File "/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/std.py", line 1147, in __del__
    self.close()
  File "/opt/marta/baselines/codamosa/replication/test-apps/tqdm/tqdm/notebook.py", line 286, in close
    self.disp(bar_style='danger', check_delay=False)
AttributeError: 'tqdm_notebook' object has no attribute 'disp'
"""