import streamlit as st 

def rendersem():
    col1 , back_col = st.columns([9,1])
    with col1:
        st.success("Done")

    with back_col:
        if st.button("x"):
            st.session_state["page"] = "landing"

