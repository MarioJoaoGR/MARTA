
import pytest
from pysnooper.tracer import Tracer

def test_valid_case():
    tracer = Tracer(thread_info=True)
    padded_thread_info = tracer.set_thread_info_padding('Thread-1')
    assert padded_thread_info == 'Thread-1'

def test_edge_case_empty_string():
    tracer = Tracer(thread_info=True)
    padded_thread_info = tracer.set_thread_info_padding('')
    assert padded_thread_info == ''

def test_invalid_case_non_string_input():
    tracer = Tracer(thread_info=True)
    with pytest.raises(TypeError):
        tracer.set_thread_info_padding(123)
