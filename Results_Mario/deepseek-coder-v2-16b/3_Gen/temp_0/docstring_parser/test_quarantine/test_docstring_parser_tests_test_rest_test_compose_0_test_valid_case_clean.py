
import pytest
from docstring_parser.tests.test_rest import parse, compose, RenderingStyle

@pytest.mark.parametrize("rendering_style, expected", [
    (RenderingStyle.COMPACT, "Short description\n\nLong description"),
    (RenderingStyle.CLEAN, "Short description\n\nLong description"),
    (RenderingStyle.EXPANDED, "Short description\n\nLong description")
])
def test_compose(rendering_style: RenderingStyle, expected: str) -> None:
    """Test compose function to ensure it correctly renders a parsed docstring into the specified format.

    This function takes a `rendering_style` and an `expected` string as inputs. It parses a sample ReST-style docstring using the `parse` function, then uses the `compose` function with the provided rendering style to generate a formatted string representation of the parsed docstring. The generated string is compared against the expected string to verify correctness.

    Parameters:
        rendering_style (RenderingStyle): Specifies the desired formatting style for the rendered docstring. Must be one of 'compact', 'clean', or 'expanded'.
        expected (str): The expected output string format after applying the `compose` function with the specified `rendering_style`.

    Returns:
        None: This function does not return any value but raises an assertion error if the generated docstring does not match the expected output.

    Examples:
        >>> test_compose(RenderingStyle.COMPACT, "Short description\n\nLong description")
        # This example tests the `test_compose` function with a compact rendering style and expects a specific short and long description format.
        
        >>> test_compose(RenderingStyle.CLEAN, "Short description\n\nLong description")
        # This example tests the same but with a clean rendering style to ensure it handles different styles correctly.
    """
    docstring = parse(
        """
        Short description.

        Long description.

        :param int foo: a description
        :param int bar: another description
        :return float: a return
        """
    )
    assert compose(docstring, rendering_style=rendering_style) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_compose_0_test_valid_case_clean.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__ test_compose[RenderingStyle.COMPACT-Short description\n\nLong description] __

rendering_style = <RenderingStyle.COMPACT: 1>
expected = 'Short description\n\nLong description'

    @pytest.mark.parametrize("rendering_style, expected", [
        (RenderingStyle.COMPACT, "Short description\n\nLong description"),
        (RenderingStyle.CLEAN, "Short description\n\nLong description"),
        (RenderingStyle.EXPANDED, "Short description\n\nLong description")
    ])
    def test_compose(rendering_style: RenderingStyle, expected: str) -> None:
        """Test compose function to ensure it correctly renders a parsed docstring into the specified format.
    
        This function takes a `rendering_style` and an `expected` string as inputs. It parses a sample ReST-style docstring using the `parse` function, then uses the `compose` function with the provided rendering style to generate a formatted string representation of the parsed docstring. The generated string is compared against the expected string to verify correctness.
    
        Parameters:
            rendering_style (RenderingStyle): Specifies the desired formatting style for the rendered docstring. Must be one of 'compact', 'clean', or 'expanded'.
            expected (str): The expected output string format after applying the `compose` function with the specified `rendering_style`.
    
        Returns:
            None: This function does not return any value but raises an assertion error if the generated docstring does not match the expected output.
    
        Examples:
            >>> test_compose(RenderingStyle.COMPACT, "Short description\n\nLong description")
            # This example tests the `test_compose` function with a compact rendering style and expects a specific short and long description format.
    
            >>> test_compose(RenderingStyle.CLEAN, "Short description\n\nLong description")
            # This example tests the same but with a clean rendering style to ensure it handles different styles correctly.
        """
        docstring = parse(
            """
            Short description.
    
            Long description.
    
            :param int foo: a description
            :param int bar: another description
            :return float: a return
            """
        )
>       assert compose(docstring, rendering_style=rendering_style) == expected
E       AssertionError: assert 'Short descri...oat: a return' == 'Short descri...g description'
E         
E         - Short description
E         + Short description.
E         ?                  +
E           
E         - Long description
E         + Long description....
E         
E         ...Full output truncated (5 lines hidden), use '-vv' to show

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_compose_0_test_valid_case_clean.py:40: AssertionError
___ test_compose[RenderingStyle.CLEAN-Short description\n\nLong description] ___

