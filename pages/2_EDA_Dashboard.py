import streamlit as st

st.title("📊 Exploratory Data Analysis")

st.markdown("""
Exploratory Data Analysis (EDA) was performed to understand inventory behavior,
sales patterns, supplier performance, stock movement, and demand characteristics.

The analysis helped identify important business insights before building the
machine learning models.
""")

# ==================================================
# Fast Moving Products
# ==================================================

st.header("🚀 Fast Moving Products")

st.image(
    "images/EDA_images/fast_moving_products.png",
    use_container_width=True
)

st.info("""
Products in this category showed the highest sales frequency and inventory movement.

These products require regular replenishment and should be prioritized during stock planning.
""")

# ==================================================
# High Turnover Companies
# ==================================================

st.header("🏢 High Turnover Companies")

st.image(
    "images/EDA_images/high_turnover_companies.png",
    use_container_width=True
)

st.info("""
These companies generated the highest sales value and contributed significantly to business revenue.

Understanding supplier performance helps optimize procurement decisions.
""")

# ==================================================
# Inventory Hoarding Companies
# ==================================================

st.header("📦 Inventory Hoarding Companies")

st.image(
    "images/EDA_images/inventory_hoarding_companies.png",
    use_container_width=True
)

st.warning("""
Some companies maintained significantly larger inventory levels than others.

Excess inventory may increase holding costs and reduce operational efficiency.
""")

# ==================================================
# Purchase vs Sales
# ==================================================

st.header("💰 Purchase Value vs Sales Value")

st.image(
    "images/EDA_images/purchase_vs_sales.png",
    use_container_width=True
)

st.info("""
The scatter plot shows the relationship between purchasing activity and sales performance.

A positive relationship suggests that higher procurement generally supports higher sales.
""")

# ==================================================
# Stock vs Sales
# ==================================================

st.header("📈 Stock vs Sales Analysis")

st.image(
    "images/EDA_images/stock_vs_sales.png",
    use_container_width=True
)

st.info("""
This visualization highlights how inventory levels relate to product sales.

Products with high stock but low sales may indicate overstocking, while low stock with high sales may indicate potential shortages.
""")

# ==================================================
# Overstocked Products
# ==================================================

st.header("⚠️ Overstocked Products")

st.image(
    "images/EDA_images/overstocked_products.png",
    use_container_width=True
)

st.warning("""
These products maintain high stock levels despite relatively low sales activity.

Such products should be monitored to reduce inventory carrying costs.
""")

# ==================================================
# Business Summary
# ==================================================

st.header("🎯 Key Business Insights")

st.success("""
✅ Fast-moving products drive inventory turnover.

✅ Supplier performance varies significantly across companies.

✅ Overstocked products can increase inventory costs.

✅ Purchase activity strongly influences sales outcomes.

✅ Inventory optimization opportunities exist across multiple product groups.

These insights were used to support feature engineering, model development,
and inventory segmentation throughout the project.
""")