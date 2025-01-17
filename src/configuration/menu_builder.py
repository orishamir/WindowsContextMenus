from typing import Generator

from pydantic import ByteSize

from src.configuration.models import ContextMenuConfig, ConditionsConfig
from src.configuration.comparers import (
    StartswithComparerConfig,
    EndswithComparerConfig,
    ContainsComparerConfig,
    EqualsComparerConfig,
    NotEqualsComparerConfig,
    LessThanComparerConfig,
    GreaterThanComparerConfig,
    LessThanEqualsComparerConfig,
    GreaterThanEqualsComparerConfig,
)
from src.comparers import (
    IComparer,
    StartsWith,
    Contains,
    Equal,
    NotEqual,
    LessThan,
    GreaterThan,
    LessThanEqual,
    GreaterThanEqual,
    EndsWith,
)
from src.conditions import (
    FileName,
    ICondition,
    And,
    FileSize,
    ExtensionType,
    Not,
    Or,
)
from src.context_menu import ContextMenu
from src.features import (
    IFeature,
    EntryName,
    Icon,
    ShiftClick,
    Command,
    ConditionFeature,
    Disabled,
)


def build_menu_from_config(config: ContextMenuConfig) -> ContextMenu:
    return ContextMenu(
        name=config.name,
        features=list(_build_features_from_config(config)),
        submenus=[
            build_menu_from_config(submenu)
            for submenu in config.sub_menus
        ],
    )


def _build_features_from_config(config: ContextMenuConfig) -> Generator[IFeature, None, None]:
    yield EntryName(name=config.name)

    if config.exec is not None:
        yield Command(command=config.exec)

    if config.icon is not None:
        yield Icon(path_to_icon=config.icon)

    if config.disabled:
        yield Disabled()

    if config.on_shift_click:
        yield ShiftClick()

    if config.conditions:
        yield ConditionFeature(_build_conditions(config.conditions))


def _build_conditions(conditions_config: ConditionsConfig) -> ICondition:
    conditions: list[ICondition] = []

    if conditions_config.file_name is not None:
        conditions.extend(
            FileName(comparer)
            for comparer in _build_comparers(conditions_config.file_name)
        )

    if conditions_config.file_size is not None:
        conditions.extend(
            FileSize(comparer=comparer)
            for comparer in _build_comparers(conditions_config.file_size)
        )

    if conditions_config.extension is not None:
        conditions.extend(
            ExtensionType(comparer=comparer)
            for comparer in _build_comparers(conditions_config.extension)
        )

    if conditions_config.or_:
        conditions.append(
            Or(
                [
                    _build_conditions(subcondition_config)
                    for subcondition_config in conditions_config.or_
                ]
            )
        )

    if conditions_config.not_:
        conditions.append(
            Not(_build_conditions(conditions_config.not_))
        )

    if len(conditions) == 1:
        return conditions[0]

    return And(conditions)


def _build_comparers(
    comparer_config: str | int | ByteSize
                     | StartswithComparerConfig
                     | EndswithComparerConfig
                     | ContainsComparerConfig
                     | EqualsComparerConfig
                     | NotEqualsComparerConfig
                     | LessThanComparerConfig
                     | GreaterThanComparerConfig
                     | LessThanEqualsComparerConfig
                     | GreaterThanEqualsComparerConfig
) -> Generator[IComparer, None, None]:
    """
    Given a comparer's config, returns all IComparers.
    One ComparerConfig can have multiple IComparers since the config specifies multiple Comparers in the same config.
    """
    if isinstance(comparer_config, str | int):
        yield Equal(to=comparer_config)

    if isinstance(comparer_config, StartswithComparerConfig) and comparer_config.startswith:
        yield StartsWith(starts_with=comparer_config.startswith)

    if isinstance(comparer_config, EndswithComparerConfig) and comparer_config.endswith:
        yield EndsWith(ends_with=comparer_config.endswith)

    if isinstance(comparer_config, ContainsComparerConfig) and comparer_config.contains:
        yield Contains(substr=comparer_config.contains)

    if isinstance(comparer_config, EqualsComparerConfig) and comparer_config.eq:
        yield Equal(to=comparer_config.eq)

    if isinstance(comparer_config, NotEqualsComparerConfig) and comparer_config.ne:
        yield NotEqual(to=comparer_config.ne)

    if isinstance(comparer_config, LessThanComparerConfig) and comparer_config.lt:
        yield LessThan(than=comparer_config.lt)

    if isinstance(comparer_config, GreaterThanComparerConfig) and comparer_config.gt:
        yield GreaterThan(than=comparer_config.gt)

    if isinstance(comparer_config, LessThanEqualsComparerConfig) and comparer_config.lte:
        yield LessThanEqual(than=comparer_config.lte)

    if isinstance(comparer_config, GreaterThanEqualsComparerConfig) and comparer_config.gte:
        yield GreaterThanEqual(than=comparer_config.gte)
