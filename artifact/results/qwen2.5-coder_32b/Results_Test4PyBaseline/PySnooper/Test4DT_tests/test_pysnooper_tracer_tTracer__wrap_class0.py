
# Assuming Tracer is defined in a module named pysnooper, adjust the import path as necessary.
from pysnooper.tracer import Tracer

def test_tracer_initialization_with_output_file():
    tracer = Tracer(output='trace.log')
    assert tracer._write.__name__ == 'write'
