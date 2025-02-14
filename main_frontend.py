from typing import Callable, Any

import requests
import streamlit as st

from src.frontend import ConditionType, CONDITION_TYPE_TO_COMPARER, ContextMenuForm, ConditionForm
from src.frontend.convert_to_api import form_to_configuration

st.set_page_config(layout="wide")


def _file_size_ui(key) -> Any | None:
    l, r = st.columns([0.6, 0.4])
    val = l.number_input("count", min_value=0, step=50, label_visibility="hidden", key=f"{key}-count")
    units = r.selectbox("size_units", ["B", "KB", "MB", "GB"], label_visibility="hidden", key=f"{key}-units", index=None)
    if units is None:
        return None

    return f"{val}{units}"


def _string_ui(key) -> Any | None:
    s = st.text_input("str", placeholder="value", label_visibility="hidden", key=f"{key}-stringinput")
    if not s:
        return None
    return s


CONDITION_TYPE_TO_UI: dict[ConditionType, Callable[[int], Any | None]] = {
    ConditionType.FILE_SIZE: _file_size_ui,
    ConditionType.FILE_NAME: _string_ui,
    ConditionType.EXTENSION: _string_ui,
}


def get_condition(key) -> ConditionForm:
    """
    Condition is the combination of
    "Condition type" - (file name, extension, etc.)
    "Comparer type" - (gt, lte, etc.)
    "Value" - the value itself
    """
    with st.container(border=True):
        condition_type = st.selectbox("Condition Type", list(ConditionType), label_visibility="hidden", index=None, key=f"{key}-condition_type")
        if condition_type is None:
            return ConditionForm()

        comparer_type = st.selectbox(
            f"Comparer Type",
            CONDITION_TYPE_TO_COMPARER[condition_type],
            label_visibility="hidden",
            index=None,
            key=f"{key}-comparer_type"
        )
        if comparer_type is None:
            return ConditionForm(type=condition_type)

        value = CONDITION_TYPE_TO_UI[condition_type](key)
        if value is None:
            return ConditionForm(type=condition_type, comparer=comparer_type)

        return ConditionForm(
            type=condition_type,
            comparer=comparer_type,
            value=value,
        )


def get_conditions(key) -> list[ConditionForm]:
    with st.expander("Conditions"):
        conditions = []

        i = 0
        while True:
            new_condition = get_condition(key=f"{key}-{i}")
            if new_condition.type is None or new_condition.value is None:
                # incomplete condition so stop
                break

            conditions.append(new_condition)
            i += 1
        return conditions


st.title('Context menu creator')

with st.sidebar.container(border=True):
    st.text("Context Menu Options")

    name = st.text_input("Name")
    exec = st.text_input("Exec", placeholder="cmd.exe /c start chrome www.google.com")
    icon = st.text_input("Icon", placeholder="D:\\Pictures\\icon.ico")
    shift_click = st.toggle("On Shift Click")
    disabled = st.toggle("Disabled")

    conditions = get_conditions(key=1)

    context_menu = ContextMenuForm(
        name=name,
        exec=exec,
        icon=icon,
        shift_click=shift_click,
        disabled=disabled,
        conditions=conditions,
    )

print(context_menu)

config = form_to_configuration(context_menu)

# exported_reg = r"""
# Windows Registry Editor Version 5.00
#
# [HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Shell Extensions\Blocked]
# "{1FA0E654-C9F2-4A1F-9800-B9A75D744B00}"=-
#
# [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Shell Extensions\Blocked]
# "{1FA0E654-C9F2-4A1F-9800-B9A75D744B00}"=-
# """

r = requests.post("http://127.0.0.1:8000/make-reg-file", json=config.model_dump())
st.code(r.text)
st.download_button("Download .reg", data=r.text, file_name=f"{context_menu.name}.reg")
print(config)
