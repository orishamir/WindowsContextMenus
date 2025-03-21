"""Features are used for customizing the context menu."""
from .command import Command, CommandPlaceholder
from .condition import Condition
from .disabled import Disabled
from .display_text import DisplayText
from .has_lua_shield import HasLuaShield
from .icon import Icon, WindowsIcon
from .ifeature import IFeature
from .never_default import NeverDefault
from .no_working_directory import NoWorkingDirectory
from .position import Position
from .separator import Separator
from .shift_click import ShiftClick

__all__ = [
    "Command", "CommandPlaceholder",
    "Condition",
    "Disabled",
    "DisplayText",
    "HasLuaShield",
    "Icon", "WindowsIcon",
    "IFeature",
    "NeverDefault",
    "NoWorkingDirectory",
    "Position",
    "Separator",
    "ShiftClick",
]
