from contextlib import nullcontext as does_not_raise
import pytest
from levels.easy.factor import check_for_factor


@pytest.mark.parametrize(
    "base, factor, result, expectation",
    [
        (10, 2, True, does_not_raise()),
        (63, 7, True, does_not_raise()),
        (2450, 5, True, does_not_raise()),
        (24612, 3, True, does_not_raise()),
        (9, 2, False, does_not_raise()),
        (653, 7, False, does_not_raise()),
        (2453, 5, False, does_not_raise()),
        (24617, 3, False, does_not_raise()),
        ("hello", 11, False, pytest.raises(TypeError)),
        ("hello", True, False, pytest.raises(TypeError)),
        ("", "", False, pytest.raises(TypeError)),
    ]
)
def test_factor(base, factor, result, expectation):
    with expectation:
        assert check_for_factor(base, factor) == result