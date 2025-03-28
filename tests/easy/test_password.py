from contextlib import nullcontext as does_not_raise
import pytest
from levels.easy.password_validator import password


@pytest.mark.parametrize(
    "s, result, expectation",
    [
        ("aaa", False, does_not_raise()),
        ("12345", False, does_not_raise()),
        ("abc123", False, does_not_raise()),
        ("ABC123", False, does_not_raise()),
        ("abcABC", False, does_not_raise()),
        ("abc!@#", False, does_not_raise()),
        ("a1A", False, does_not_raise()),
        ("Abc123", False, does_not_raise()),
        (False, False, pytest.raises(TypeError)),
        ("Password123", True, does_not_raise()),
        ("P@ssw0rd1", True, does_not_raise()),
        ("AbC123xyz", True, does_not_raise()),
        ("A1bcDefG2", True, does_not_raise()),
        ("", False, does_not_raise()),
        ("A", False, does_not_raise()),
        ("123", False, does_not_raise()),
        ("!@#", False, does_not_raise()),
        (2123, False, pytest.raises(TypeError)),
    ]
)
def test_password(s, result, expectation):
    with expectation:
        assert password(s) == result