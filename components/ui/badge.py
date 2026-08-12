import streamlit as st


def badge(
    text: str,
    class_name: str = "",
):
    st.markdown(
        f"""
        <span class="devxp-badge {class_name}">
            {text}
        </span>
        """,
        unsafe_allow_html=True,
    )