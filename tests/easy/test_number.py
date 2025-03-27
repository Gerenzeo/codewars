from contextlib import nullcontext as does_not_raise
import pytest
from levels.easy.task_number import number




@pytest.mark.parametrize(
    "lines, result, expectation",
    [
        (["a", "b", "c"], ["1: a", "2: b", "3: c"], does_not_raise()),
        ([1, 2, 3], ["1: 1", "2: 2", "3: 3"], does_not_raise()),
        (["", "", ""], ["1: ", "2: ", "3: "], does_not_raise()),
        ([], [], does_not_raise()),
        (["single"], ["1: single"], does_not_raise()),
        ([1.1, 2.2, 3.3], ["1: 1.1", "2: 2.2", "3: 3.3"], does_not_raise()),
        (list(range(1000)), [f"{i+1}: {i}" for i in range(1000)], does_not_raise()),
    ]
)
def test_number(lines, result, expectation):
    with expectation:
        assert number(lines) == result
        