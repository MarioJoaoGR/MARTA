
from flutes import MapList

def test_maplist_with_non_callable():
    # Define a simple transformation function
    def square(x):
        return x * x

    # Create an instance of MapList with the square function and a list of integers
    map_list_instance = MapList(square, [1, 2, 3])

    # Test initializing with a non-callable should not raise TypeError based on current behavior
    try:
        _ = MapList("not a function", [1, 2, 3])
        assert True  # No exception raised, test passes
    except TypeError:
        assert False  # Exception raised, test fails

def test_maplist_with_non_sequence():
    # Define a simple transformation function
    def square(x):
        return x * x

    # Create an instance of MapList with the square function and a list of integers
    map_list_instance = MapList(square, [1, 2, 3])

    # Test initializing with a non-sequence should not raise TypeError based on current behavior
    try:
        _ = MapList(lambda x: x * x, "not a sequence")
        assert True  # No exception raised, test passes
    except TypeError:
        assert False  # Exception raised, test fails
