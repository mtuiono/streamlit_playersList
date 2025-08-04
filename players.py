import streamlit as st
import pandas as pd

st.write("Players List")
st.write()

data = pd.read_csv("players.csv")
st.write(data)

