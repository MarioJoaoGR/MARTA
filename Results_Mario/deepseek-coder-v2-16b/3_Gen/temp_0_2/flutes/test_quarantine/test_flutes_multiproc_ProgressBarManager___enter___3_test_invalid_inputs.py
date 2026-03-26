
import pytest
from unittest.mock import MagicMock, patch
from flutes.multiproc import ProgressBarManager

@pytest.mark.parametrize("invalid_input", [None, "", [], {}, ()])
def test_invalid_inputs(invalid_input):
    with patch('flutes.multiproc.ProgressBarManager', new=MagicMock()):
        manager = ProgressBarManager(verbose=True)
        if invalid_input is None:
            with pytest.raises(ValueError):
                manager._proxy.new([], update_frequency=invalid_input)
        elif isinstance(invalid_input, list):
            with pytest.raises(KeyError):
                manager._proxy.new(None, update_frequency=invalid_input['update_frequency'])
        else:
            with pytest.raises(ValueError):
                manager._proxy.new([], update_frequency=invalid_input)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___3_test_invalid_inputs.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
__________________________ test_invalid_inputs[None] ___________________________

invalid_input = None

    @pytest.mark.parametrize("invalid_input", [None, "", [], {}, ()])
    def test_invalid_inputs(invalid_input):
        with patch('flutes.multiproc.ProgressBarManager', new=MagicMock()):
            manager = ProgressBarManager(verbose=True)
            if invalid_input is None:
                with pytest.raises(ValueError):
>                   manager._proxy.new([], update_frequency=invalid_input)

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___3_test_invalid_inputs.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.ProgressBarManager.Proxy object at 0x7ff9b8c4ad10>
iterable = [], update_frequency = None, kwargs = {'total': 0}, length = 0
ret_val = <flutes.multiproc.ProgressBarManager.Proxy object at 0x7ff9b8c4ad10>
iter_len = 0

    def new(self, iterable=None, update_frequency=1, **kwargs):
        r"""Construct a new progress bar.
    
        :param iterable: The iterable to decorate with a progress bar. If ``None``, then updates must be manually
            managed with calls to :meth:`update`.
        :param update_frequency: How many iterations per update. This argument only takes effect if :attr:`iterable`
            is not ``None``:
    
            - If :attr:`update_frequency` is a ``float``, then the progress bar is updated whenever the iterable
              progresses over that percentage of elements. For instance, a value of ``0.01`` results in an update
              per 1% of progress. Requires a sized iterable (having a valid ``__len__``).
            - If :attr:`update_frequency` is an ``int``, then the progress bar is updated whenever the iterable
              progresses over that many elements. For instance, a value of ``10`` results in an update per 10
              elements.
        :param kwargs: Additional arguments for the `tqdm <https://tqdm.github.io/>`_ progress bar initializer.
            These can override the default arguments set in the constructor of :class:`ProgressBarManager`.
        :return: The wrapped iterable, or the proxy class itself.
        """
        length = kwargs.get("total", None)
        ret_val = self
        if iterable is not None:
            try:
                iter_len = len(iterable)
                if length is None:
                    length = iter_len
                    kwargs.update(total=iter_len)
                elif length != iter_len:
                    import warnings
                    warnings.warn(f"Iterable has length {iter_len} but total={length} is specified")
            except TypeError:
                pass
            if isinstance(update_frequency, float):
                if length is None:
                    raise ValueError("`iterable` must have valid length, or `total` must be specified "
                                     "if `update_frequency` is float")
                if not (0.0 < update_frequency <= 1.0):
                    raise ValueError("`update_frequency` must be within the range (0, 1]")
                ret_val = self._iter_per_percentage(iterable, length, update_frequency)
            else:
>               if not (0 < update_frequency):
E               TypeError: '<' not supported between instances of 'int' and 'NoneType'

flutes/flutes/multiproc.py:921: TypeError
____________________________ test_invalid_inputs[] _____________________________

invalid_input = ''

    @pytest.mark.parametrize("invalid_input", [None, "", [], {}, ()])
    def test_invalid_inputs(invalid_input):
        with patch('flutes.multiproc.ProgressBarManager', new=MagicMock()):
            manager = ProgressBarManager(verbose=True)
            if invalid_input is None:
                with pytest.raises(ValueError):
                    manager._proxy.new([], update_frequency=invalid_input)
            elif isinstance(invalid_input, list):
                with pytest.raises(KeyError):
                    manager._proxy.new(None, update_frequency=invalid_input['update_frequency'])
            else:
                with pytest.raises(ValueError):
