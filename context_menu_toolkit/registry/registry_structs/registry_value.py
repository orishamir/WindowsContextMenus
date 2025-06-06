import json
import winreg
from enum import IntEnum

from pydantic import BaseModel


class DataType(IntEnum):
    """Some constant data types.

    References:
        [^1]: <https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-value-types>
    """

    REG_BINARY = winreg.REG_BINARY
    REG_DWORD = winreg.REG_DWORD
    REG_SZ = winreg.REG_SZ
    REG_EXPAND_SZ = winreg.REG_EXPAND_SZ


class RegistryValue(BaseModel):
    """Represents a registry value."""

    name: str
    type: DataType
    data: str | int

    def export_reg(self) -> str:
        """Export the registry value as a .reg file format.

        Example:
            ```
            "MUIVerb"="Convert mp4..."
            ```

        Returns:
            The .reg file line representing the registry value.

        References:
            [^1]: <https://support.microsoft.com/en-us/topic/how-to-add-modify-or-delete-registry-subkeys-and-values-by-using-a-reg-file-9c7f37cf-a5e9-e1cd-c4fa-2a26218a1a23>
        """
        if self.type is DataType.REG_SZ:
            data_str = json.dumps(self.data)  # escapes "\" and '"'
        elif self.type is DataType.REG_DWORD:
            data_str = f"dword:{self.data}"
        else:
            raise NotImplementedError(f"registry data type not supported: {self.type}")

        if self.name == "":
            return f"@={data_str}"
        return f'"{self.name}"={data_str}'
