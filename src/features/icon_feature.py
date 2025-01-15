from dataclasses import dataclass
from pathlib import Path

from src.features.ifeature import IFeature
from src.registry_structs import RegistryKey, RegistryValue, DataType

ICON_FEATURE_VALUE = "Icon"
ACCEPTED_ICON_EXTENSIONS = (
    ".ico",
    ".exe",
)


@dataclass
class Icon(IFeature):
    """
    Add an icon for the context menu item's label.
    """
    path_to_icon: str

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name=ICON_FEATURE_VALUE, type=DataType.REG_SZ, data=str(self.path_to_icon))
        )

    def __post_init__(self):
        if Path(self.path_to_icon).suffix not in ACCEPTED_ICON_EXTENSIONS:
            raise ValueError(
                f"Icon not in acceptable extensions: {self.path_to_icon}. Available extensions: {ACCEPTED_ICON_EXTENSIONS}"
            )
