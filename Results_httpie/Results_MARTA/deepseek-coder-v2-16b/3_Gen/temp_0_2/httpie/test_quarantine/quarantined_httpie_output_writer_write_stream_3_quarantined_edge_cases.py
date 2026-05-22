
import pytest
from io import StringIO
from unittest.mock import patch
from httpie.output.writer import write_stream

def test_write_stream():
    with patch('httpie.output.writer.sys.stdout', new=StringIO()):
        stream = ["line1\n", "line2\n"]
        outfile = sys.stdout
        flush = True
        
        write_stream(stream, outfile, flush)
        
        assert sys.stdout.getvalue() == "line1\nline2\n"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_writer_write_stream_3_test_edge_cases
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_writer_write_stream_3_test_edge_cases.py:10:18: E0602: Undefined variable 'sys' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_writer_write_stream_3_test_edge_cases.py:15:15: E0602: Undefined variable 'sys' (undefined-variable)


"""