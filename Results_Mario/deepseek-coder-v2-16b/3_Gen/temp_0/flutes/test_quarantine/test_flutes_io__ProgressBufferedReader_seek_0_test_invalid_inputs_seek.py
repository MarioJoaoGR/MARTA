
import io
import os
from flutes.io import _ProgressBufferedReader, BarFn

def test_seek_invalid_inputs():
    # Create a mock raw IO base with a fixed size for testing
    class MockRawIOBase(io.RawIOBase):
        def __init__(self):
            super().__init__()
            self.file_size = 1024 * 10  # 10 KB file size
        
        def seekable(self):
            return True
        
        def seek(self, offset: int, whence: int):
            if whence == io.SEEK_SET:
                self._pos = offset
            elif whence == io.SEEK_CUR:
                self._pos += offset
            elif whence == io.SEEK_END:
                self._pos = self.file_size + offset
            return self._pos
        
        def tell(self):
            return self._pos
    
    # Create a mock progress bar function
    class MockProgressBar:
        def __init__(self, total):
            self.total = total
            self.current = 0
        
        def update(self, bytes_read):
            self.current += bytes_read
    
    # Initialize the reader with a mock raw IO base and progress bar function
    raw = MockRawIOBase()
    bar_fn = lambda total: MockProgressBar(total)
    buffered_reader = _ProgressBufferedReader(raw, buffer_size=4096, bar_fn=bar_fn)
    
    # Test seeking with invalid inputs
    assert buffered_reader.seek(-100, io.SEEK_CUR) == -100  # Negative offset not allowed
    assert buffered_reader.seek(2048, io.SEEK_SET) == 2048  # Valid seek within file size
    assert buffered_reader.seek(512, io.SEEK_END) == raw.file_size + 512  # Seek from end of file
    
    # Test seeking beyond the file size (should not move the pointer and should return the original position)
    initial_position = buffered_reader.tell()
    assert buffered_reader.seek(raw.file_size * 2, io.SEEK_SET) == raw.file_size  # Seek beyond file size
    assert buffered_reader.tell() == initial_position  # Position should not change

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader_seek_0_test_invalid_inputs_seek.py F [100%]

=================================== FAILURES ===================================
___________________________ test_seek_invalid_inputs ___________________________

    def test_seek_invalid_inputs():
        # Create a mock raw IO base with a fixed size for testing
        class MockRawIOBase(io.RawIOBase):
            def __init__(self):
                super().__init__()
                self.file_size = 1024 * 10  # 10 KB file size
    
            def seekable(self):
                return True
    
            def seek(self, offset: int, whence: int):
                if whence == io.SEEK_SET:
                    self._pos = offset
                elif whence == io.SEEK_CUR:
                    self._pos += offset
                elif whence == io.SEEK_END:
                    self._pos = self.file_size + offset
                return self._pos
    
            def tell(self):
                return self._pos
    
        # Create a mock progress bar function
        class MockProgressBar:
            def __init__(self, total):
                self.total = total
                self.current = 0
    
            def update(self, bytes_read):
                self.current += bytes_read
    
        # Initialize the reader with a mock raw IO base and progress bar function
        raw = MockRawIOBase()
        bar_fn = lambda total: MockProgressBar(total)
>       buffered_reader = _ProgressBufferedReader(raw, buffer_size=4096, bar_fn=bar_fn)

flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader_seek_0_test_invalid_inputs_seek.py:40: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_ProgressBufferedReader>
raw = <Test4DT_tests.test_flutes_io__ProgressBufferedReader_seek_0_test_invalid_inputs_seek.test_seek_invalid_inputs.<locals>.MockRawIOBase object at 0x7fea67560820>
buffer_size = 4096

    def __init__(self, raw: io.RawIOBase, buffer_size: int = io.DEFAULT_BUFFER_SIZE, *, bar_fn: BarFn):
>       super().__init__(raw, buffer_size)
E       io.UnsupportedOperation: File or stream is not readable.

flutes/flutes/io.py:54: UnsupportedOperation
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader_seek_0_test_invalid_inputs_seek.py::test_seek_invalid_inputs
============================== 1 failed in 0.09s ===============================

"""