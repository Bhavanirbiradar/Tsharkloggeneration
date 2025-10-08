import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Network Packet Analyzer", layout="wide")
st.title("📡 Network Packet Analyzer Dashboard")

uploaded_file = st.file_uploader("Upload your packet CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    st.subheader("🔍 Raw Data Preview")
    st.dataframe(data.head(10))

    st.subheader("📊 Protocol Distribution")
    protocol_counts = data["Protocol"].value_counts()
    fig1, ax1 = plt.subplots()
    protocol_counts.plot(kind="bar", ax=ax1)
    st.pyplot(fig1)

    if "Source IP" in data.columns:
        st.subheader("🌐 Top 5 Source IPs")
        top_sources = data["Source IP"].value_counts().head(5)
        fig2, ax2 = plt.subplots()
        top_sources.plot(kind="bar", color="lightgreen", ax=ax2)
        st.pyplot(fig2)

    st.subheader("📏 Packet Length Distribution")
    fig3, ax3 = plt.subplots()
    ax3.hist(data["Length"], bins=20)
    st.pyplot(fig3)

    st.subheader("📈 Summary Statistics")
    st.write(data.describe())
else:
    st.info("👆 Please upload your packet_analysis.csv or packets.csv file to start.")
