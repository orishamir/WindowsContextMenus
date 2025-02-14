import json
import winreg
from enum import IntEnum
from typing import Any

from pydantic import BaseModel


class DataType(IntEnum):
    """
    Some constant value types as defined in
    https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-value-types
    """

    REG_BINARY = winreg.REG_BINARY
    REG_DWORD = winreg.REG_DWORD
    REG_SZ = winreg.REG_SZ


class RegistryValue(BaseModel):
    """
    Represents a registry value as defined in
    https://learn.microsoft.com/en-us/windows/win32/sysinfo/structure-of-the-registry
    """

    name: str
    type: DataType
    data: Any

    def export_reg(self) -> str:
        """
        Syntax of .reg file:
        https://support.microsoft.com/en-us/topic/how-to-add-modify-or-delete-registry-subkeys-and-values-by-using-a-reg-file-9c7f37cf-a5e9-e1cd-c4fa-2a26218a1a23
        Example:
            "MUIVerb"="Convert mp4..."
        Returns:
            A list of lines of the file.
        """
        assert self.type in (DataType.REG_SZ, DataType.REG_DWORD)

        if self.type is DataType.REG_SZ:
            data_str = json.dumps(self.data)  # escapes "\" and '"'
        elif self.type is DataType.REG_DWORD:
            data_str = f"dword:{self.data}"

        if self.name == "":
            return f"@={data_str}"
        return f'"{self.name}"={data_str}'
