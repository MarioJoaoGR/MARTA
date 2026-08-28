
import pytest
from flutils.txtutils import AnsiTextWrapper

def create_ansi_text_wrapper(width=None):
    return AnsiTextWrapper(width=width)

@pytest.mark.parametrize("width, expected", [
    (40, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor. Cras a varius ligula. Phasellus ut ipsum eu erat consequat posuere."),
    (20, "Lorem ipsum dolor\nsit amet,\nconsectetur adipiscing\nelit. Cras fermentum\nmaximus auctor.\nCras a varius ligula.\nPhasellus ut ipsum eu\nerat consequat posuere.")
])
def test_wrap_ansi_text(width, expected):
    wrapper = create_ansi_text_wrapper(width)
    text = (
        '\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit.\x1b[0m '
        'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.'
    )
    wrapped_text = wrapper.fill(text)
    assert wrapped_text == expected



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 5 items

../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper__split_0.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
_ test_wrap_ansi_text[40-Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor. Cras a varius ligula. Phasellus ut ipsum eu erat consequat posuere.] _

width = 40
expected = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor. Cras a varius ligula. Phasellus ut ipsum eu erat consequat posuere.'

    @pytest.mark.parametrize("width, expected", [
        (40, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor. Cras a varius ligula. Phasellus ut ipsum eu erat consequat posuere."),
        (20, "Lorem ipsum dolor\nsit amet,\nconsectetur adipiscing\nelit. Cras fermentum\nmaximus auctor.\nCras a varius ligula.\nPhasellus ut ipsum eu\nerat consequat posuere.")
    ])
    def test_wrap_ansi_text(width, expected):
        wrapper = create_ansi_text_wrapper(width)
        text = (
            '\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit.\x1b[0m '
            'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.'
        )
        wrapped_text = wrapper.fill(text)
>       assert wrapped_text == expected
E       AssertionError: assert '\x1b[31m\x1b...rpis egestas.' == 'Lorem ipsum ...quat posuere.'
E         
E         - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor. Cras a varius ligula. Phasellus ut ipsum eu erat consequat posuere.
E         + [31m[1m[4mLorem ipsum dolor sit amet, consectetur
E         + adipiscing elit.[0m Pellentesque habitant
E         + morbi tristique senectus et netus et
E         + malesuada fames ac turpis egestas.

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper__split_0.py:19: AssertionError
_ test_wrap_ansi_text[20-Lorem ipsum dolor\nsit amet,\nconsectetur adipiscing\nelit. Cras fermentum\nmaximus auctor.\nCras a varius ligula.\nPhasellus ut ipsum eu\nerat consequat posuere.] _

width = 20
expected = 'Lorem ipsum dolor\nsit amet,\nconsectetur adipiscing\nelit. Cras fermentum\nmaximus auctor.\nCras a varius ligula.\nPhasellus ut ipsum eu\nerat consequat posuere.'

    @pytest.mark.parametrize("width, expected", [
        (40, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor. Cras a varius ligula. Phasellus ut ipsum eu erat consequat posuere."),
        (20, "Lorem ipsum dolor\nsit amet,\nconsectetur adipiscing\nelit. Cras fermentum\nmaximus auctor.\nCras a varius ligula.\nPhasellus ut ipsum eu\nerat consequat posuere.")
    ])
    def test_wrap_ansi_text(width, expected):
        wrapper = create_ansi_text_wrapper(width)
        text = (
            '\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit.\x1b[0m '
            'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.'
        )
        wrapped_text = wrapper.fill(text)
>       assert wrapped_text == expected
E       AssertionError: assert '\x1b[31m\x1b...rpis egestas.' == 'Lorem ipsum ...quat posuere.'
E         
E         - Lorem ipsum dolor
E         + [31m[1m[4mLorem ipsum dolor
E           sit amet,
E         - consectetur adipiscing
E         - elit. Cras fermentum
E         - maximus auctor....
E         
E         ...Full output truncated (11 lines hidden), use '-vv' to show

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper__split_0.py:19: AssertionError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        wrapper = create_ansi_text_wrapper()
        with pytest.raises(TypeError):
>           wrapper.fill(None)  # None is an invalid input type

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper__split_0.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/flutils/flutils/txtutils.py:423: in fill
    return super().fill(text)
/opt/conda/envs/test4py_env/lib/python3.10/textwrap.py:371: in fill
    return "\n".join(self.wrap(text))
/opt/marta/baselines/codamosa/replication/test-apps/flutils/flutils/txtutils.py:412: in wrap
    return super().wrap(text)
/opt/conda/envs/test4py_env/lib/python3.10/textwrap.py:359: in wrap
    chunks = self._split_chunks(text)
/opt/conda/envs/test4py_env/lib/python3.10/textwrap.py:345: in _split_chunks
    text = self._munge_whitespace(text)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutils.txtutils.AnsiTextWrapper object at 0x7f20faf230a0>, text = None

    def _munge_whitespace(self, text):
        """_munge_whitespace(text : string) -> string
    
        Munge whitespace in text: expand tabs and convert all other
        whitespace characters to spaces.  Eg. " foo\\tbar\\n\\nbaz"
        becomes " foo    bar  baz".
        """
        if self.expand_tabs:
>           text = text.expandtabs(self.tabsize)
E           AttributeError: 'NoneType' object has no attribute 'expandtabs'

/opt/conda/envs/test4py_env/lib/python3.10/textwrap.py:154: AttributeError
___________________________ test_custom_indentation ____________________________

    def test_custom_indentation():
        wrapper = create_ansi_text_wrapper()
        text = (
            '\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit.\x1b[0m '
            'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.'
        )
>       wrapped_text = wrapper.fill(text)

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper__split_0.py:32: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/flutils/flutils/txtutils.py:423: in fill
    return super().fill(text)
/opt/conda/envs/test4py_env/lib/python3.10/textwrap.py:371: in fill
    return "\n".join(self.wrap(text))
/opt/marta/baselines/codamosa/replication/test-apps/flutils/flutils/txtutils.py:412: in wrap
    return super().wrap(text)
/opt/conda/envs/test4py_env/lib/python3.10/textwrap.py:362: in wrap
    return self._wrap_chunks(chunks)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutils.txtutils.AnsiTextWrapper object at 0x7f20fadc3be0>
chunks = ['\x1b[31m', '\x1b[1m', '\x1b[4m', 'Lorem', ' ', 'ipsum', ...]

    def _wrap_chunks(self, chunks: List[str]) -> List[str]:
    
        lines = []
>       if self.width <= 0:
E       TypeError: '<=' not supported between instances of 'NoneType' and 'int'

/opt/marta/baselines/codamosa/replication/test-apps/flutils/flutils/txtutils.py:276: TypeError
_______________________ test_no_expansion_or_replacement _______________________

    def test_no_expansion_or_replacement():
        wrapper = create_ansi_text_wrapper()
        wrapper.expand_tabs = False
        wrapper.replace_whitespace = False
        text = (
            '\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit.\x1b[0m '
            'Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.'
        )
>       wrapped_text = wrapper.fill(text)

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper__split_0.py:43: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/flutils/flutils/txtutils.py:423: in fill
    return super().fill(text)
/opt/conda/envs/test4py_env/lib/python3.10/textwrap.py:371: in fill
    return "\n".join(self.wrap(text))
/opt/marta/baselines/codamosa/replication/test-apps/flutils/flutils/txtutils.py:412: in wrap
    return super().wrap(text)
/opt/conda/envs/test4py_env/lib/python3.10/textwrap.py:362: in wrap
    return self._wrap_chunks(chunks)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutils.txtutils.AnsiTextWrapper object at 0x7f20fb04d780>
chunks = ['\x1b[31m', '\x1b[1m', '\x1b[4m', 'Lorem', ' ', 'ipsum', ...]

    def _wrap_chunks(self, chunks: List[str]) -> List[str]:
    
        lines = []
>       if self.width <= 0:
E       TypeError: '<=' not supported between instances of 'NoneType' and 'int'

/opt/marta/baselines/codamosa/replication/test-apps/flutils/flutils/txtutils.py:276: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper__split_0.py::test_wrap_ansi_text[40-Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor. Cras a varius ligula. Phasellus ut ipsum eu erat consequat posuere.]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper__split_0.py::test_wrap_ansi_text[20-Lorem ipsum dolor\nsit amet,\nconsectetur adipiscing\nelit. Cras fermentum\nmaximus auctor.\nCras a varius ligula.\nPhasellus ut ipsum eu\nerat consequat posuere.]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper__split_0.py::test_invalid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper__split_0.py::test_custom_indentation
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper__split_0.py::test_no_expansion_or_replacement
============================== 5 failed in 0.10s ===============================
"""