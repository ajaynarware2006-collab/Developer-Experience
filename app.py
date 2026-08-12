import streamlit as st

from styles.theme import inject_global_css
from components.ui.card import card
from components.ui.badge import badge
from components.ui.progress import progress_bar
from components.ui.button import primary_button


inject_global_css()

st.title("DEV/XP Component Test")

card(
    """
    <h3>Python</h3>
    <p>Strong backend programming skill.</p>
    """
)

badge("Strong")

progress_bar(92)

clicked = primary_button("Test Button")

if clicked:
    st.success("Button works!")