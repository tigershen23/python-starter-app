"""Streamlit application module."""

import streamlit as st

from myapplication.main import (
    main,
)


def run_streamlit_app() -> None:
    """Run the Streamlit application."""
    # Call the main function and capture its output
    import io
    import sys

    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()

    main()

    sys.stdout = old_stdout
    output = buffer.getvalue().strip()

    # Display the output in a Streamlit h1 element
    st.markdown(
        f"# {output}",
    )


if __name__ == "__main__":
    run_streamlit_app()
