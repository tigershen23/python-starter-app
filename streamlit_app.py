import streamlit as st

from myapplication.main import main


def run_streamlit_app() -> None:
    # Call the main function and capture its output
    import io
    import sys

    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    main()

    output = new_stdout.getvalue().strip()
    sys.stdout = old_stdout

    # Display the output in a Streamlit h1 element
    st.markdown(f"# {output}")
    # st.markdown("# HWorld")


if __name__ == "__main__":
    run_streamlit_app()
