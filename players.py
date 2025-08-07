import streamlit as st
import pandas as pd

#st.code(line_number=False)

st.image("logo2.jpg",width=80)
st.title("Tonga USA Golf Tournament")
st.subheader("At the Bluerock Golf Course (East), Vallejo CA")
st.subheader("8/22 and 8/23 2025")
st.write("Players List as of 8/7/25")
st.write()
st.divider()

data = pd.read_csv("players.csv")
st.write(data)

