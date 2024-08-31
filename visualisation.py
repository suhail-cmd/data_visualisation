import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.title("Data Visualization Dashboard")


st.write("Upload your CSV file to visualize the data.")


uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    
    st.write("Data Preview:")
    st.write(df.head())

    
    st.subheader("Data Cleaning and Preprocessing")
    if st.checkbox("Drop rows with missing values"):
        df = df.dropna()

    
    selected_columns = st.multiselect("Select columns to visualize", df.columns.tolist(), df.columns.tolist())
    df = df[selected_columns]

    
    st.subheader("Visualization Options")
    chart_type = st.selectbox("Choose a chart type", ["Bar Chart", "Line Chart", "Scatter Plot", "Histogram"])

    if chart_type == "Bar Chart":
        x_axis = st.selectbox("Choose X-axis", df.columns)
        y_axis = st.selectbox("Choose Y-axis", df.columns)
        fig, ax = plt.subplots()
        sns.barplot(data=df, x=x_axis, y=y_axis, ax=ax)
        st.pyplot(fig)

    elif chart_type == "Line Chart":
        x_axis = st.selectbox("Choose X-axis", df.columns)
        y_axis = st.selectbox("Choose Y-axis", df.columns)
        fig, ax = plt.subplots()
        sns.lineplot(data=df, x=x_axis, y=y_axis, ax=ax)
        st.pyplot(fig)

    elif chart_type == "Scatter Plot":
        x_axis = st.selectbox("Choose X-axis", df.columns)
        y_axis = st.selectbox("Choose Y-axis", df.columns)
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=x_axis, y=y_axis, ax=ax)
        st.pyplot(fig)

    elif chart_type == "Histogram":
        column = st.selectbox("Choose column", df.columns)
        fig, ax = plt.subplots()
        sns.histplot(df[column], bins=30, ax=ax)
        st.pyplot(fig)
else:
    st.write("Please upload a CSV file.")