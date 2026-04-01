
import io
from unittest import mock
import os

class _ProgressBufferedReader(io.BufferedReader):
    def __init__(self, raw: io.RawIOBase, buffer_size: int = io.DEFAULT_BUFFER_SIZE, *, bar_fn: BarFn):
        super().__init__(raw, buffer_size)
        file_size = os.fstat(raw.fileno()).st_size
        self._read_bytes = 0
        self.progress_bar = bar_fn(total=file_size)

    def read(self, size: Optional[int] = -1) -> bytes:
        ret = super().read(size)
        if ret is not None:
            self._read_bytes += len(ret)
            self.progress_bar.update(len(ret))
        return ret

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_io__ProgressBufferedReader_read_0_test_edge_case_none
flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader_read_0_test_edge_case_none.py:7:96: E0602: Undefined variable 'BarFn' (undefined-variable)
flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader_read_0_test_edge_case_none.py:13:25: E0602: Undefined variable 'Optional' (undefined-variable)


"""