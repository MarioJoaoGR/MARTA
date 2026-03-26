
import pytest
from flutes.io import progress_open
from pathlib import Path

@pytest.mark.parametrize("path, mode", [
    (12345, "r"),  # Invalid path type (int)
    ("invalid/path", "r"),  # Invalid path string
    (Path(), "invalid_mode")  # Invalid mode string
])
def test_invalid_inputs(path, mode):
    with pytest.raises(TypeError):
        progress_open(path, mode)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

flutes/Test4DT_tests/test_flutes_io_progress_open_2_test_invalid_inputs.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_________________________ test_invalid_inputs[12345-r] _________________________

path = 12345, mode = 'r'

    @pytest.mark.parametrize("path, mode", [
        (12345, "r"),  # Invalid path type (int)
        ("invalid/path", "r"),  # Invalid path string
        (Path(), "invalid_mode")  # Invalid mode string
    ])
    def test_invalid_inputs(path, mode):
        with pytest.raises(TypeError):
>           progress_open(path, mode)

flutes/Test4DT_tests/test_flutes_io_progress_open_2_test_invalid_inputs.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = 12345, mode = 'r', encoding = 'utf-8', verbose = True, buffer_size = 8192
bar_fn = functools.partial(<class 'tqdm.std.tqdm'>, bar_format='{l_bar}{bar}| [{elapsed}<{remaining}{postfix}]')
kwargs = {'bar_format': '{l_bar}{bar}| [{elapsed}<{remaining}{postfix}]'}
tqdm = <class 'tqdm.std.tqdm'>

    def progress_open(path, mode="r", *, encoding='utf-8', verbose=True, buffer_size=io.DEFAULT_BUFFER_SIZE,
                      bar_fn: Optional[BarFn] = None, **kwargs):
        r"""A replacement for :py:func:`open` that shows the progress of reading the file:
    
        .. code:: python
    
            with progress_open(path, mode="r") as f:
                # `f` is just what you'd get with `open(path)`, now with a progress bar
                bar = f.progress_bar  # type: tqdm.tqdm
    
        :param path: Path to the file.
        :param mode: The file open mode. When progress bar is enabled, only read modes ``"r"`` and ``"rb"`` are supported
            (write progress doesn't make a lot of sense). Defaults to ``"r"``.
        :param encoding: Encoding for the file. Only required for ``"r"`` mode. Defaults to ``"utf-8"``.
        :param verbose: If ``False``, the progress bar is not displayed and a normal file object is returned. Defaults to
            ``True``.
        :param buffer_size: The size of the file buffer. Defaults to :py:data:`io.DEFAULT_BUFFER_SIZE`.
        :param bar_fn: An optional callable that constructs a progress bar when called. This is useful when you want to
            override the default progress bar, for instance, to use with :class:`~flutes.ProgressBarManager`:
    
            .. code:: python
    
                def process(path: str, bar: flutes.ProgressBarManager.Proxy):
                    with flutes.progress_open(path, bar_fn=bar.new) as f:
                        ...
    
        :param kwargs: Additional arguments to pass to `tqdm <https://tqdm.github.io/>`_ initializer.
        :return: A file object.
        """
        if not verbose:
            return open(path, mode)
    
        if mode not in ["r", "rb"]:
            raise ValueError(f"Unsupported mode '{mode}'. Only read modes ('r', 'rb') are supported")
    
        kwargs.setdefault("bar_format", "{l_bar}{bar}| [{elapsed}<{remaining}{postfix}]")
        if bar_fn is None:
            from tqdm import tqdm
            bar_fn = tqdm
        if len(kwargs) > 0:
            bar_fn = functools.partial(bar_fn, **kwargs)
>       buffer = f = _ProgressBufferedReader(io.FileIO(str(path), mode="r"), buffer_size, bar_fn=bar_fn)
E       FileNotFoundError: [Errno 2] No such file or directory: '12345'

flutes/flutes/io.py:157: FileNotFoundError
_____________________ test_invalid_inputs[invalid/path-r] ______________________

path = 'invalid/path', mode = 'r'

    @pytest.mark.parametrize("path, mode", [
        (12345, "r"),  # Invalid path type (int)
        ("invalid/path", "r"),  # Invalid path string
        (Path(), "invalid_mode")  # Invalid mode string
    ])
    def test_invalid_inputs(path, mode):
        with pytest.raises(TypeError):
>           progress_open(path, mode)

