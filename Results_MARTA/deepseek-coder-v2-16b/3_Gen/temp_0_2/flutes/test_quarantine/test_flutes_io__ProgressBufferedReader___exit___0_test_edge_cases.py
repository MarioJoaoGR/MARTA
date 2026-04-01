
import io
from flutes.io import BarFn

class _ProgressBufferedReader(io.BufferedReader):
    def __init__(self, raw: io.RawIOBase, buffer_size: int = io.DEFAULT_BUFFER_SIZE, *, bar_fn: BarFn):
        super().__init__(raw, buffer_size)
        file_size = os.fstat(raw.fileno()).st_size
        self._read_bytes = 0
        self.progress_bar = bar_fn(total=file_size)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if super().__exit__(exc_type, exc_val, exc_tb):
            return True
        return self.progress_bar.__exit__(exc_type, exc_val, exc_tb)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_io__ProgressBufferedReader___exit___0_test_edge_cases
flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader___exit___0_test_edge_cases.py:8:20: E0602: Undefined variable 'os' (undefined-variable)


"""