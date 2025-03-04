from __future__ import annotations

from collections.abc import Generator

from pydantic import BaseModel

from context_menu_toolkit.registry_structs.registry_value import RegistryValue


class RegistryKey(BaseModel):
    """Represents a registry key.

    References:
        [MSDN | Structure of the Registry](https://learn.microsoft.com/en-us/windows/win32/sysinfo/structure-of-the-registry)
    """

    name: str
    values: list[RegistryValue] = []
    subkeys: list[RegistryKey] = []

    def export_reg(self, location: str) -> Generator[str]:
        r"""Export the Context Menu as a .reg file format.

        Syntax of .reg file:
        <a href="https://support.microsoft.com/en-us/topic/how-to-add-modify-or-delete-registry-subkeys-and-values-by-using-a-reg-file-9c7f37cf-a5e9-e1cd-c4fa-2a26218a1a23" target="_blank">
        MSDN topic | How to add, modify, or delete registry subkeys and values by using a .reg file
        </a>.

        Example:
            ```python3
            [HKEY_LOCAL_MACHINE\Software\Classes\*\shell\ConvertVideo]
            "MUIVerb"="Convert mp4..."
            "SubCommands"=""
            ```

        Yields:
            Lines of the .reg file.
        """
        yield f"[{location}\\{self.name}]"
        for value in self.values:
            yield value.export_reg()

        yield ""
        for subkey in self.subkeys:
            yield from subkey.export_reg(f"{location}\\{self.name}")
