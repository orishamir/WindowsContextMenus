from pathlib import Path

from src.exceptions import NotAFileError, BadIconExtensionError
from src.features import IFeature
from src.registry_structs import RegistryKey, RegistryValue, ValueType

ICON_FEATURE_VALUE = "Icon"
ACCEPTED_ICON_EXTENSIONS = (
    ".ico",
    ".png",
    ".jpg",
    ".jpeg",
    ".exe",
)


def _validate_path(path_to_icon: Path):
    if not path_to_icon.exists():
        raise FileNotFoundError(f"Icon {path_to_icon} not found.")

    if not path_to_icon.is_file():
        raise NotAFileError(f"Icon {path_to_icon} is not a file.")

    if path_to_icon.suffix not in ACCEPTED_ICON_EXTENSIONS:
        raise BadIconExtensionError(
            f"Icon {path_to_icon} should be any of these extensions: {ACCEPTED_ICON_EXTENSIONS}"
        )


class Icon(IFeature):
    """
    Add an icon for the context menu item's label.
    """

    def __init__(self, path_to_icon: Path | str):
        if not isinstance(path_to_icon, Path | str):
            raise TypeError("path_to_icon should be of type Path or str.")

        _validate_path(path_to_icon)

        self.path_to_icon = Path(path_to_icon)

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(ICON_FEATURE_VALUE, ValueType.REG_SZ, self.path_to_icon)
        )
