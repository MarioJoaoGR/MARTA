
import pytest
from flutils.txtutils import AnsiTextWrapper

def len_without_ansi(text):
    return len(re.sub('\x1b\[.*?m', '', text))

@pytest.mark.parametrize("width, initial_indent, subsequent_indent, expand_tabs, replace_whitespace, fix_sentence_endings, break_long_words, drop_whitespace, break_on_hyphens, tabsize, max_lines, placeholder", [
    (40, '> ', '  ', True, True, False, True, True, True, 8, None, ' [...]'),
    (60, '', '', True, True, False, True, True, True, 8, 3, ' [TRUNCATED]')
])
def test_AnsiTextWrapper(width, initial_indent, subsequent_indent, expand_tabs, replace_whitespace, fix_sentence_endings, break_long_words, drop_whitespace, break_on_hyphens, tabsize, max_lines, placeholder):
    text = (
        '\x1b[31m\x1b[1m\x1b[4mLorem ipsum dolor sit amet, consectetur adipiscing elit. Cras fermentum maximus auctor. Cras a varius ligula. Phasellus ut ipsum eu erat consequat posuere.\x1b[0m Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas ultricies lacus id massa interdum dignissim. Curabitur \x1b[38;2;55;172;230m efficitur ante sit amet nibh consectetur, consequat rutrum nunc\x1b[0m egestas. Duis mattis arcu eget orci euismod, sit amet vulputate ante scelerisque. Aliquam ultrices, turpis id gravida vestibulum, tortor ipsum consequat mauris, eu cursus nisi felis at felis. Quisque blandit lacus nec mattis suscipit. Proin sed tortor ante. Praesent fermentum orci id dolor \x1b[38;5;208meuismod, quis auctor nisl sodales.\x1b[0m'
    )
    
    wrapper = AnsiTextWrapper(width=width, initial_indent=initial_indent, subsequent_indent=subsequent_indent, expand_tabs=expand_tabs, replace_whitespace=replace_whitespace, fix_sentence_endings=fix_sentence_endings, break_long_words=break_long_words, drop_whitespace=drop_whitespace, break_on_hyphens=break_on_hyphens, tabsize=tabsize, max_lines=max_lines, placeholder=placeholder)
    wrapped_text = wrapper.fill(text)
    
    assert isinstance(wrapped_text, str), "Expected a string but got something else"
    if max_lines:
        lines = wrapped_text.split('\n')
        assert len(lines) <= max_lines, f"Expected at most {max_lines} lines but got {len(lines)}"
    
    # Additional assertions can be added to check specific properties of the wrapped text
