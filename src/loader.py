import pandas as pd
import streamlit as st


@st.cache_data
def load_data(filepath: str):
    """
    Load dataset with Streamlit caching.
    """

    df = pd.read_csv(filepath)

    return df
