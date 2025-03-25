import pytest
from contextlib import nullcontext as does_not_raise

from levels.easy.alternating_case import to_alternating_case

@pytest.mark.parametrize(
    "string, result, expectation",
    [
        ("124bC=", "124Bc=", does_not_raise()),
        ("abcd", "ABCD", does_not_raise()),
        ("", "", does_not_raise()),
        (2, "", pytest.raises(TypeError)),
        (True, "", pytest.raises(TypeError)),
        ("AbC", "aBc", does_not_raise()),
        ("123456", "123456", does_not_raise()),
        ("!@#AbCd123", "!@#aBcD123", does_not_raise()),
        ("ABCDE", "abcde", does_not_raise()),
        ("a", "A", does_not_raise()),
        ("A", "a", does_not_raise()),
        ("123!@#", "123!@#", does_not_raise()),
    ]
)
def test_to_alternating_case(string, result, expectation):
    with expectation:
        assert to_alternating_case(string) == result
