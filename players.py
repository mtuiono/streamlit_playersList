import streamlit as st
from IPython.display import display, HTML
import pandas as pd

def create_scrollable_table(df, table_id, title, height='200px'):
    html = f'<h3>{title}</h3>'
    html += f'<div id="{table_id}" style="height:{height}; overflow:auto;">'
    html += df.to_html()
    html += '</div>'
    return html


#st.code(line_number=False)

st.image("logo2.jpg",width=80)
st.title("TUGC 2025 Tournament")
st.subheader("Bluerock Golf Course,Vallejo CA, 8/22 and 8/23")
st.write("Players List as of 8/7/25")
st.write()
st.divider()

data = pd.read_csv("players.csv")

df = pd.DataFrame(data) # Your DataFrame
html_output = create_scrollable_table(df, 'my_dataframe_table', 'My Scrollable DataFrame', height='300px')
display(HTML(html_output))

#st.write(data)




# Example usage:
# 
# 
# 

