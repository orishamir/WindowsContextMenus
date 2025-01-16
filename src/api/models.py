from __future__ import annotations

from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field, ByteSize

from src.api.comparers import FileNameComparerConfig, FileSizeComparerConfig, ExtensionComparerConfig


class ContextMenuConfig(BaseModel):
    display_name: str
    exec: Optional[str] = None
    icon: Optional[Path] = None
    disabled: Optional[bool] = None
    on_shift_click: Optional[bool] = None
    conditions: Optional[ConditionsConfig] = None
    sub_menus: list[ContextMenuConfig] = []


class ConditionsConfig(BaseModel):
    file_name: Optional[str | FileNameComparerConfig] = None
    file_size: Optional[ByteSize | FileSizeComparerConfig] = None
    extension: Optional[str | ExtensionComparerConfig] = None

    or_: Optional[list[ConditionsConfig]] = Field(None, alias="$or")
    not_: Optional[ConditionsConfig] = Field(None, alias="$not")
