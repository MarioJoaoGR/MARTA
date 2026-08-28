
import pytest
from pysnooper.tracer import Tracer
import pysnooper  # Importing here to resolve the undefined variable error

# Test basic usage of the Tracer class with default parameters
def test_basic_usage():
    @pysnooper.snoop()
    def my_function():
        x = 10
        y = x + 5
        print(y)
    
    # Call the function to see its execution logged
    my_function()

# Test redirecting logs to a file
def test_redirect_to_file():
    tracer = Tracer(output='debug.log', overwrite=True)
    
    @pysnooper.snoop(output='debug.log')
    def my_function():
        x = 10
        y = x + 5
        print(y)
    
    # Call the function to see its execution logged in 'debug.log'
    my_function()

# Test watching specific variables or expressions
def test_watch_expressions():
    @pysnooper.snoop(watch=('self.value', 'foo.bar'))
    def my_function():
        pass
    
    # Call the function to see its execution logged with specific watches
    my_function()

# Test expanding watched expressions
def test_expand_watches():
    @pysnooper.snoop(watch_explode=('foo', 'self'))
    def my_function():
        pass
    
    # Call the function to see its execution logged with expanded watches
    my_function()

# Test including thread information in logs
def test_thread_info():
    tracer = Tracer(thread_info=True)
    
    @pysnooper.snoop(thread_info=True)
    def my_function():
        pass
    
    # Call the function to see its execution logged with thread information
    my_function()

# Test customizing representation of values
def test_custom_repr():
    @pysnooper.snoop(custom_repr=((int, lambda x: f"Int({x})"), (list, lambda x: f"List({', '.join(map(str, x))}")))
    def my_function():
        x = 10
        y = [x, x + 5]
        print(y)
    
    # Call the function to see its execution logged with customized repr
    my_function()

# Test tracing function calls at a specific depth
def test_trace_depth():
    @pysnooper.snoop(depth=2)
    def my_function():
        x = 10
        y = x + 5
        print(y)
    
    # Call the function to see its execution logged with a depth of 2
    my_function()

# Test using relative time stamps in logs
def test_relative_time():
    @pysnooper.snoop(relative_time=True)
    def my_function():
        x = 10
        y = x + 5
        print(y)
    
    # Call the function to see its execution logged with relative timestamps
    my_function()
