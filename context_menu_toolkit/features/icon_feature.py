from dataclasses import dataclass
from pathlib import Path

from context_menu_toolkit.features.ifeature import IFeature
from context_menu_toolkit.registry_structs import RegistryKey, RegistryValue, DataType

_ACCEPTED_ICON_EXTENSIONS = (
    ".ico",
    ".exe",
)


@dataclass
class Icon(IFeature):
    """
    Add an icon that will be displayed for the context menu.
    """
    path_to_icon: str

    def apply_to(self, tree: RegistryKey) -> None:
        tree.values.append(
            RegistryValue(name="Icon", type=DataType.REG_SZ, data=str(self.path_to_icon))
        )

    def __post_init__(self) -> None:
        if Path(self.path_to_icon).suffix not in _ACCEPTED_ICON_EXTENSIONS:
            raise ValueError(
                f"Icon not in acceptable extensions: {self.path_to_icon}. Available extensions: {_ACCEPTED_ICON_EXTENSIONS}"
            )
