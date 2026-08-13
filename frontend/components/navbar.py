import streamlit as st


def render_navbar():
    st.html(
        """
        <nav class="devxp-navbar">

            <div class="devxp-brand">

                <div class="devxp-brand-mark">
                    D
                </div>

                <div>
                    DEV<span>/</span>XP
                </div>

            </div>


            <div class="devxp-nav-right">

                <div class="devxp-nav-link">
                    Features
                </div>

                <div class="devxp-nav-link">
                    How it works
                </div>

                <div class="devxp-nav-link">
                    About
                </div>

            </div>

        </nav>
        """
    )