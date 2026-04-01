
import pytest
from flutes.io import progress_open
from pathlib import Path
import os

@pytest.mark.parametrize("path, mode, encoding, verbose, buffer_size", [
    (None, 'r', None, False, 1024 * 1024),
    (Path('test.txt'), None, None, False, 1024 * 1024),
    (Path('test.txt'), 'r', None, False, 1024 * 1024),
    (Path('test.txt'), 'r', 'utf-8', None, 1024 * 1024),
    (Path('test.txt'), 'r', 'utf-8', True, None)
])
def test_edge_case(path, mode, encoding, verbose, buffer_size):
    with pytest.raises(FileNotFoundError):
        progress_open(path, mode, encoding=encoding, verbose=verbose, buffer_size=buffer_size)

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

flutes/Test4DT_tests/test_flutes_io_progress_open_0_test_edge_case.py FF [ 40%]
...                                                                      [100%]

=================================== FAILURES ===================================
__________________ test_edge_case[None-r-None-False-1048576] ___________________

path = None, mode = 'r', encoding = None, verbose = False, buffer_size = 1048576

    @pytest.mark.parametrize("path, mode, encoding, verbose, buffer_size", [
        (None, 'r', None, False, 1024 * 1024),
        (Path('test.txt'), None, None, False, 1024 * 1024),
        (Path('test.txt'), 'r', None, False, 1024 * 1024),
        (Path('test.txt'), 'r', 'utf-8', None, 1024 * 1024),
        (Path('test.txt'), 'r', 'utf-8', True, None)
    ])
    def test_edge_case(path, mode, encoding, verbose, buffer_size):
        with pytest.raises(FileNotFoundError):
>           progress_open(path, mode, encoding=encoding, verbose=verbose, buffer_size=buffer_size)

flutes/Test4DT_tests/test_flutes_io_progress_open_0_test_edge_case.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = None, mode = 'r', encoding = None, verbose = False, buffer_size = 1048576
bar_fn = None, kwargs = {}

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
>           return open(path, mode)
E           TypeError: expected str, bytes or os.PathLike object, not NoneType

flutes/flutes/io.py:146: TypeError
________________ test_edge_case[path1-None-None-False-1048576] _________________

path = PosixPath('test.txt'), mode = None, encoding = None, verbose = False
buffer_size = 1048576

    @pytest.mark.parametrize("path, mode, encoding, verbose, buffer_size", [
        (None, 'r', None, False, 1024 * 1024),
        (Path('test.txt'), None, None, False, 1024 * 1024),
        (Path('test.txt'), 'r', None, False, 1024 * 1024),
        (Path('test.txt'), 'r', 'utf-8', None, 1024 * 1024),
        (Path('test.txt'), 'r', 'utf-8', True, None)
    ])
    def test_edge_case(path, mode, encoding, verbose, buffer_size):
        with pytest.raises(FileNotFoundError):
>           progress_open(path, mode, encoding=encoding, verbose=verbose, buffer_size=buffer_size)

flutes/Test4DT_tests/test_flutes_io_progress_open_0_test_edge_case.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = PosixPath('test.txt'), mode = None, encoding = None, verbose = False
buffer_size = 1048576, bar_fn = None, kwargs = {}

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
>           return open(path, mode)
E           TypeError: open() argument 'mode' must be str, not None

flutes/flutes/io.py:146: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io_progress_open_0_test_edge_case.py::test_edge_case[None-r-None-False-1048576]
FAILED flutes/Test4DT_tests/test_flutes_io_progress_open_0_test_edge_case.py::test_edge_case[path1-None-None-False-1048576]
========================= 2 failed, 3 passed in 0.11s ==========================
"""