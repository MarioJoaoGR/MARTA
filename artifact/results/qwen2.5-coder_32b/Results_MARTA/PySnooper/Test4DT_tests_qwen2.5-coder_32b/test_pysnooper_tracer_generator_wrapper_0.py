
import pytest
from pysnooper.tracer import Tracer

# Define a simple generator function to be wrapped
def my_generator():
    value = yield "start"
    while True:
        value = yield f"received: {value}"

# Define the generator wrapper function
def generator_wrapper(function, *args, **kwargs):
    gen = function(*args, **kwargs)
    method, incoming = gen.send, None
    with Tracer():
        try:
            outgoing = method(incoming)
        except StopIteration:
            return
    while True:
        yield outgoing
        try:
            method, incoming = gen.send, (yield outgoing)
        except Exception as e:
            method, incoming = gen.throw, e

# Test function to check the initial output of the generator
def test_initial_output():
    wrapped_gen = generator_wrapper(my_generator)
    assert next(wrapped_gen) == "start"

# Test function to check sending a value to the generator

# Test function to check invalid input handling

# Test function to check StopIteration when generator is exhausted