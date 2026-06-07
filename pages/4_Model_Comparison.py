import streamlit as st
import pandas as pd

st.title("📊 Model Comparison")

# ======================
# Winner Metrics
# ======================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "R² Score",
        "0.7978",
        delta="Best Model"
    )

with col2:
    st.metric(
        "RMSE",
        "9.692",
        delta="Lowest"
    )

with col3:
    st.metric(
        "MAE",
        "4.415",
        delta="Lowest"
    )

st.success("🏆 Final Selected Model: Gradient Boosting Regressor")
st.markdown("""
### Gradient Boosting Regressor

- Highest R²
- Lowest RMSE
- Lowest MAE
- Best Generalization
""")
# ======================
# Complete Model Comparison Table
# ======================

st.header("📋 Complete Model Comparison")

results = pd.DataFrame({
    "Type": [
        "Tree-Based Models",
        "Tree-Based Models",
        "Tree-Based Models",
        "Voting Ensembles",
        "Voting Ensembles",
        "Voting Ensembles",
        "Voting Ensembles",
        "Voting Ensembles",
        "Stacking Ensembles",
        "Stacking Ensembles",
        "Stacking Ensembles",
        "Stacking Ensembles",
        "Stacking Ensembles",
        "Stacking Ensembles"
    ],

    "Model": [
        "Random Forest",
        "XGBoost",
        "Gradient Boosting",
        "Voting [1,1,1]",
        "Voting [1,3,2]",
        "Voting [1,4,2]",
        "Voting [1,5,3]",
        "Voting [2,5,3]",
        "Stacking Lasso",
        "Stacking Ridge",
        "Stacking LR",
        "Stacking RF",
        "Stacking GBR",
        "Stacking XGB"
    ],

    "R²": [
        0.751264,
        0.768374,
        0.797793,
        0.782585,
        0.788158,
        0.790035,
        0.789513,
        0.788160,
        0.780971,
        0.780400,
        0.780399,
        0.750803,
        0.718373,
        0.644817
    ],

    "RMSE": [
        10.749720,
        10.373410,
        9.692284,
        10.050152,
        9.920503,
        9.876454,
        9.888741,
        9.920461,
        10.087382,
        10.100529,
        10.100544,
        10.759674,
        11.438390,
        12.845583
    ],

    "MAE": [
        4.558990,
        4.595388,
        4.414635,
        4.430305,
        4.429442,
        4.422043,
        4.434641,
        4.419982,
        4.530112,
        4.562007,
        4.562016,
        4.699166,
        4.716652,
        5.100603
    ]
})

# ======================
# Filter
# ======================

selected_type = st.selectbox(
    "🔍 Filter by Model Type",
    ["All"] + sorted(results["Type"].unique().tolist())
)

if selected_type == "All":
    filtered_results = results.copy()
else:
    filtered_results = results[
        results["Type"] == selected_type
    ].copy()

# ======================
# Sort & Rank
# ======================

filtered_results = filtered_results.sort_values(
    by="R²",
    ascending=False
)

filtered_results.insert(
    0,
    "Rank",
    range(1, len(filtered_results) + 1)
)

display_df = filtered_results

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)

# ======================
# Visualizations
# ======================

st.markdown(
    """
    <h2 style='color:#00FFFF;'>
        📈 Model Performance Visualization
    </h2>
    """,
    unsafe_allow_html=True
)
st.image(
    "images/model_comparison.png",
    use_container_width=True
)

st.markdown(
    """
    <h2 style='color:#00FFFF;'>
        ⚖️ Actual vs Predicted Sales
    </h2>
    """,
    unsafe_allow_html=True
)

st.image(
    "images/actual_vs_predicted.png",
    use_container_width=True
)

st.markdown(
    """
    <h2 style='color:#00FFFF;'>
        🔍 Residual Error Analysis
    </h2>
    """,
    unsafe_allow_html=True
)
st.image(
    "images/residual_plot.png",
    use_container_width=True
)

st.markdown(
    """
    <h2 style='color:#00FFFF;'>
        📌 Feature Importance
    </h2>
    """,
    unsafe_allow_html=True
)
st.image(
    "images/feature_importance.png",
    use_container_width=True
)

st.success("""
Top Predictive Features

1. OStk (Opening Stock)
2. PurTot (Purchase Total)
3. QohValue (Inventory Value)

These variables contributed the majority of the predictive power in the final Gradient Boosting model.
""")

# ======================
# Final Model Selection
# ======================

st.header("🎯 Why Gradient Boosting Won")

st.markdown("""
Gradient Boosting Regressor delivered the strongest overall performance across all evaluated models.

### Performance Highlights

✅ Highest R² Score (0.7978)

✅ Lowest RMSE (9.692)

✅ Lowest MAE (4.415)

### Model Analysis

Tree-based models significantly outperformed traditional regression approaches for this dataset due to their ability to capture complex nonlinear relationships between inventory features and sales.

Although Voting Ensembles achieved competitive performance, none surpassed Gradient Boosting's combination of high predictive accuracy and low error metrics.

Stacking models introduced additional complexity but did not provide meaningful improvements over Gradient Boosting.

### Final Selection

Gradient Boosting Regressor was selected as the production model because it consistently achieved the best balance between:

- Prediction Accuracy
- Error Minimization
- Generalization Performance
- Model Stability

This made it the most reliable model for forecasting medical inventory sales.
""")