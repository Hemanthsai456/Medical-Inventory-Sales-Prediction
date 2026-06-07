import streamlit as st
from utils.prediction import predict_sales

st.title("🔮 Sales Prediction")

# ======================
# Numeric Inputs
# ======================

packing = st.number_input(
    "Packing",
    min_value=0.0,
    value=None,
    placeholder="Enter Packing"
)

ostk = st.number_input(
    "Opening Stock (OStk)",
    min_value=0.0,
    value=None,
    placeholder="Enter Opening Stock"
)

purtot = st.number_input(
    "Purchase Total (PurTot)",
    min_value=0.0,
    value=None,
    placeholder="Enter Purchase Total"
)

qohvalue = st.number_input(
    "Quantity on Hand Value (QohValue)",
    min_value=0.0,
    value=None,
    placeholder="Enter Quantity on Hand Value"
)

# ======================
# Product Type
# ======================

product_type = st.selectbox(
    "Product Type",
    [
        "dose",
        "gram",
        "kit",
        "lot",
        "ml",
        "sach",
        "tab",
        "unit",
        "vial",
        "x"
    ]
)

# ======================
# Prediction
# ======================

if st.button("Predict Sales"):

    if None in [packing, ostk, purtot, qohvalue]:
        st.warning("⚠️ Please fill all numeric fields.")
    else:
        prediction = predict_sales(
            packing,
            ostk,
            purtot,
            qohvalue,
            product_type
        )

        st.success(
            f"✅ Predicted SaleTot: {prediction:.2f}"
        )