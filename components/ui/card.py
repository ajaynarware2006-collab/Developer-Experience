import streamlit as st


def card(
    content: str,
    class_name: str = "",
    ):
    html = f"""
    <div class="devxp-card {class_name}">
    {content}
    </div>
    """

    st.markdown(
        html,
        unsafe_allow_html=True,
    )