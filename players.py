import streamlit as st
import pandas as pd
import datetime


#st.code(line_number=False)

#st.image("logo2.jpg",width=80)
st.title("TUGC 2025 Golf Tournament")
st.subheader("Bluerock Golf Course,Vallejo CA, 8/22 and 8/23")
st.write("Players List as of 8/17/25 ")


st.divider()

data = pd.read_csv("players.csv")
st.write(data)

