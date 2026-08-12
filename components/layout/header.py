import streamlit as st


def render_header(page_title: str):

    st.html(
        f"""
        <div class="devxp-header">

            <div class="devxp-header-title">
                {page_title}
            </div>

            <div class="devxp-header-right">

                <div class="devxp-search">

                    <span>
                        ⌕
                    </span>

                    <span class="devxp-search-placeholder">
                        Search...
                    </span>

                    <span class="devxp-search-key">
                        Ctrl K
                    </span>

                </div>

                <div class="devxp-icon-button">
                    ♢
                </div>

                <div class="devxp-header-avatar">
                    A
                </div>

            </div>

        </div>
        """
    )