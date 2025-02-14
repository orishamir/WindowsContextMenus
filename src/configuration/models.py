from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from src.configuration.comparers import FileNameComparerConfig, FileSizeComparerConfig, ExtensionComparerConfig
from src.configuration.custom_types import StrByteSize


class ContextMenuConfig(BaseModel):
    name: str
    exec: Optional[str] = None
    icon: Optional[str] = None
    disabled: Optional[bool] = None
    on_shift_click: Optional[bool] = None
    conditions: Optional[ConditionsConfig] = None
    sub_menus: list[ContextMenuConfig] = []


class ConditionsConfig(BaseModel):
    file_name: Optional[str | FileNameComparerConfig] = None
    file_size: Optional[StrByteSize | FileSizeComparerConfig] = None
    extension: Optional[str | ExtensionComparerConfig] = None

    or_: Optional[list[ConditionsConfig]] = Field(None, alias="$or")
    not_: Optional[ConditionsConfig] = Field(None, alias="$not")
