import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Data Insight Generator")

uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.write(df.head())

    st.subheader("Dataset Summary")
    st.write(df.describe())

    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    numeric_cols = df.select_dtypes(include=['float64','int64']).columns

    if len(numeric_cols) > 0:

        st.subheader("Histogram")

        column = st.selectbox("Select column", numeric_cols)

        fig, ax = plt.subplots()
        sns.histplot(df[column], kde=True, ax=ax)
        st.pyplot(fig)

        st.subheader("Correlation Heatmap")

        fig2, ax2 = plt.subplots()
        sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax2)
        st.pyplot(fig2)

    st.subheader("AI Insights")

    insights = []

    for col in numeric_cols:
        mean = df[col].mean()
        max_val = df[col].max()
        min_val = df[col].min()

        insights.append(
            f"The variable {col} has an average value of {mean:.2f}, "
            f"a maximum of {max_val}, and a minimum of {min_val}."
        )

    for insight in insights:
        st.write(insight)



