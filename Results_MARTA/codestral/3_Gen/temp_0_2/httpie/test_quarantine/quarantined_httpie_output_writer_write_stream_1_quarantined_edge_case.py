
import pytest
from io import StringIO
from httpie.output.writer import write_stream
from unittest.mock import patch

@pytest.mark.parametrize("flush", [True, False])
def test_write_stream(flush):
    stream = iter(["line1\n", "line2\n"])
    outfile = StringIO()
    
    with patch('httpie.output.writer.sys.stdout', new=outfile):
        write_stream(stream, sys.stdout, flush)
        
    assert outfile.getvalue() == "line1\nline2\n"
    if flush:
        assert not outfile.flush.called

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_writer_write_stream_1_test_edge_case
httpie/Test4DT_tests_codestral/test_httpie_output_writer_write_stream_1_test_edge_case.py:13:29: E0602: Undefined variable 'sys' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_output_writer_write_stream_1_test_edge_case.py:17:19: E1101: Method 'flush' has no 'called' member (no-member)


"""