"""
Contains dataclasses describing registry objects as defined in
<a herf="https://learn.microsoft.com/en-us/windows/win32/sysinfo/structure-of-the-registry" target="_blank">MSDN | Structure of the Registry</a>
"""
from .registry_key import RegistryKey
from .registry_value import DataType, RegistryValue
