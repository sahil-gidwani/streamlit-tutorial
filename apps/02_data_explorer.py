import streamlit as st

from common import load_events


st.set_page_config(page_title="Data Explorer", layout="wide")
st.title("Football Data Ingestion and Cleaning")
st.caption("Module 2 demo app")

required_cols = ["match_id", "team", "player", "x", "y", "event_type", "xg"]

events = load_events()

st.sidebar.header("Cleaning Options")
drop_missing_locations = st.sidebar.toggle("Drop missing x/y", value=True)

raw_preview, cleaned_preview = st.tabs(["Raw Preview", "Cleaned Preview"])

with raw_preview:
    st.dataframe(events.head(20), use_container_width=True)

missing_report = events.isna().sum().rename("missing_count").reset_index(names="column")

cleaned = events.copy()
if drop_missing_locations:
    cleaned = cleaned.dropna(subset=["x", "y"])

with cleaned_preview:
    st.dataframe(cleaned.head(20), use_container_width=True)

st.subheader("Data Quality Report")
missing_cols = [c for c in required_cols if c not in events.columns]
if missing_cols:
    st.error(f"Missing required columns: {missing_cols}")
else:
    st.success("All required columns are present.")

st.dataframe(missing_report, use_container_width=True)

if st.button("Download cleaned CSV"):
    st.download_button(
        label="Download",
        data=cleaned.to_csv(index=False),
        file_name="cleaned_events.csv",
        mime="text/csv",
    )
