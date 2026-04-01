
import inspect
import functools
from dataclasses import dataclass
from typing import Callable, Any

class _CatchAllUndefinedParameters:
    """
        This class allows to add a field of type utils.CatchAll which acts as a
        dictionary into which all
        undefined parameters will be written.
        These parameters are not affected by LetterCase.
        If no undefined parameters are given, this dictionary will be empty.
    """
    class _SentinelNoDefault:
        pass

def create_init(obj) -> Callable:
    """
    This function creates an initializer for a class or dataclass that can handle unknown parameters by separating defined and undefined keyword arguments. It binds the partial arguments to the method signature and updates them with any remaining unknown arguments, then processes these combined arguments to call the original constructor. This allows for flexibility in initializing instances even when some parameters are not explicitly defined.
    
    Parameters:
        obj (class or dataclass): The class or dataclass object for which the initializer is being created.
        
    Returns:
        Callable: A function that can be used as a constructor for the given class or dataclass, capable of handling unknown arguments.
    
    Examples:
        To use this function with a custom class `MyClass`, you would do the following:
        
        ```python
        from your_module import create_init
        
        @dataclass
        class MyClass:
            param1: int
            param2: str
        
        modified_init = create_init(MyClass)
        
        # Now you can use the modified init method in a class that inherits from MyClass:
        @dataclass
        class SubClass(MyClass):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
        
        sub_instance = SubClass()
        # The undefined parameters will be stored in the special dictionary accessible through `sub_instance._CatchAllUndefinedParameters__catch_all`.
        ```
    """
    original_init = obj.__init__
    init_signature = inspect.signature(original_init)

    @functools.wraps(obj.__init__)
    def _catch_all_init(self, *args, **kwargs):
        known_kwargs, unknown_kwargs = \
            _CatchAllUndefinedParameters._separate_defined_undefined_kvs(
                obj, kwargs)
        num_params_takeable = len(
            init_signature.parameters) - 1  # don't count self
        if _CatchAllUndefinedParameters._get_catch_all_field(
                obj).name not in known_kwargs:
            num_params_takeable -= 1
        num_args_takeable = num_params_takeable - len(known_kwargs)

        args, unknown_args = args[:num_args_takeable], args[
                                                       num_args_takeable:]
        bound_parameters = init_signature.bind_partial(self, *args,
                                                       **known_kwargs)

        unknown_args = {f"_UNKNOWN{i}": v for i, v in
                        enumerate(unknown_args)}
        arguments = bound_parameters.arguments
        arguments.update(unknown_args)
        arguments.update(unknown_kwargs)
        arguments.pop("self", None)
        final_parameters = _CatchAllUndefinedParameters.handle_from_dict(
            obj, arguments)
        original_init(self, **final_parameters)

    return _catch_all_init

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__CatchAllUndefinedParameters_create_init_0_test_valid_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_create_init_0_test_valid_case.py:57:12: E1101: Class '_CatchAllUndefinedParameters' has no '_separate_defined_undefined_kvs' member (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_create_init_0_test_valid_case.py:61:11: E1101: Class '_CatchAllUndefinedParameters' has no '_get_catch_all_field' member (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__CatchAllUndefinedParameters_create_init_0_test_valid_case.py:77:27: E1101: Class '_CatchAllUndefinedParameters' has no 'handle_from_dict' member (no-member)


"""