rendering_style = <RenderingStyle.CLEAN: 2>
expected = 'Short description\n\nLong description'

    @pytest.mark.parametrize("rendering_style, expected", [
        (RenderingStyle.COMPACT, "Short description\n\nLong description"),
        (RenderingStyle.CLEAN, "Short description\n\nLong description"),
        (RenderingStyle.EXPANDED, "Short description\n\nLong description")
    ])
    def test_compose(rendering_style: RenderingStyle, expected: str) -> None:
        """Test compose function to ensure it correctly renders a parsed docstring into the specified format.
    
        This function takes a `rendering_style` and an `expected` string as inputs. It parses a sample ReST-style docstring using the `parse` function, then uses the `compose` function with the provided rendering style to generate a formatted string representation of the parsed docstring. The generated string is compared against the expected string to verify correctness.
    
        Parameters:
            rendering_style (RenderingStyle): Specifies the desired formatting style for the rendered docstring. Must be one of 'compact', 'clean', or 'expanded'.
            expected (str): The expected output string format after applying the `compose` function with the specified `rendering_style`.
    
        Returns:
            None: This function does not return any value but raises an assertion error if the generated docstring does not match the expected output.
    
        Examples:
            >>> test_compose(RenderingStyle.COMPACT, "Short description\n\nLong description")
            # This example tests the `test_compose` function with a compact rendering style and expects a specific short and long description format.
    
            >>> test_compose(RenderingStyle.CLEAN, "Short description\n\nLong description")
            # This example tests the same but with a clean rendering style to ensure it handles different styles correctly.
        """
        docstring = parse(
            """
            Short description.
    
            Long description.
    
            :param int foo: a description
            :param int bar: another description
            :return float: a return
            """
        )
>       assert compose(docstring, rendering_style=rendering_style) == expected
E       AssertionError: assert 'Short descri...oat: a return' == 'Short descri...g description'
E         
E         - Short description
E         + Short description.
E         ?                  +
E           
E         - Long description
E         + Long description....
E         
E         ...Full output truncated (5 lines hidden), use '-vv' to show

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_compose_0_test_valid_case_clean.py:40: AssertionError
_ test_compose[RenderingStyle.EXPANDED-Short description\n\nLong description] __

rendering_style = <RenderingStyle.EXPANDED: 3>
expected = 'Short description\n\nLong description'

    @pytest.mark.parametrize("rendering_style, expected", [
        (RenderingStyle.COMPACT, "Short description\n\nLong description"),
        (RenderingStyle.CLEAN, "Short description\n\nLong description"),
        (RenderingStyle.EXPANDED, "Short description\n\nLong description")
    ])
    def test_compose(rendering_style: RenderingStyle, expected: str) -> None:
        """Test compose function to ensure it correctly renders a parsed docstring into the specified format.
    
        This function takes a `rendering_style` and an `expected` string as inputs. It parses a sample ReST-style docstring using the `parse` function, then uses the `compose` function with the provided rendering style to generate a formatted string representation of the parsed docstring. The generated string is compared against the expected string to verify correctness.
    
        Parameters:
            rendering_style (RenderingStyle): Specifies the desired formatting style for the rendered docstring. Must be one of 'compact', 'clean', or 'expanded'.
            expected (str): The expected output string format after applying the `compose` function with the specified `rendering_style`.
    
        Returns:
            None: This function does not return any value but raises an assertion error if the generated docstring does not match the expected output.
    
        Examples:
            >>> test_compose(RenderingStyle.COMPACT, "Short description\n\nLong description")
            # This example tests the `test_compose` function with a compact rendering style and expects a specific short and long description format.
    
            >>> test_compose(RenderingStyle.CLEAN, "Short description\n\nLong description")
            # This example tests the same but with a clean rendering style to ensure it handles different styles correctly.
        """
        docstring = parse(
            """
            Short description.
    
            Long description.
    
            :param int foo: a description
            :param int bar: another description
            :return float: a return
            """
        )
>       assert compose(docstring, rendering_style=rendering_style) == expected
E       AssertionError: assert 'Short descri...:rtype: float' == 'Short descri...g description'
E         
E         - Short description
E         + Short description.
E         ?                  +
E           
E         - Long description
E         + Long description....
E         
E         ...Full output truncated (11 lines hidden), use '-vv' to show

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_compose_0_test_valid_case_clean.py:40: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_compose_0_test_valid_case_clean.py::test_compose[RenderingStyle.COMPACT-Short description\n\nLong description]
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_compose_0_test_valid_case_clean.py::test_compose[RenderingStyle.CLEAN-Short description\n\nLong description]
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_compose_0_test_valid_case_clean.py::test_compose[RenderingStyle.EXPANDED-Short description\n\nLong description]
============================== 3 failed in 0.03s ===============================
"""