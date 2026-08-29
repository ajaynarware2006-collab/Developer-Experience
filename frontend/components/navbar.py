import streamlit as st


def render_navbar():

    st.html(
        """
        <style>

            .devxp-navbar {

                width: 100%;
                height: 78px;

                display: flex;
                align-items: center;
                justify-content: space-between;

                padding: 18px 0;

                border-bottom: 1px solid
                    rgba(255, 255, 255, 0.07);
            }


            .devxp-brand {

                display: flex;
                align-items: center;

                gap: 11px;

                color: #F4F7F5;

                font-size: 22px;
                font-weight: 850;

                letter-spacing: -0.7px;
            }


            .devxp-brand-mark {

                width: 38px;
                height: 38px;

                display: flex;
                align-items: center;
                justify-content: center;

                border-radius: 11px;

                background:
                    linear-gradient(
                        135deg,
                        #087B84,
                        #12AAB3
                    );

                color: #FFFFFF;

                font-size: 15px;
                font-weight: 900;

                box-shadow:
                    0 8px 25px
                    rgba(18, 170, 179, 0.22);
            }


            .devxp-brand span {
                color: #9ED33C;
            }

        </style>


        <nav class="devxp-navbar">

            <div class="devxp-brand">

                <div class="devxp-brand-mark">
                    D
                </div>

                <div>
                    D<span>EV</span>X<span>P</span>
                </div>

            </div>

        </nav>
        """
    )


    # ============================================================
    # NAVIGATION
    # ============================================================

    col1, col2, col3, col4 = st.columns(
        [5, 1, 1.25, 0.8]
    )


    with col2:

        if st.button(
            "Features",
            key="feature-button",
        ):

            st.session_state["page"] = "features"
            st.rerun()


    with col3:

        if st.button(
            "How it works",
            key="how-it-works-button",
        ):

            st.session_state["page"] = "how_it_work"
            st.rerun()


    with col4:

        if st.button(
            "About",
            key="about-button",
        ):

            st.session_state["page"] = "about"
            st.rerun()