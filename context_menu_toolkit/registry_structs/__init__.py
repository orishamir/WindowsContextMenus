"""Contains dataclasses describing registry objects.

References:
    MSDN | Structure of the Registry(https://learn.microsoft.com/en-us/windows/win32/sysinfo/structure-of-the-registry)
"""
from .registry_key import RegistryKey
from .registry_path import RegistryPath, TopLevelKey
from .registry_value import DataType, RegistryValue
