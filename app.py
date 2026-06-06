import streamlit as st
import pandas as pd
import numpy as np

my_name = st.secrets["name"]
st.write(my_name)

student1 = st.secrets.student1

st.write(student1)

st.markdown("""
            # This is a header
            ## This is a sub header!
            """)

def get_select_box_data():

    return pd.DataFrame({
          'first column': list(range(1, 11)),
          'second column': np.arange(10, 101, 10)
        })

df = get_select_box_data()

option = st.selectbox('Select a line to filter', df['first column'])

filtered_df = df[df['first column'] == option]

st.write(filtered_df)

if st.button('click me'):
    # print is visible in the server output, not in the page
    print('button clicked!')
    st.write('I was clicked 🎉')
    st.write('Further clicks are not visible but are executed')
else:
    st.write('I was not clicked 😞')
