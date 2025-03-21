import pytest

from context_menu_toolkit.registry_structs.registry_path import RegistryPath

TESTS_TRAILING_SLASH: list[tuple[str, str]] = [
    ("HKEY_CURRENT_USER\\Software\\", "HKEY_CURRENT_USER\\Software"),
    ("HKEY_CURRENT_USER\\Software\\\\\\\\", "HKEY_CURRENT_USER\\Software"),
    ("\\\\HKEY_CURRENT_USER\\Software\\\\\\\\", "HKEY_CURRENT_USER\\Software"),
    ("//HKEY_CURRENT_USER\\Software\\\\\\\\", "HKEY_CURRENT_USER\\Software"),
    ("//HKEY_CURRENT_USER\\Software//\\/\\", "HKEY_CURRENT_USER\\Software"),
]

TESTS_MIDDLE_SLASH: list[tuple[str, str]] = [
    ("HKEY_CURRENT_USER\\Software", "HKEY_CURRENT_USER\\Software"),
    ("HKEY_CURRENT_USER\\\\Software", "HKEY_CURRENT_USER\\Software"),
    ("HKEY_CURRENT_USER/Software", "HKEY_CURRENT_USER\\Software"),
    ("HKEY_CURRENT_USER///Software", "HKEY_CURRENT_USER\\Software"),
    ("HKEY_CURRENT_USER/\\/Software", "HKEY_CURRENT_USER\\Software"),
    ("HKEY_CURRENT_USER///\\\\/Software", "HKEY_CURRENT_USER\\Software"),
]

TESTS_UPPERCASE_TOPKEY: list[tuple[str, str]] = [
    ("hkey_current_user\\Software\\", "HKEY_CURRENT_USER\\Software"),
    ("hkey_current_user\\Software\\\\\\\\", "HKEY_CURRENT_USER\\Software"),
    ("\\\\hkey_current_user\\Software\\\\\\\\", "HKEY_CURRENT_USER\\Software"),
    ("//hkey_current_user\\Software\\\\\\\\", "HKEY_CURRENT_USER\\Software"),
    ("//hkey_current_user\\Software//\\/\\", "HKEY_CURRENT_USER\\Software"),
    ("hkey_current_user\\Software", "HKEY_CURRENT_USER\\Software"),
    ("hkey_current_user\\\\Software", "HKEY_CURRENT_USER\\Software"),
    ("hkey_current_user/Software", "HKEY_CURRENT_USER\\Software"),
    ("hkey_current_user///Software", "HKEY_CURRENT_USER\\Software"),
    ("hkey_current_user/\\/Software", "HKEY_CURRENT_USER\\Software"),
    ("hkey_current_user///\\\\/Software", "HKEY_CURRENT_USER\\Software"),
]

TESTS_EDGE_CASES: list[tuple[str, str]] = [
    # ("", ""),
]

@pytest.mark.parametrize(
    ("input_path", "expected"),
    [
        *TESTS_TRAILING_SLASH,
        *TESTS_MIDDLE_SLASH,
        *TESTS_UPPERCASE_TOPKEY,
        *TESTS_EDGE_CASES,
    ],
)
def test_normalize_raw_path(input_path: str, expected: str) -> None:
    """Tests the normalize_raw_path() method."""
    assert RegistryPath._normalize_raw_path(input_path) == expected  # type: ignore
