from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from context_menu_toolkit.models.access_scope import MenuAccessScope
from context_menu_toolkit.registry.registry_structs.registry_path import RegistryPath

if TYPE_CHECKING:
    from context_menu_toolkit.models.explorer_items import ExplorerItemType


@dataclass
class ContextMenuBinding:
    r"""Represents a binding for a context menu.

    Bindings determine the basic conditions for a context menu
    to appear when right-clicking items.

    For example binding a context menu to files/folders/drives mean that it displays when right-clicking them.

    Tip:
        For more advanced control of conditions see `Condition` feature, `ICondition`, and `conditions`.

    Attributes:
        menu_item_type: Determines which object type the context menu is relevant for.
                        For example files/folders/drives/etc.
                        Should be a string. See ExplorerItemType for options and descriptions.
        access_scope: Bind to current user or all users.
    """
    menu_item_type: str | ExplorerItemType
    access_scope: MenuAccessScope = MenuAccessScope.ALL_USERS

    def to_path(self) -> RegistryPath:
        r"""Compose the registry path that match the binding.

        Example:
            ```python
            ContextMenuBinding(
                MenuAccessScope.ALL_USERS,
                ExplorerItemType.ALL_FILES,
            ).construct_registry_path()
            # HKEY_LOCAL_MACHINE\Software\Classes\*\shell
            ```

            ```python
            ContextMenuBinding(
                MenuAccessScope.ALL_USERS,
                ExplorerItemType.DESKTOP_BACKGROUND,
            ).construct_registry_path()
            # HKEY_LOCAL_MACHINE\Software\Classes\DesktopBackground\shell
            ```

            ```python
            ContextMenuBinding(
                MenuAccessScope.ALL_USERS,
                ExplorerItemType.SPECIFIC_FILE_TYPE.format(file_type="image"),
            ).construct_registry_path()
            # HKEY_LOCAL_MACHINE\Software\Classes\DesktopBackground\shell
            ```
        """
        self._validate_parameters_provided()

        return RegistryPath(self.access_scope) / self.menu_item_type / "shell"

    def _validate_parameters_provided(self) -> None:
        """Validate that all parameters of the chosen item type are filled.

        Example:
            ExplorerItemType.SPECIFIC_FILE_TYPE requires the `file_type` parameter.
        """
        try:
            # raises KeyError if the string contains unsubstituted arguments.
            # Example: "some {name} string".format() -> raises KeyError: name.
            #          "some string".format() -> does not raise anything.
            self.menu_item_type.format()
        except KeyError as e:
            missing_parameter, *_ = e.args
            raise ValueError(f'item type parameter not provided: "{missing_parameter}"') from None
