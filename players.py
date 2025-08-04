import streamlit as st
import pandas as pd

#st.code(line_number=False)

st.title("Tonga USA Golf Tournament")
st.subheader("At the Bluerock Golf Course (East), Vallejo CA")
st.subheader("August 22nd and 23rd, 2025")
st.subheader("Players List")
st.write()
st.divider()

data = pd.read_csv("players.csv")
st.write(data)

