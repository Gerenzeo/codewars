import pytest
from contextlib import nullcontext as does_not_raise

from levels.easy.task_is_even import is_even

@pytest.mark.parametrize(
    "n, result, expectation",
    [
        (1, False, does_not_raise()),
        (-2, True, does_not_raise()),
        ("2", False, pytest.raises(TypeError)),
        (3.0, False, does_not_raise()),
        (3, False, does_not_raise()),
        (4, True, does_not_raise()),
        (-5, False, does_not_raise()),
        (0, True, does_not_raise()),
        (2.0, True, does_not_raise()),
        (-10.0, True, does_not_raise()),
        (1000, True, does_not_raise()),
        (-999, False, does_not_raise()),
        (1e6, True, does_not_raise()),
        (-1e6, True, does_not_raise()),
    ]
)
def test_is_even(n, result, expectation):
    with expectation:
        assert is_even(n) == result