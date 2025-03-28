"""Features are used for customizing the context menu."""
from .command import Command, CommandPlaceholder
from .conditionfeature import ConditionFeature
from .disabled import Disabled
from .display_text import DisplayText
from .icon_feature import Icon, WindowsIcon
from .ifeature import IFeature
from .never_default import NeverDefault
from .no_working_directory import NoWorkingDirectory
from .position import Position
from .selection_model import SelectionModel, SelectionModelAmount
from .separator import Separator
from .shift_click import ShiftClick

__all__ = [
    "Command", "CommandPlaceholder",
    "ConditionFeature",
    "Disabled",
    "DisplayText",
    "Icon", "WindowsIcon",
    "IFeature",
    "NeverDefault",
    "NoWorkingDirectory",
    "Position",
    "SelectionModel", "SelectionModelAmount",
    "Separator",
    "ShiftClick",
]
