import streamlit as st


def card(
    content: str,
    class_name: str = "",
):
    st.markdown(
        f"""
        <div class="devxp-card {class_name}">
            {content}
        </div>
        """,
        unsafe_allow_html=True,
    )