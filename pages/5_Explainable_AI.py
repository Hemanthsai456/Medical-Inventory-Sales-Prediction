import streamlit as st

st.title("🧠 Explainable AI (SHAP)")

st.markdown("""
Machine Learning models can make highly accurate predictions, but understanding *why* a prediction was made is equally important.

This project uses **SHAP (SHapley Additive exPlanations)** to interpret the Gradient Boosting Regressor and identify which inventory features most strongly influence sales predictions.
""")

# ======================
# SHAP Summary Plot
# ======================

st.header("📊 SHAP Summary Plot")

st.image(
    "images/shap_summary.png",
    use_container_width=True
)

st.markdown("""
### What This Plot Shows

The SHAP Summary Plot provides a global explanation of the model by showing:

- Which features are most important overall
- Whether a feature increases or decreases predicted sales
- How strongly each feature impacts predictions

### Key Insights

- Features at the top have the greatest influence on sales predictions.
- Features with larger SHAP values contribute more strongly to model decisions.
- The plot helps identify the most important inventory and stock-related variables.
""")

# ======================
# SHAP Waterfall Plot
# ======================

st.header("🌊 SHAP Waterfall Plot")

st.image(
    "images/shap_waterfall.png",
    use_container_width=True
)

st.markdown("""
### What This Plot Shows

The SHAP Waterfall Plot explains a **single prediction** made by the final Gradient Boosting model.

Starting from the model's average prediction:

- Blue bars decrease the prediction
- Red bars increase the prediction

The combined contribution of all features produces the final predicted sales value.

### Example Interpretation

In this prediction:

- Opening Stock (OStk) had the largest negative impact.
- Purchase Total (PurTot) also reduced the prediction.
- Product type and packing contributed positively.
- The final prediction was obtained by combining all feature contributions.

This provides transparency into how the model arrives at individual predictions.
""")

# ======================
# Why Explainability Matters
# ======================

st.header("🎯 Why Explainability Matters")

st.info("""
Explainable AI helps stakeholders trust machine learning predictions by showing which factors drive model decisions.

For inventory management, explainability helps:

• Understand key sales drivers

• Validate model behavior

• Support business decision-making

• Increase confidence in forecasting results
""")