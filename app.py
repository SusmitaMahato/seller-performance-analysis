import streamlit as st
from analysis import load_data

st.title("Seller Performance Dashboard")

df = load_data()
st.dataframe(df)
st.bar_chart(df.set_index("seller_name")["ratings"])
st.bar_chart(df.set_index("seller_name")["revenue"])
