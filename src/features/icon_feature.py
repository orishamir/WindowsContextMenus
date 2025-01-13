from pathlib import Path

from src.exceptions import NotAFileError, BadIconExtensionError
from src.features.ifeature import IFeature
from src.registry_structs import RegistryKey, RegistryValue, DataType

ICON_FEATURE_VALUE = "Icon"
ACCEPTED_ICON_EXTENSIONS = (
    ".ico",
    ".exe",
)


def _validate_path(path_to_icon: Path):
    if not path_to_icon.exists():
        raise FileNotFoundError(f"Icon not found: {path_to_icon}")

    if not path_to_icon.is_file():
        raise NotAFileError(f"Icon is not a file: {path_to_icon}")

    if path_to_icon.suffix not in ACCEPTED_ICON_EXTENSIONS:
        raise BadIconExtensionError(
            f"Icon not in acceptable extensions: {path_to_icon}. Available extensions: {ACCEPTED_ICON_EXTENSIONS}"
        )


class Icon(IFeature):
    """
    Add an icon for the context menu item's label.
    """

    def __init__(self, path_to_icon: Path | str):
        if not isinstance(path_to_icon, Path | str):
            raise TypeError("path_to_icon should be of type Path or str.")

        self.path_to_icon = Path(path_to_icon)

        _validate_path(self.path_to_icon)

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(ICON_FEATURE_VALUE, DataType.REG_SZ, str(self.path_to_icon))
        )
