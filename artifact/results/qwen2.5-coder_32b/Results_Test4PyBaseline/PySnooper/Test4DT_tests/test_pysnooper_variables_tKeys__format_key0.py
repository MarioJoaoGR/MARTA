
from pysnooper import Keys  # Assuming Keys is part of the pysnooper module

def test_format_key_custom_object():
    class CustomObject:
        def __init__(self, value):
            self.value = value

    obj = CustomObject(42)
    keys_instance = Keys(source="test_source")
    formatted_key = keys_instance._format_key(obj)
    assert formatted_key.startswith('[<') and formatted_key.endswith('>]')
