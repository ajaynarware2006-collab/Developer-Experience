import streamlit as st


def primary_button(
    label: str,
    key: str | None = None,
):
    return st.button(
        label,
        key=key,
        type="primary",
        use_container_width=False,
    )