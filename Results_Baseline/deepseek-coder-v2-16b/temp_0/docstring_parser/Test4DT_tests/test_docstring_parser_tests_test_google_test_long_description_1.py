
def test_long_description():
    source = "This is a summary.\n            \n            Args:\n                param1 (int): Description of parameter 1.\n                param2 (str): Description of parameter 2.\n                \n            Returns:\n                int: The result of the operation, which could be an integer."
    expected_short_desc = "This is a summary."
    expected_long_desc = None
    expected_blank = True
