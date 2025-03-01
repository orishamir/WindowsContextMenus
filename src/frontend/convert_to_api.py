from src.configuration.comparers import (
    FileNameComparerConfig,
    FileSizeComparerConfig,
    ExtensionComparerConfig,
    LessThanEqualsComparerConfig,
    LessThanComparerConfig,
    GreaterThanComparerConfig,
    GreaterThanEqualsComparerConfig,
    StartswithComparerConfig,
    EndswithComparerConfig,
    EqualsComparerConfig,
    ContainsComparerConfig,
    WildcardComparerConfig,
)
from src.configuration.models import ContextMenuConfig, ConditionsConfig
from src.frontend import ConditionForm, ConditionType
from src.frontend.models import ContextMenuForm, ComparerType


def form_to_configuration(form: ContextMenuForm) -> ContextMenuConfig:
    conditions = _condition_form_to_config(form.conditions)
    return ContextMenuConfig(
        name=form.name,
        exec=form.exec,
        icon=form.icon if form.icon != "" else None,
        disabled=True if form.disabled else None,
        on_shift_click=True if form.shift_click else None,
        conditions=conditions if conditions else None,
    )


def _condition_form_to_config(forms: list[ConditionForm]) -> ConditionsConfig | None:
    config = ConditionsConfig()
    for condition_form in forms:
        if condition_form.type is ConditionType.FILE_NAME:
            config.file_name = _comparer_form_to_config(condition_form, FileNameComparerConfig)
        elif condition_form.type is ConditionType.FILE_SIZE:
            config.file_size = _comparer_form_to_config(condition_form, FileSizeComparerConfig)
        elif condition_form.type is ConditionType.EXTENSION:
            config.extension = _comparer_form_to_config(condition_form, ExtensionComparerConfig)

    if config.file_name or config.file_size or config.extension or config.or_ or config.not_:
        return config
    return None


def _comparer_form_to_config[T](condition_form: ConditionForm, comparer_config: type[T]) -> T:
    if condition_form.comparer is ComparerType.LESS_THAN_EQUALS:
        assert issubclass(comparer_config, LessThanEqualsComparerConfig)
        return comparer_config(lte=condition_form.value)

    if condition_form.comparer is ComparerType.LESS_THAN:
        assert issubclass(comparer_config, LessThanComparerConfig)
        return comparer_config(lt=condition_form.value)

    if condition_form.comparer is ComparerType.GREATER_THAN:
        assert issubclass(comparer_config, GreaterThanComparerConfig)
        return comparer_config(gt=condition_form.value)

    if condition_form.comparer is ComparerType.GREATER_THAN_EQUALS:
        assert issubclass(comparer_config, GreaterThanEqualsComparerConfig)
        return comparer_config(gte=condition_form.value)

    if condition_form.comparer is ComparerType.CONTAINS:
        assert issubclass(comparer_config, ContainsComparerConfig)
        return comparer_config(contains=condition_form.value)

    if condition_form.comparer is ComparerType.EQUALS:
        assert issubclass(comparer_config, EqualsComparerConfig)
        return comparer_config(eq=condition_form.value)

    if condition_form.comparer is ComparerType.WILDCARD:
        assert issubclass(comparer_config, WildcardComparerConfig)
        return comparer_config(wildcard=condition_form.value)

    if condition_form.comparer is ComparerType.STARTS_WITH:
        assert issubclass(comparer_config, StartswithComparerConfig)
        return comparer_config(startswith=condition_form.value)

    if condition_form.comparer is ComparerType.ENDS_WITH:
        assert issubclass(comparer_config, EndswithComparerConfig)
        return comparer_config(endswith=condition_form.value)

    raise ValueError(f"could not convert condition form to {comparer_config}")
