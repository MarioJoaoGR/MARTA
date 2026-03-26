
import io
from typing import Optional, Callable
from flutes.io import _ProgressBufferedReader

def progress_open(path: str, mode: str = "r", *, encoding: str = 'utf-8', verbose: bool = True, buffer_size: int = io.DEFAULT_BUFFER_SIZE, bar_fn: Optional[Callable] = None, **kwargs):
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

    buffer = f = _ProgressBufferedReader(io.FileIO(path, mode="r"), buffer_size, bar_fn=bar_fn)
    if mode == "r":
        f = io.TextIOWrapper(f, encoding=encoding)  # type: ignore[assignment]
        f.progress_bar = buffer.progress_bar
    return f

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_io_progress_open_0_test_valid_input
flutes/Test4DT_tests/test_flutes_io_progress_open_0_test_valid_input.py:18:17: E0602: Undefined variable 'functools' (undefined-variable)


"""