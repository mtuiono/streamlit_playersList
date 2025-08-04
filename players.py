import streamlit as st
import pandas as pd

st.write("Tonga USA Golf Tournament 2025 at Bluerock Golf Course, Vallejo CA")
st.write("August 22nd and 23rd, 2025")
st.write("Players List")
st.write()

data = pd.read_csv("players.csv")
st.write(data)

