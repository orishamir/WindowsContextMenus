from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

from context_menu_toolkit.registry.registry_structs.registry_path import RegistryPath  # noqa: TC001
from context_menu_toolkit.registry.registry_structs.registry_value import RegistryValue  # noqa: TC001

if TYPE_CHECKING:
    from collections.abc import Generator


class RegistryKey(BaseModel):
    """Represents a registry key.

    References:
        [MSDN | Structure of the Registry](https://learn.microsoft.com/en-us/windows/win32/sysinfo/structure-of-the-registry)
    """

    name: str
    values: list[RegistryValue] = []
    subkeys: list[RegistryKey] = []

    def add_subkey(self, key: RegistryKey) -> None:
        self.subkeys.append(key)

    def add_value(self, value: RegistryValue) -> None:
        self.values.append(value)

    def export_reg(self, location: RegistryPath) -> Generator[str]:
        r"""Export the Context Menu as a .reg file format.

        Syntax of .reg file:
        <https://support.microsoft.com/en-us/topic/how-to-add-modify-or-delete-registry-subkeys-and-values-by-using-a-reg-file-9c7f37cf-a5e9-e1cd-c4fa-2a26218a1a23>.

        Example:
            ```python3
            [HKEY_LOCAL_MACHINE\Software\Classes\*\shell\ConvertVideo]
            "MUIVerb"="Convert mp4..."
            "SubCommands"=""
            ```

        Yields:
            Lines of the .reg file.
        """
        yield f"[{location / self.name}]"
        for value in self.values:
            yield value.export_reg()

        yield ""
        for subkey in self.subkeys:
            yield from subkey.export_reg(location / self.name)

    def contains_subkey(self, name: str) -> bool:
        return any(subkey.name.lower() == name.lower() for subkey in self.subkeys)

    def contains_value(self, name: str) -> bool:
        return any(value.name.lower() == name.lower() for value in self.values)

    def get_value(self, name: str) -> RegistryValue | None:
        for value in self.values:
            if value.name.lower() == name.lower():
                return value
        return None

    def get_subkey(self, name: str) -> RegistryKey | None:
        for subkey in self.subkeys:
            if subkey.name.lower() == name.lower():
                return subkey
        return None
