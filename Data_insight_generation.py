import streamlit as st
import pandas as pd
import plotly.express as px # Upgraded to Plotly for Premium visuals
import plotly.graph_objects as go

# 1. SETTING THE STAGE (UI/UX)
st.set_page_config(page_title="Sentinel Data Insight", layout="wide")
st.title("🛡️ Sentinel Data Insight Generator")
st.markdown("---")

# 2. THE "MEMORY" UPGRADE (Optimization)
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

uploaded_file = st.sidebar.file_uploader("Step 1: Upload Dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    df = load_data(uploaded_file)
    
    # SIDEBAR NAVIGATION
    menu = st.sidebar.radio("Navigation", ["Overview", "Visual Analytics", "Sentinel AI Insights"])

    if menu == "Overview":
        st.subheader("📋 Dataset Intelligence")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Rows", df.shape[0])
        col2.metric("Total Columns", df.shape[1])
        col3.metric("Missing Values", df.isnull().sum().sum())
        
        st.write("### Data Preview")
        st.dataframe(df.head(10), use_container_width=True)

    elif menu == "Visual Analytics":
        st.subheader("📊 Interactive Visualization")
        numeric_cols = df.select_dtypes(include=['float64','int64']).columns
        
        if len(numeric_cols) > 0:
            column = st.selectbox("Select target variable", numeric_cols)
            
            # UPGRADED PLOTLY CHART
            fig = px.histogram(df, x=column, title=f"Distribution of {column}", 
                               template="plotly_dark", color_discrete_sequence=['#00CC96'])
            st.plotly_chart(fig, use_container_width=True)
            
            st.subheader("Correlation Intelligence")
            corr = df[numeric_cols].corr()
            fig2 = px.imshow(corr, text_auto=True, aspect="auto", title="Feature Correlation Matrix")
            st.plotly_chart(fig2, use_container_width=True)

    elif menu == "Sentinel AI Insights":
        st.subheader("🧠 Automated Logic Engine")
        numeric_cols = df.select_dtypes(include=['float64','int64']).columns
        
        for col in numeric_cols:
            mean = df[col].mean()
            std = df[col].std()
            
            # ADDING ACTUAL LOGIC (The "Engineering" part)
            with st.expander(f"Analysis for {col}"):
                st.write(f"**Average Performance:** {mean:.2f}")
                if std > (mean * 0.5):
                    st.warning(f"⚠️ High Volatility detected in {col}. Data points are spread out significantly.")
                else:
                    st.success(f"✅ Consistent Data: {col} shows stable patterns.")
                
                # Outlier Detection
                outliers = df[df[col] > (mean + 3*std)]
                if not outliers.empty:
                    st.error(f"🚨 Anomalies Found: We detected {len(outliers)} unusual spikes in {col} that require attention.")
