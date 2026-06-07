import streamlit as st

st.title("📦 Inventory Segmentation")

st.markdown("""
K-Means Clustering was applied to identify groups of products with similar inventory and sales characteristics.

This unsupervised machine learning technique helps businesses understand inventory behavior and improve stock management decisions.
""")

# ======================
# Elbow Method
# ======================

st.header("📉 Optimal Number of Clusters")

st.image(
    "images/elbow_method.png",
    use_container_width=True
)

st.markdown("""
The Elbow Method was used to determine the optimal number of clusters.

The curve showed a clear elbow at **K = 4**, indicating that four clusters provide a good balance between model simplicity and segmentation quality.
""")

# ======================
# Cluster Visualization
# ======================

st.header("🎯 K-Means Cluster Visualization")

st.image(
    "images/kmeans_clusters.png",
    use_container_width=True
)

st.markdown("""
The scatter plot shows how products were grouped based on inventory-related characteristics.

Each color represents a different cluster discovered by the K-Means algorithm.
""")

# ======================
# Cluster Profiles
# ======================

st.header("📊 Cluster Interpretation")

col1, col2 = st.columns(2)

with col1:
    st.info("""
### Cluster 0

**Low-Demand Products**

• Low sales volume

• Low stock movement

• Slow inventory turnover

• Requires demand monitoring
""")

    st.success("""
### Cluster 1

**Fast-Moving Products**

• High sales volume

• Frequent stock movement

• Strong customer demand

• High replenishment priority
""")

with col2:
    st.warning("""
### Cluster 2

**High-Value Products**

• High inventory value

• Significant financial investment

• Requires careful monitoring

• Important for inventory control
""")

    st.error("""
### Cluster 3

**Bulk & Moderate-Demand Products**

• Moderate sales demand

• Larger inventory quantities

• Supports routine operations

• Occasional high-volume transactions
""")

# ======================
# Business Value
# ======================

st.header("💼 Business Impact")

st.markdown("""
The clustering analysis provides actionable business insights:

✅ Inventory Optimization

✅ Better Stock Planning

✅ Improved Demand Forecasting

✅ Reduced Overstocking Risk

✅ Better Resource Allocation

✅ Data-Driven Inventory Decisions
""")

st.success("""
K-Means clustering successfully identified four distinct inventory segments, enabling more effective inventory management and strategic decision-making.
""")