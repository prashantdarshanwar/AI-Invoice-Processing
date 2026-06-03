import streamlit as st
import requests

data = requests.get(
    "http://localhost:8000/dashboard"
).json()

st.title("Invoice AI Dashboard")

col1, col2 = st.columns(2)

col1.metric(
    "Total Invoices",
    data["total_invoices"]
)

col2.metric(
    "Approved",
    data["approved"]
)

st.metric(
    "Pending",
    data["pending"]
)

st.metric(
    "Rejected",
    data["rejected"]
)

st.metric(
    "Errors",
    data["error"]
)