>                   manager._proxy.new([], update_frequency=invalid_input)

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___3_test_invalid_inputs.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.ProgressBarManager.Proxy object at 0x7ff9b7d8e890>
iterable = [], update_frequency = '', kwargs = {'total': 0}, length = 0
ret_val = <flutes.multiproc.ProgressBarManager.Proxy object at 0x7ff9b7d8e890>
iter_len = 0

    def new(self, iterable=None, update_frequency=1, **kwargs):
        r"""Construct a new progress bar.
    
        :param iterable: The iterable to decorate with a progress bar. If ``None``, then updates must be manually
            managed with calls to :meth:`update`.
        :param update_frequency: How many iterations per update. This argument only takes effect if :attr:`iterable`
            is not ``None``:
    
            - If :attr:`update_frequency` is a ``float``, then the progress bar is updated whenever the iterable
              progresses over that percentage of elements. For instance, a value of ``0.01`` results in an update
              per 1% of progress. Requires a sized iterable (having a valid ``__len__``).
            - If :attr:`update_frequency` is an ``int``, then the progress bar is updated whenever the iterable
              progresses over that many elements. For instance, a value of ``10`` results in an update per 10
              elements.
        :param kwargs: Additional arguments for the `tqdm <https://tqdm.github.io/>`_ progress bar initializer.
            These can override the default arguments set in the constructor of :class:`ProgressBarManager`.
        :return: The wrapped iterable, or the proxy class itself.
        """
        length = kwargs.get("total", None)
        ret_val = self
        if iterable is not None:
            try:
                iter_len = len(iterable)
                if length is None:
                    length = iter_len
                    kwargs.update(total=iter_len)
                elif length != iter_len:
                    import warnings
                    warnings.warn(f"Iterable has length {iter_len} but total={length} is specified")
            except TypeError:
                pass
            if isinstance(update_frequency, float):
                if length is None:
                    raise ValueError("`iterable` must have valid length, or `total` must be specified "
                                     "if `update_frequency` is float")
                if not (0.0 < update_frequency <= 1.0):
                    raise ValueError("`update_frequency` must be within the range (0, 1]")
                ret_val = self._iter_per_percentage(iterable, length, update_frequency)
            else:
>               if not (0 < update_frequency):
E               TypeError: '<' not supported between instances of 'int' and 'str'

flutes/flutes/multiproc.py:921: TypeError
_____________________ test_invalid_inputs[invalid_input2] ______________________

invalid_input = []

    @pytest.mark.parametrize("invalid_input", [None, "", [], {}, ()])
    def test_invalid_inputs(invalid_input):
        with patch('flutes.multiproc.ProgressBarManager', new=MagicMock()):
            manager = ProgressBarManager(verbose=True)
            if invalid_input is None:
                with pytest.raises(ValueError):
                    manager._proxy.new([], update_frequency=invalid_input)
            elif isinstance(invalid_input, list):
                with pytest.raises(KeyError):
>                   manager._proxy.new(None, update_frequency=invalid_input['update_frequency'])
E                   TypeError: list indices must be integers or slices, not str

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___3_test_invalid_inputs.py:15: TypeError
_____________________ test_invalid_inputs[invalid_input3] ______________________

invalid_input = {}

    @pytest.mark.parametrize("invalid_input", [None, "", [], {}, ()])
    def test_invalid_inputs(invalid_input):
        with patch('flutes.multiproc.ProgressBarManager', new=MagicMock()):
            manager = ProgressBarManager(verbose=True)
            if invalid_input is None:
                with pytest.raises(ValueError):
                    manager._proxy.new([], update_frequency=invalid_input)
            elif isinstance(invalid_input, list):
                with pytest.raises(KeyError):
                    manager._proxy.new(None, update_frequency=invalid_input['update_frequency'])
            else:
                with pytest.raises(ValueError):
>                   manager._proxy.new([], update_frequency=invalid_input)

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___3_test_invalid_inputs.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.ProgressBarManager.Proxy object at 0x7ff9b7d7e3d0>
iterable = [], update_frequency = {}, kwargs = {'total': 0}, length = 0
ret_val = <flutes.multiproc.ProgressBarManager.Proxy object at 0x7ff9b7d7e3d0>
iter_len = 0

    def new(self, iterable=None, update_frequency=1, **kwargs):
        r"""Construct a new progress bar.
    
        :param iterable: The iterable to decorate with a progress bar. If ``None``, then updates must be manually
            managed with calls to :meth:`update`.
        :param update_frequency: How many iterations per update. This argument only takes effect if :attr:`iterable`
            is not ``None``:
    
            - If :attr:`update_frequency` is a ``float``, then the progress bar is updated whenever the iterable
              progresses over that percentage of elements. For instance, a value of ``0.01`` results in an update
              per 1% of progress. Requires a sized iterable (having a valid ``__len__``).
            - If :attr:`update_frequency` is an ``int``, then the progress bar is updated whenever the iterable
              progresses over that many elements. For instance, a value of ``10`` results in an update per 10
              elements.
        :param kwargs: Additional arguments for the `tqdm <https://tqdm.github.io/>`_ progress bar initializer.
            These can override the default arguments set in the constructor of :class:`ProgressBarManager`.
        :return: The wrapped iterable, or the proxy class itself.
        """
        length = kwargs.get("total", None)
        ret_val = self
        if iterable is not None:
            try:
                iter_len = len(iterable)
                if length is None:
                    length = iter_len
                    kwargs.update(total=iter_len)
                elif length != iter_len:
                    import warnings
                    warnings.warn(f"Iterable has length {iter_len} but total={length} is specified")
            except TypeError:
                pass
            if isinstance(update_frequency, float):
                if length is None:
                    raise ValueError("`iterable` must have valid length, or `total` must be specified "
                                     "if `update_frequency` is float")
                if not (0.0 < update_frequency <= 1.0):
                    raise ValueError("`update_frequency` must be within the range (0, 1]")
                ret_val = self._iter_per_percentage(iterable, length, update_frequency)
            else:
