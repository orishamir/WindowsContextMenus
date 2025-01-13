from __future__ import annotations

from dataclasses import dataclass, field
from typing import Generator

from src.registry_structs.registry_value import RegistryValue


@dataclass
class RegistryKey:
    """
    This dataclass represents a registry key as defined in https://learn.microsoft.com/en-us/windows/win32/sysinfo/structure-of-the-registry
    """

    name: str
    values: list[RegistryValue] = field(default_factory=list)
    subkeys: list[RegistryKey] = field(default_factory=list)

    def export_reg(self, location: str) -> Generator[str, None, None]:
        r"""
        Syntax of .reg file:
        https://support.microsoft.com/en-us/topic/how-to-add-modify-or-delete-registry-subkeys-and-values-by-using-a-reg-file-9c7f37cf-a5e9-e1cd-c4fa-2a26218a1a23
        Example:
            [HKEY_LOCAL_MACHINE\Software\Classes\*\shell\ConvertVideo]
            "MUIVerb"="Convert mp4..."
            "SubCommands"=""
        """
        yield f"[{location}\\{self.name}]"
        for value in self.values:
            yield value.export_reg()

        yield ""
        for subkey in self.subkeys:
            yield from subkey.export_reg(f"{location}\\{self.name}")