flutes/Test4DT_tests/test_flutes_io_progress_open_2_test_invalid_inputs.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = 'invalid/path', mode = 'r', encoding = 'utf-8', verbose = True
buffer_size = 8192
bar_fn = functools.partial(<class 'tqdm.std.tqdm'>, bar_format='{l_bar}{bar}| [{elapsed}<{remaining}{postfix}]')
kwargs = {'bar_format': '{l_bar}{bar}| [{elapsed}<{remaining}{postfix}]'}
tqdm = <class 'tqdm.std.tqdm'>

    def progress_open(path, mode="r", *, encoding='utf-8', verbose=True, buffer_size=io.DEFAULT_BUFFER_SIZE,
                      bar_fn: Optional[BarFn] = None, **kwargs):
        r"""A replacement for :py:func:`open` that shows the progress of reading the file:
    
        .. code:: python
    
            with progress_open(path, mode="r") as f:
                # `f` is just what you'd get with `open(path)`, now with a progress bar
                bar = f.progress_bar  # type: tqdm.tqdm
    
        :param path: Path to the file.
        :param mode: The file open mode. When progress bar is enabled, only read modes ``"r"`` and ``"rb"`` are supported
            (write progress doesn't make a lot of sense). Defaults to ``"r"``.
        :param encoding: Encoding for the file. Only required for ``"r"`` mode. Defaults to ``"utf-8"``.
        :param verbose: If ``False``, the progress bar is not displayed and a normal file object is returned. Defaults to
            ``True``.
        :param buffer_size: The size of the file buffer. Defaults to :py:data:`io.DEFAULT_BUFFER_SIZE`.
        :param bar_fn: An optional callable that constructs a progress bar when called. This is useful when you want to
            override the default progress bar, for instance, to use with :class:`~flutes.ProgressBarManager`:
    
            .. code:: python
    
                def process(path: str, bar: flutes.ProgressBarManager.Proxy):
                    with flutes.progress_open(path, bar_fn=bar.new) as f:
                        ...
    
        :param kwargs: Additional arguments to pass to `tqdm <https://tqdm.github.io/>`_ initializer.
        :return: A file object.
        """
        if not verbose:
            return open(path, mode)
    
        if mode not in ["r", "rb"]:
            raise ValueError(f"Unsupported mode '{mode}'. Only read modes ('r', 'rb') are supported")
    
        kwargs.setdefault("bar_format", "{l_bar}{bar}| [{elapsed}<{remaining}{postfix}]")
        if bar_fn is None:
            from tqdm import tqdm
            bar_fn = tqdm
        if len(kwargs) > 0:
            bar_fn = functools.partial(bar_fn, **kwargs)
>       buffer = f = _ProgressBufferedReader(io.FileIO(str(path), mode="r"), buffer_size, bar_fn=bar_fn)
E       FileNotFoundError: [Errno 2] No such file or directory: 'invalid/path'

flutes/flutes/io.py:157: FileNotFoundError
___________________ test_invalid_inputs[path2-invalid_mode] ____________________

path = PosixPath('.'), mode = 'invalid_mode'

    @pytest.mark.parametrize("path, mode", [
        (12345, "r"),  # Invalid path type (int)
        ("invalid/path", "r"),  # Invalid path string
        (Path(), "invalid_mode")  # Invalid mode string
    ])
    def test_invalid_inputs(path, mode):
        with pytest.raises(TypeError):
>           progress_open(path, mode)

flutes/Test4DT_tests/test_flutes_io_progress_open_2_test_invalid_inputs.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = PosixPath('.'), mode = 'invalid_mode', encoding = 'utf-8', verbose = True
buffer_size = 8192, bar_fn = None, kwargs = {}

    def progress_open(path, mode="r", *, encoding='utf-8', verbose=True, buffer_size=io.DEFAULT_BUFFER_SIZE,
                      bar_fn: Optional[BarFn] = None, **kwargs):
        r"""A replacement for :py:func:`open` that shows the progress of reading the file:
    
        .. code:: python
    
            with progress_open(path, mode="r") as f:
                # `f` is just what you'd get with `open(path)`, now with a progress bar
                bar = f.progress_bar  # type: tqdm.tqdm
    
        :param path: Path to the file.
        :param mode: The file open mode. When progress bar is enabled, only read modes ``"r"`` and ``"rb"`` are supported
            (write progress doesn't make a lot of sense). Defaults to ``"r"``.
        :param encoding: Encoding for the file. Only required for ``"r"`` mode. Defaults to ``"utf-8"``.
        :param verbose: If ``False``, the progress bar is not displayed and a normal file object is returned. Defaults to
            ``True``.
        :param buffer_size: The size of the file buffer. Defaults to :py:data:`io.DEFAULT_BUFFER_SIZE`.
        :param bar_fn: An optional callable that constructs a progress bar when called. This is useful when you want to
            override the default progress bar, for instance, to use with :class:`~flutes.ProgressBarManager`:
    
            .. code:: python
    
                def process(path: str, bar: flutes.ProgressBarManager.Proxy):
                    with flutes.progress_open(path, bar_fn=bar.new) as f:
                        ...
    
        :param kwargs: Additional arguments to pass to `tqdm <https://tqdm.github.io/>`_ initializer.
        :return: A file object.
        """
        if not verbose:
            return open(path, mode)
    
        if mode not in ["r", "rb"]:
>           raise ValueError(f"Unsupported mode '{mode}'. Only read modes ('r', 'rb') are supported")
E           ValueError: Unsupported mode 'invalid_mode'. Only read modes ('r', 'rb') are supported

flutes/flutes/io.py:149: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io_progress_open_2_test_invalid_inputs.py::test_invalid_inputs[12345-r]
FAILED flutes/Test4DT_tests/test_flutes_io_progress_open_2_test_invalid_inputs.py::test_invalid_inputs[invalid/path-r]
FAILED flutes/Test4DT_tests/test_flutes_io_progress_open_2_test_invalid_inputs.py::test_invalid_inputs[path2-invalid_mode]
============================== 3 failed in 0.11s ===============================

"""