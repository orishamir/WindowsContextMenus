from __future__ import annotations

from dataclasses import dataclass

from context_menu_toolkit.context_menu_locations import ContextMenuLocation
from context_menu_toolkit.features import EntryName, IFeature
from context_menu_toolkit.features.mui_verb import MUIVerb
from context_menu_toolkit.features.sub_commands import SubCommands
from context_menu_toolkit.registry_structs import RegistryKey


@dataclass
class ContextMenu:
    """Represents a context menu,
    that has a name, features, and submenus.
    """

    name: str
    features: list[IFeature]
    submenus: list[ContextMenu] = None

    def build(self) -> RegistryKey:
        """Convert the context menu to RegistryKey which can then
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

    def export_reg(self, location: ContextMenuLocation) -> list[str]:
        r"""Syntax of .reg file:
        https://support.microsoft.com/en-us/topic/how-to-add-modify-or-delete-registry-subkeys-and-values-by-using-a-reg-file-9c7f37cf-a5e9-e1cd-c4fa-2a26218a1a23
        Example:
            Windows Registry Editor Version 5.00

            [HKEY_LOCAL_MACHINE\Software\Classes\*\shell\ConvertVideo]
            "MUIVerb"="Convert mp4..."

        Arguments:
            location (ContextMenuLocation): nig?
        Returns:
            A list of lines of the file.
        """
        built_menu: RegistryKey = self.build()

        return [
            "Windows Registry Editor Version 5.00",
            "",
        ] + list(built_menu.export_reg(location))

    def _modify_because_submenus(self) -> None:
        """If we have submenus, then for whatever reason instead of using (Default) as
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
