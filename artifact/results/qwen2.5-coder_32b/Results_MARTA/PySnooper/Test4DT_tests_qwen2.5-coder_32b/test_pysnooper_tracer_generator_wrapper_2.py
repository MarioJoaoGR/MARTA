
import pytest
from pysnooper.tracer import Tracer

# Define the generator functions as specified in the scenarios
def my_generator_happy_path():
    value = yield 'start'
    while True:
        value = yield f'received: {value}'

def my_generator_edge_cases():
    value = yield ''
    while True:
        value = yield f'{value}'

def my_generator_error_handling():
    value = yield 'start'
    while True:
        if not isinstance(value, str):
            raise ValueError('Invalid input')
        value = yield f'received: {value}'

# Define the generator wrapper function
def generator_wrapper(function, *args, **kwargs):
    gen = function(*args, **kwargs)
    method, incoming = gen.send, None
    while True:
        with Tracer():
            try:
                outgoing = method(incoming)
            except StopIteration:
                return
        try:
            method, incoming = gen.send, (yield outgoing)
        except Exception as e:
            method, incoming = gen.throw, e

# Test function for happy path scenario
def test_happy_path():
    wrapped_gen = generator_wrapper(my_generator_happy_path)
    assert next(wrapped_gen) == 'start'
    assert wrapped_gen.send("hello") == 'received: hello'

# Test function for edge cases scenario
def test_edge_cases():
    wrapped_gen = generator_wrapper(my_generator_edge_cases)
    assert next(wrapped_gen) == ''
    assert wrapped_gen.send(None) == 'None'
    assert wrapped_gen.send('') == ''

# Test function for error handling scenario
def test_error_handling():
    wrapped_gen = generator_wrapper(my_generator_error_handling)
    assert next(wrapped_gen) == 'start'
    with pytest.raises(ValueError, match='Invalid input'):
        wrapped_gen.send(123)
