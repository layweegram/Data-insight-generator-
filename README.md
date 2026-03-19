# 🛡️ Sentinel Data Insight Engine (AAIC Stage 2)

This repository is a high-performance refactor of the original Data Insight Generator. It has been engineered to provide deeper business intelligence through automated heuristic analysis and interactive visualizations.

## 🚀 Key Enhancements

### 1. Performance Engineering
- **Data Caching:** Implemented `@st.cache_data` to optimize memory usage and reduce latency during data re-renders.
- **Efficient I/O:** Streamlined the CSV processing pipeline for faster uploads.

### 2. Analytical Intelligence (The Sentinel Logic)
- **Outlier Detection:** Integrated Z-score based logic to automatically flag statistical anomalies in datasets.
- **Volatility Analysis:** Added automated alerts for high variance in numeric columns to identify unstable data trends.

### 3. UI/UX Transformation
- **Interactive Visuals:** Migrated from Matplotlib to **Plotly Express**, allowing users to drill down into data points.
- **Intuitive Navigation:** Implemented a sidebar-driven interface to separate data overview, visual analytics, and AI insights.

## 🛠️ Installation & Setup
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run Data_insight_generation.py`

## 📊 Sample Analysis
The engine is tested against real-world business datasets to ensure robust anomaly detection and trend visualization.
