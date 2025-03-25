import pytest
from contextlib import nullcontext as does_not_raise

from levels.easy.remove_exclamation_marks import remove_exclamation_marks


@pytest.mark.parametrize(
    "s, result, expectation",
    [
        ("Hello world!", "Hello world", does_not_raise()),
        ("Hello! Mr. Born!", "Hello Mr. Born", does_not_raise()),
        ("Hello world", "Hello world", pytest.raises(ValueError)),
        (1, "", pytest.raises(TypeError)),
        (True, True, pytest.raises(TypeError)),
        ("!a!b!c!", "abc", does_not_raise()),
        ("", "", pytest.raises(ValueError)),
        ("!!!", "", does_not_raise()),
        ("!   !", "   ", does_not_raise()),
        ("abc", "abc", pytest.raises(ValueError)),
        ("123!456!", "123456", does_not_raise()),
        ("!Hello! World!", "Hello World", does_not_raise()),
    ]
)
def test_remove_exclamation_marks(s, result, expectation):
    with expectation:
        assert remove_exclamation_marks(s) == result
