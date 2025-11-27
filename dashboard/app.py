import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
from utils.db import get_latest_data

# Force pandas to avoid pyarrow dependency
pd.set_option("mode.data_manager", "block")

st.set_page_config(page_title="Crypto Dashboard", layout="wide")

st.title("📈 Live Crypto Dashboard")
st.caption("Streaming real-time crypto prices from your ingestion pipeline.")

# Fetch data
df = get_latest_data(limit=50)

if df is None or df.empty:
    st.warning("No data found in database yet. Start ingestion first!")
else:
    st.subheader("Latest Crypto Prices")
    st.dataframe(df, use_container_width=True)

