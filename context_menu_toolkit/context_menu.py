from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from context_menu_toolkit.context_menu_bindings import ContextMenuBinding
from context_menu_toolkit.features import EntryName, IFeature
from context_menu_toolkit.features.mui_verb import MUIVerb
from context_menu_toolkit.features.sub_commands import SubCommands
from context_menu_toolkit.registry_structs import RegistryKey


@dataclass
class ContextMenu:
    """Represents a context menu.

    Attributes:
        name: The name of the context menu, as it would appear in the registry when applied.
        features: The list of features to use. See [Features](../features/index.md).
        submenus: An optional list of submenus.
    """

    name: str
    features: list[IFeature]
    submenus: list[ContextMenu] | None = None

    def build(self) -> RegistryKey:
        """Build context menu as registry.

        Builds the context menu to RegistryKey which can then
        be added to the registry in the correct location.

        Returns:
            The registry-key representation of the context menu.
        """
        cm = RegistryKey(name=self.name)

        if self.submenus:
            self._modify_because_submenus()

        for feature in self.features:
            feature.apply_to(cm)

        if self.submenus:
            subkeys: list[RegistryKey] = [submenu.build() for submenu in self.submenus]

            cm.subkeys.append(
                RegistryKey(name="shell", subkeys=subkeys),
            )

        return cm

    def export_reg(self, bindings: list[ContextMenuBinding]) -> list[str]:
        r"""Export the Context Menu as a .reg file format.

        Syntax of .reg file:
        <https://support.microsoft.com/en-us/topic/how-to-add-modify-or-delete-registry-subkeys-and-values-by-using-a-reg-file-9c7f37cf-a5e9-e1cd-c4fa-2a26218a1a23>

        Example:
            ```
            Windows Registry Editor Version 5.00

            [HKEY_LOCAL_MACHINE\Software\Classes\*\shell\ConvertVideo]
            "MUIVerb"="Convert mp4..."
            ```

        Returns:
            A list of lines of the .reg file.
        """
        built_menu: RegistryKey = self.build()

        lines = [
            "Windows Registry Editor Version 5.00",
            "",
            "; Created by: ContextMenuToolkit @ https://github.com/orishamir/WindowsContextMenus/",
            f"; Created on: {datetime.now().strftime('%B %d, %Y')}",
            "",
        ]

        for i, binding in enumerate(bindings):
            lines.append(f";;; menu for binding #{i+1}: access_scope={binding.access_scope.name}, item_type={binding.menu_item_type}")
            lines.extend(
                built_menu.export_reg(
                    binding.construct_registry_path(),
                ),
            )
            lines.append(f";;; end of menu for binding #{i+1}: access_scope={binding.access_scope.name}, item_type={binding.menu_item_type}")

        return lines

    def _modify_because_submenus(self) -> None:
        """Modify context menu to allow for submenus.

        If we have submenus, then for whatever reason instead of using (Default) as
        a way to tell the label, we need to set MUIVerb to the label.
        Also, we need to add an empty SubCommands value.
        """
        self.features = [
            MUIVerb(feature.name) if isinstance(feature, EntryName) else feature
            for feature in self.features
        ]
        self.features.append(SubCommands())

        for submenu in self.submenus:
            submenu.features = [
                MUIVerb(feature.name) if isinstance(feature, EntryName) else feature
                for feature in submenu.features
            ]
