
import ast
import inspect
import textwrap
from typing import Any, Dict, Optional, Tuple

class AttributeDocstrings:
    """An ast.NodeVisitor that collects attribute docstrings."""
    attr_docs = None
    prev_attr = None
    
    def get_attr_docs(self, component: Any) -> Dict[str, Tuple[str, Optional[str], Optional[str]]]:
        """Get attribute docstrings from the given component.

        This function processes an abstract syntax tree (AST) to extract information about the attributes of the provided component, including their names, types, and default values if available via annotations or assignments. It uses `ast.NodeVisitor` to traverse the AST nodes representing attribute definitions.

        Parameters:
            self (AttributeDocstrings): An instance of the AttributeDocstrings class that will collect attribute docstrings.
            component (Any): The component to process, which can be either a class or module containing attributes.

        Returns:
            Dict[str, Tuple[str, Optional[str], Optional[str]]]: A dictionary where each key is an attribute name and the value is a tuple containing (description, type, default). If no description is available, it will be `None`.

        Examples:
            To use this function, you would typically create an instance of `AttributeDocstrings`, call the `get_attr_docs` method with a class or module component, and then access the collected attribute information via the `attr_docs` property of the instance. For example:
            
            ```python
            visitor = AttributeDocstrings()
            # Assuming `my_class` is an instance of a class or `my_module` is an AST node representing a Python module containing attribute definitions
            attr_docs = visitor.get_attr_docs(my_class)  # or my_module
            
            print(attr_docs)  # This will print the collected attributes with their types and default values if available
            ```
        """
        self.attr_docs = {}
        self.prev_attr = None
        try:
            source = textwrap.dedent(inspect.getsource(component))
        except OSError:
            pass
        else:
            tree = ast.parse(source)
            if inspect.ismodule(component):
                self.visit(tree)
            elif isinstance(tree, ast.Module) and isinstance(tree.body[0], ast.ClassDef):
                self.visit(tree.body[0])
        return self.attr_docs

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_attrdoc_AttributeDocstrings_get_attr_docs_0_test_none_input
docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_get_attr_docs_0_test_none_input.py:44:16: E1101: Instance of 'AttributeDocstrings' has no 'visit' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_attrdoc_AttributeDocstrings_get_attr_docs_0_test_none_input.py:46:16: E1101: Instance of 'AttributeDocstrings' has no 'visit' member (no-member)


"""