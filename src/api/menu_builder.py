from typing import Generator

from src.api.models import ContextMenuConfig, ConditionsConfig
from src.api.comparers import (
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
        name="whatever for now",
        features=list(_build_features_from_config(config)),
        submenus=[
            build_menu_from_config(submenu)
            for submenu in config.sub_menus
        ],
    )


def _build_features_from_config(config: ContextMenuConfig) -> Generator[IFeature, None, None]:
    yield EntryName(name=config.display_name)

    yield Command(command=config.exec)

    if config.icon is not None:
        yield Icon(path_to_icon=config.icon)

    if config.disabled is True:
        yield Disabled()

    if config.on_shift_click is True:
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

    if conditions_config.and_:
        conditions.append(
            And(
                [
                    _build_conditions(subcondition_request)
                    for subcondition_request in conditions_config.and_
                ]
            )
        )

    if conditions_config.or_:
        conditions.append(
            Or(
                [
                    _build_conditions(subcondition_request)
                    for subcondition_request in conditions_config.or_
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
    condition: str | int
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
    Given a condition's config, returns
    """
    if isinstance(condition, str | int):
        yield Equal(to=condition)

    if isinstance(condition, StartswithComparerConfig) and condition.startswith:
        yield StartsWith(starts_with=condition.startswith)

    if isinstance(condition, EndswithComparerConfig) and condition.endswith:
        yield EndsWith(ends_with=condition.endswith)

    if isinstance(condition, ContainsComparerConfig) and condition.contains:
        yield Contains(substr=condition.contains)

    if isinstance(condition, EqualsComparerConfig) and condition.eq:
        yield Equal(to=condition.eq)

    if isinstance(condition, NotEqualsComparerConfig) and condition.ne:
        yield NotEqual(to=condition.ne)

    if isinstance(condition, LessThanComparerConfig) and condition.lt:
        yield LessThan(than=condition.lt)

    if isinstance(condition, GreaterThanComparerConfig) and condition.gt:
        yield GreaterThan(than=condition.gt)

    if isinstance(condition, LessThanEqualsComparerConfig) and condition.lte:
        yield LessThanEqual(than=condition.lte)

    if isinstance(condition, GreaterThanEqualsComparerConfig) and condition.gte:
        yield GreaterThanEqual(than=condition.gte)
