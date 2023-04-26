from __future__ import annotations

from src.registry_structs.registry_key import RegistryKey
from src.features import IFeature, EntryName
from src.features.mui_verb import MUIVerb
from src.features.sub_commands import SubCommands


class ContextMenu:
    def __init__(
            self,
            name: str,
            features: list[IFeature],
            submenus: list[ContextMenu] = None
    ):
        if submenus is None:
            submenus = []

        self.name = name
        self.features = features
        self.submenus = submenus

    def build(self) -> RegistryKey:
        cm = RegistryKey(
            self.name,
        )

        if self.submenus:
            self._modify_because_submenus()

        for feature in self.features:
            feature.apply_to(cm)

        if self.submenus:
            subkeys: list[RegistryKey] = [submenu.build() for submenu in self.submenus]

            cm.subkeys.append(
                RegistryKey("shell", subkeys=subkeys)
            )

        return cm

    def _modify_because_submenus(self):
        """
        If we have submenus, then for whatever reason instead of using (Default) as
        a way to tell the label, we need to set MUIVerb to the label.
        Also, we need to add an empty SubCommands value.
        :return:
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
