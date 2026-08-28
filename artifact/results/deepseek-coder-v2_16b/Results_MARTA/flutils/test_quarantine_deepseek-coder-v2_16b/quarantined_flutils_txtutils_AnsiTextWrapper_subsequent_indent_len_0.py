
import pytest
from flutils.txtutils import AnsiTextWrapper

def len_without_ansi(text):
    return len(strip_ansi(text))

def strip_ansi(text):
    if not text:
        return ""
    ansi_escape = re.compile(r'(?:\x1b\[[\d;]*[mGKH])')
    return ansi_escape.sub('', text)

@pytest.mark.parametrize("input_type", [None, 123, [], {}])
def test_error_case(input_type):
    wrapper = AnsiTextWrapper()
    with pytest.raises(TypeError):
        wrapped_text = wrapper.fill(input_type)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 5 items

../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper_subsequent_indent_len_0.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
____________________________ test_error_case[None] _____________________________

input_type = None

    @pytest.mark.parametrize("input_type", [None, 123, [], {}])
    def test_error_case(input_type):
        wrapper = AnsiTextWrapper()
        with pytest.raises(TypeError):
>           wrapped_text = wrapper.fill(input_type)

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper_subsequent_indent_len_0.py:18: 
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

self = <flutils.txtutils.AnsiTextWrapper object at 0x7f384fd86440>, text = None

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
_____________________________ test_error_case[123] _____________________________

input_type = 123

    @pytest.mark.parametrize("input_type", [None, 123, [], {}])
    def test_error_case(input_type):
        wrapper = AnsiTextWrapper()
        with pytest.raises(TypeError):
>           wrapped_text = wrapper.fill(input_type)

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper_subsequent_indent_len_0.py:18: 
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

self = <flutils.txtutils.AnsiTextWrapper object at 0x7f384fecf1c0>, text = 123

    def _munge_whitespace(self, text):
        """_munge_whitespace(text : string) -> string
    
        Munge whitespace in text: expand tabs and convert all other
        whitespace characters to spaces.  Eg. " foo\\tbar\\n\\nbaz"
        becomes " foo    bar  baz".
        """
        if self.expand_tabs:
>           text = text.expandtabs(self.tabsize)
E           AttributeError: 'int' object has no attribute 'expandtabs'

/opt/conda/envs/test4py_env/lib/python3.10/textwrap.py:154: AttributeError
_________________________ test_error_case[input_type2] _________________________

input_type = []

    @pytest.mark.parametrize("input_type", [None, 123, [], {}])
    def test_error_case(input_type):
        wrapper = AnsiTextWrapper()
        with pytest.raises(TypeError):
>           wrapped_text = wrapper.fill(input_type)

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper_subsequent_indent_len_0.py:18: 
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

self = <flutils.txtutils.AnsiTextWrapper object at 0x7f384fc77d30>, text = []

    def _munge_whitespace(self, text):
        """_munge_whitespace(text : string) -> string
    
        Munge whitespace in text: expand tabs and convert all other
        whitespace characters to spaces.  Eg. " foo\\tbar\\n\\nbaz"
        becomes " foo    bar  baz".
        """
        if self.expand_tabs:
>           text = text.expandtabs(self.tabsize)
E           AttributeError: 'list' object has no attribute 'expandtabs'

/opt/conda/envs/test4py_env/lib/python3.10/textwrap.py:154: AttributeError
_________________________ test_error_case[input_type3] _________________________

input_type = {}

    @pytest.mark.parametrize("input_type", [None, 123, [], {}])
    def test_error_case(input_type):
        wrapper = AnsiTextWrapper()
        with pytest.raises(TypeError):
>           wrapped_text = wrapper.fill(input_type)

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper_subsequent_indent_len_0.py:18: 
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

self = <flutils.txtutils.AnsiTextWrapper object at 0x7f384fd85690>, text = {}

    def _munge_whitespace(self, text):
        """_munge_whitespace(text : string) -> string
    
        Munge whitespace in text: expand tabs and convert all other
        whitespace characters to spaces.  Eg. " foo\\tbar\\n\\nbaz"
        becomes " foo    bar  baz".
        """
        if self.expand_tabs:
>           text = text.expandtabs(self.tabsize)
E           AttributeError: 'dict' object has no attribute 'expandtabs'

/opt/conda/envs/test4py_env/lib/python3.10/textwrap.py:154: AttributeError
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        text = (
            '\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor. Cras a varius ligula. Phasellus ut ipsum eu erat consequat posuere.\x1b[0m Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas ultricies lacus id massa interdum dignissim. Curabitur \x1b[38;2;55;172;230m efficitur ante sit amet nibh consectetur, consequat rutrum nunc\x1b[0m egestas. Duis mattis arcu eget orci euismod, sit amet vulputate ante scelerisque. Aliquam ultrices, turpis id gravida vestibulum, tortor ipsum consequat mauris, eu cursus nisi felis at felis. Quisque blandit lacus nec mattis suscipit. Proin sed tortor ante. Praesent fermentum orci id dolor \x1b[38;5;208meuismod, quis auctor nisl sodales.\x1b[0m'
        )
        wrapper = AnsiTextWrapper(width=40)
        wrapped_text = wrapper.fill(text)
        assert isinstance(wrapped_text, str), "Expected a string output"
>       assert len(wrapped_text) <= wrapper.width, f"Wrapped text exceeds the width limit of {wrapper.width}"
E       AssertionError: Wrapped text exceeds the width limit of 40
E       assert 759 <= 40
E        +  where 759 = len('\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, consectetur\nadipiscing elit. Cras fermentum maximus\nauctor. Cras ...it. Proin sed tortor ante.\nPraesent fermentum orci id dolor \x1b[38;5;208m\neuismod, quis auctor nisl sodales.\x1b[0m')
E        +  and   40 = <flutils.txtutils.AnsiTextWrapper object at 0x7f384fda65c0>.width

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper_subsequent_indent_len_0.py:27: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper_subsequent_indent_len_0.py::test_error_case[None]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper_subsequent_indent_len_0.py::test_error_case[123]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper_subsequent_indent_len_0.py::test_error_case[input_type2]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper_subsequent_indent_len_0.py::test_error_case[input_type3]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_txtutils_AnsiTextWrapper_subsequent_indent_len_0.py::test_valid_case
============================== 5 failed in 0.15s ===============================
"""