from contextlib import nullcontext as does_not_raise
import pytest
from levels.easy.digitize import digitize


@pytest.mark.parametrize(
    "number, result, expectation",
    [
        # Valid inputs (positive integers)
        (123, [3, 2, 1], does_not_raise()),
        (4567, [7, 6, 5, 4], does_not_raise()),
        (0, [0], does_not_raise()),  # Single digit zero
        
        # Large numbers
        (9876543210, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], does_not_raise()),

        # Valid input: single-digit number
        (9, [9], does_not_raise()),

        # Invalid input: non-integer types
        ("123", [], pytest.raises(TypeError)),
        (3.14, [], pytest.raises(TypeError)),  # Float input
        (None, [], pytest.raises(TypeError)),  # None input
        ([], [], pytest.raises(TypeError)),  # List input

        # Negative numbers
        (-123, [3, 2, 1], does_not_raise()),  # Negative integer should still work
    ]
)
def test_digitize(number, result, expectation):
    with expectation:
        assert digitize(number) == result
