import pytest
from contextlib import nullcontext as does_not_raise

from levels.easy.clock import past

@pytest.mark.parametrize(
    "h, m, s, result, expectaion",
    [
        (1, 1, 1, 3661000, does_not_raise()),
        (None, "2", 10, 0, pytest.raises(TypeError)),
        ("1", "1", "1", 0, pytest.raises(TypeError)),
    ]
)
def test_past(h, m, s, result, expectaion: does_not_raise):
    with expectaion:
        assert past(h, m, s) == result