
import pytest
from pysnooper.tracer import Tracer

# Define a simple generator function to be wrapped
def my_generator():
    value = yield "start"
    while True:
        value = yield f"received: {value}"

# Define the generator wrapper function with proper context management
def generator_wrapper(function, *args, **kwargs):
    gen = function(*args, **kwargs)
    method, incoming = gen.send, None
    tracer = Tracer()
    
    while True:
        with tracer:
            try:
                outgoing = method(incoming)
            except StopIteration:
                return
        try:
            method, incoming = gen.send, (yield outgoing)
        except Exception as e:
            method, incoming = gen.throw, e

# Test function for the valid case
def test_valid_case():
    wrapped_gen = generator_wrapper(my_generator)
    assert next(wrapped_gen) == 'start'
    assert wrapped_gen.send("hello") == 'received: hello'

# Test function for the edge case with None
def test_edge_cases():
    wrapped_gen = generator_wrapper(my_generator)
    assert next(wrapped_gen) == 'start'
    assert wrapped_gen.send(None) == 'received: None'
