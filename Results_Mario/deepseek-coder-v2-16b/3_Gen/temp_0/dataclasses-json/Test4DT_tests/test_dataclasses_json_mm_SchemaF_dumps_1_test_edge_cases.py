
import pytest
from dataclasses import dataclass
from dataclasses_json import dataclass_json
import typing

@dataclass_json
@dataclass
class A:
    attr1: str
    attr2: str

class SchemaF:
    """Lift Schema into a type constructor"""
    
    def __init__(self, *args, **kwargs):
        """
        Raises exception because this class should not be inherited.
        This class is helper only.
        """
        super().__init__(*args, **kwargs)
        raise NotImplementedError("This class is a helper only and should not be inherited or instantiated.")

    def dumps(self, obj: typing.List[A], many: typing.Optional[bool] = None, *args, **kwargs) -> str:
        """
        Converts a list of objects (of type A) into a JSON string representation.
        
        Parameters:
            obj (typing.List[A]): The list of objects to be converted. Each object in the list must be an instance of class A.
            many (typing.Optional[bool], optional): Indicates whether multiple instances of the schema are being processed. If set to True, it will handle a list of objects; if set to False or None, it will handle a single object. Default is None.
        
        Returns:
            str: A JSON string representation of the provided list of objects.
        
        Example:
            schema = SchemaF()
            obj_list = [A(attr1='value1', attr2='value2'), A(attr1='value3', attr2='value4')]
            json_str = schema.dumps(obj_list, many=True)
            # json_str will contain the JSON representation of the list of objects in obj_list.
        """
        pass

def test_edge_cases():
    with pytest.raises(NotImplementedError):
        SchemaF()
