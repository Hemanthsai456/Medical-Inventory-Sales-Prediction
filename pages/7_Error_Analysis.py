import streamlit as st
import pandas as pd

st.title("📊 Error Analysis")

st.markdown("""
This page evaluates model performance beyond traditional metrics
and investigates where forecasting errors occur.
""")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("R² Score", "0.7978")

with c2:
    st.metric("MAE", "4.415")

with c3:
    st.metric("RMSE", "9.692")

c4, c5 = st.columns(2)

with c4:
    st.metric(
        "Models Evaluated",
        "14"
    )

with c5:
    st.metric(
        "Top Error Cases",
        "20"
    )

st.caption(
    "Gradient Boosting Regressor | Test Set Performance"
)

demand_df = pd.read_csv(
    "documentation/error_analysis/demand_group_performance.csv"
)

st.divider()

st.subheader("Demand Group Performance")

st.image(
    "documentation/error_analysis/demand_group_mae.png",
    use_container_width=True
)

st.dataframe(
    demand_df,
    use_container_width=True
)

st.info("""
Key Observation

Model accuracy remains strong for low and medium demand products,
while prediction error increases for high-demand inventory items.
""")

st.divider()

top20 = pd.read_csv(
    "documentation/error_analysis/top20_errors.csv"
)

st.subheader("Largest Prediction Error Cases")

st.image(
    "documentation/error_analysis/top20_errors_plot.png",
    use_container_width=True
)

display_df = top20[
    [
        "Actual",
        "Predicted",
        "Absolute_Error",
        "OStk",
        "PurTot",
        "QohValue"
    ]
].copy()

display_df = display_df.round(2)

with st.expander(
    "View Top 20 Error Records"
):
    st.dataframe(
        display_df,
        use_container_width=True
    )


st.divider()

st.subheader("Residual Analysis")

st.image(
    "documentation/error_analysis/residual_histogram.png",
    use_container_width=True
)

st.caption(
    "Residual analysis helps identify systematic prediction bias and forecasting uncertainty."
)

st.divider()

st.image(
    "documentation/error_analysis/residual_scatter.png",
    use_container_width=True
)

st.divider()

st.subheader("Actual vs Predicted")

st.image(
    "documentation/error_analysis/actual_vs_predicted.png",
    use_container_width=True
)

st.caption(
    "Points closer to the diagonal line indicate more accurate predictions."
)

st.divider()

st.success("""
Key Findings

• The model explains approximately 80% of sales variance.

• Prediction performance remains stable across most inventory records.

• High-demand products contribute disproportionately to forecasting error.

• Most large errors occur during extreme demand scenarios.

• Inventory-related variables remain the strongest drivers of model predictions.
""")