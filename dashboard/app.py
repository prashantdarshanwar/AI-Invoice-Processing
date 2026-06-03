import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000"

st.set_page_config(
    page_title="Invoice AI Dashboard",
    layout="wide"
)

st.title("📄 Invoice AI Dashboard")

# =====================
# Upload Invoice
# =====================

st.subheader("📤 Upload Invoice")

uploaded_file = st.file_uploader(
    "Choose Invoice",
    type=["pdf", "png", "jpg", "jpeg", "bmp"]
)

if uploaded_file is not None:

    if st.button("Upload Invoice"):

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                uploaded_file.type
            )
        }

        response = requests.post(
            f"{API_URL}/invoice/upload",
            files=files
        )

        if response.status_code == 200:

            st.success(
                "Invoice Uploaded Successfully"
            )

            st.json(
                response.json()
            )

        else:

            st.error(
                "Upload Failed"
            )

# =====================
# Dashboard Metrics
# =====================

data = requests.get(
    f"{API_URL}/dashboard"
).json()

st.subheader("📊 Dashboard Metrics")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total",
    data["total_invoices"]
)

col2.metric(
    "Approved",
    data["approved"]
)

col3.metric(
    "Pending",
    data["pending"]
)

col4.metric(
    "Rejected",
    data["rejected"]
)

col5.metric(
    "Errors",
    data["error"]
)

# =====================
# Invoice Table
# =====================

st.subheader("📋 All Invoices")

response = requests.get(
    f"{API_URL}/invoice"
)

if response.status_code == 200:

    invoices = response.json()

    if invoices:

        df = pd.DataFrame(
            invoices
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.info(
            "No invoices found"
        )