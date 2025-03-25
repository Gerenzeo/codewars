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
    ]
)
def test_to_alternating_case(string, result, expectation):
    with expectation:
        assert to_alternating_case(string) == result