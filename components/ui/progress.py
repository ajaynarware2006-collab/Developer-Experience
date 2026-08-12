import streamlit as st


def progress_bar(
    value: int | float,
    show_value: bool = True,
):
    value = max(0, min(100, value))

    value_text = (
        f"{value:.0f}%"
        if show_value
        else ""
    )

    st.markdown(
        f"""
        <div style="margin: 6px 0 12px;">

            <div class="progress-track">

                <div
                    class="progress-fill"
                    style="width: {value}%"
                ></div>

            </div>

            {
                f'''
                <div style="
                    margin-top: 5px;
                    color: #7B837A;
                    font-size: 10px;
                ">
                    {value_text}
                </div>
                '''
                if show_value
                else ""
            }

        </div>
        """,
        unsafe_allow_html=True,
    )