>               if not (0 < update_frequency):
E               TypeError: '<' not supported between instances of 'int' and 'dict'

flutes/flutes/multiproc.py:921: TypeError
_____________________ test_invalid_inputs[invalid_input4] ______________________

invalid_input = ()

    @pytest.mark.parametrize("invalid_input", [None, "", [], {}, ()])
    def test_invalid_inputs(invalid_input):
        with patch('flutes.multiproc.ProgressBarManager', new=MagicMock()):
            manager = ProgressBarManager(verbose=True)
            if invalid_input is None:
                with pytest.raises(ValueError):
                    manager._proxy.new([], update_frequency=invalid_input)
            elif isinstance(invalid_input, list):
                with pytest.raises(KeyError):
                    manager._proxy.new(None, update_frequency=invalid_input['update_frequency'])
            else:
                with pytest.raises(ValueError):
>                   manager._proxy.new([], update_frequency=invalid_input)

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___3_test_invalid_inputs.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.multiproc.ProgressBarManager.Proxy object at 0x7ff9b7be5450>
iterable = [], update_frequency = (), kwargs = {'total': 0}, length = 0
ret_val = <flutes.multiproc.ProgressBarManager.Proxy object at 0x7ff9b7be5450>
iter_len = 0

    def new(self, iterable=None, update_frequency=1, **kwargs):
        r"""Construct a new progress bar.
    
        :param iterable: The iterable to decorate with a progress bar. If ``None``, then updates must be manually
            managed with calls to :meth:`update`.
        :param update_frequency: How many iterations per update. This argument only takes effect if :attr:`iterable`
            is not ``None``:
    
            - If :attr:`update_frequency` is a ``float``, then the progress bar is updated whenever the iterable
              progresses over that percentage of elements. For instance, a value of ``0.01`` results in an update
              per 1% of progress. Requires a sized iterable (having a valid ``__len__``).
            - If :attr:`update_frequency` is an ``int``, then the progress bar is updated whenever the iterable
              progresses over that many elements. For instance, a value of ``10`` results in an update per 10
              elements.
        :param kwargs: Additional arguments for the `tqdm <https://tqdm.github.io/>`_ progress bar initializer.
            These can override the default arguments set in the constructor of :class:`ProgressBarManager`.
        :return: The wrapped iterable, or the proxy class itself.
        """
        length = kwargs.get("total", None)
        ret_val = self
        if iterable is not None:
            try:
                iter_len = len(iterable)
                if length is None:
                    length = iter_len
                    kwargs.update(total=iter_len)
                elif length != iter_len:
                    import warnings
                    warnings.warn(f"Iterable has length {iter_len} but total={length} is specified")
            except TypeError:
                pass
            if isinstance(update_frequency, float):
                if length is None:
                    raise ValueError("`iterable` must have valid length, or `total` must be specified "
                                     "if `update_frequency` is float")
                if not (0.0 < update_frequency <= 1.0):
                    raise ValueError("`update_frequency` must be within the range (0, 1]")
                ret_val = self._iter_per_percentage(iterable, length, update_frequency)
            else:
>               if not (0 < update_frequency):
E               TypeError: '<' not supported between instances of 'int' and 'tuple'

flutes/flutes/multiproc.py:921: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___3_test_invalid_inputs.py::test_invalid_inputs[None]
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___3_test_invalid_inputs.py::test_invalid_inputs[]
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___3_test_invalid_inputs.py::test_invalid_inputs[invalid_input2]
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___3_test_invalid_inputs.py::test_invalid_inputs[invalid_input3]
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___3_test_invalid_inputs.py::test_invalid_inputs[invalid_input4]
============================== 5 failed in 0.25s ===============================
"""