import streamlit as st


def render_navbar():
    st.html(
        f"""
        <nav class="devxp-navbar">

            <div class="devxp-brand">

                <div class="devxp-brand-mark">
                    {"D"}
                </div>

                <div>
                    D<span style="font-size : 17px;">EV</span> X<span style="font-size : 17px;">P</span>
                </div>

            </div>


        </nav>
        """
    )

    col1 , col2 , col3 = st.columns(3)

    with col1:
        if st.button("Feature",key="feature-button"):
            st.session_state["page"] = "features"

    with col2:
        if st.button("how it work"):
            st.session_state["page"] = "how_it_work"

    with col3:
        if st.button("About"):
            st.session_state["page"] = "about"